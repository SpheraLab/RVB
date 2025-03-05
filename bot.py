import os
import time
import requests
import feedparser

# 🔍 DEBUG: Stampiamo le variabili d'ambiente per verificare se Railway le sta leggendo
print(f"🔍 Debug: TELEGRAM_BOT_TOKEN = {os.getenv('TELEGRAM_BOT_TOKEN')}")
print(f"🔍 Debug: CHAT_ID = {os.getenv('CHAT_ID')}")
print(f"🔍 Debug: RSS_FEED_URL = {os.getenv('RSS_FEED_URL')}")

# ✅ Carica le variabili d'ambiente da Railway
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()
RSS_FEED_URL = os.getenv("RSS_FEED_URL", "").strip()

# ❌ Controlliamo se le variabili sono impostate, altrimenti fermiamo il bot
if not TELEGRAM_BOT_TOKEN:
    print("❌ ERRORE: La variabile TELEGRAM_BOT_TOKEN non è impostata!")
    exit(1)

if not CHAT_ID:
    print("❌ ERRORE: La variabile CHAT_ID non è impostata!")
    exit(1)

if not RSS_FEED_URL:
    print("❌ ERRORE: La variabile RSS_FEED_URL non è impostata!")
    exit(1)

print("✅ Tutte le variabili d'ambiente sono impostate correttamente!")

# Funzione per inviare messaggi su Telegram
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("✅ Messaggio inviato con successo!")
    else:
        print(f"⚠️ Errore nell'invio del messaggio: {response.text}")

# Variabile per tracciare l'ultimo articolo inviato
last_entry = None

# Loop per controllare gli RSS ogni 60 secondi
while True:
    print("🔄 Controllo nuovi articoli...")
    feed = feedparser.parse(RSS_FEED_URL)

    if not feed.entries:
        print("⚠️ Nessun articolo trovato nel feed!")
    else:
        latest_entry = feed.entries[0]  # Prende l'ultimo articolo pubblicato
        if last_entry is None or latest_entry.link != last_entry:
            message = f"📢 Nuovo articolo: {latest_entry.title}\n{latest_entry.link}"
            send_telegram_message(message)
            last_entry = latest_entry.link

    print("⏳ Aspetto 60 secondi prima del prossimo controllo...")
    time.sleep(60)
