import feedparser
import requests
import time

# Configurazione
TELEGRAM_BOT_TOKEN = "7829474341:AAG4xOxcjrsuJytIj-zT1CNUg_9riLvANnk"
CHAT_ID = "214258536"
RSS_FEED_URL = "https://corrierealpi.gelocal.it/belluno/rss/copertina.xml"  # Sostituiscilo con un feed reale

# Funzione per inviare messaggi a Telegram
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

# Controllo degli RSS
last_entry = None
while True:
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        latest_entry = feed.entries[0]
        if last_entry is None or latest_entry.link != last_entry:
            message = f"📢 Nuovo articolo: {latest_entry.title}\n{latest_entry.link}"
            send_telegram_message(message)
            last_entry = latest_entry.link
    time.sleep(60)  # Controlla ogni minuto
