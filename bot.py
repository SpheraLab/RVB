import os
import time
import requests
import feedparser

# Legge le variabili d'ambiente da Railway
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()
RSS_FEED_URL = os.getenv("RSS_FEED_URL", "").strip()

# Controlla se tutte le variabili d'ambiente sono impostate
if not TELEGRAM_BOT_TOKEN:
    print("❌ ERRORE: La variabile TELEGRAM_BOT_TOKEN non è impostata!")
    exit(1)

if not CHAT_ID:
    print("❌ ERRORE: La variabile CHAT_ID non è impostata!")
    exit(1)

if not RSS_FEED_URL:
    print("❌ ERRORE: La variabile RSS_FEED_URL non è impostata!")
    exit(1)

print(f"✅ Configurazione OK!")
print(f"📡 RSS_FEED_URL: {RSS_FEED_URL}")

# Funzione per inviare messaggi su Telegram
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ Messaggio inviato con successo!")
    else:
        print(f"⚠️ Errore nell'invio
