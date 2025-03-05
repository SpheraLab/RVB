import feedparser
import requests
import time
import os

# Legge le variabili d'ambiente da Railway
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token del bot Telegram
CHAT_ID = os.getenv("CHAT_ID")  # ID della chat Telegram
RSS_FEED_URL = os.getenv("RSS_FEED_URL")  # URL del feed RSS da monitorare

# Controllo degli RSS
last_entry = None

def send_telegram_message(text):
    """Invia un messaggio alla chat Telegram configurata"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

while True:
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        latest_entry = feed.entries[0]
        if last_entry is None or latest_entry.link != last_entry:
            message = f"📢 Nuovo articolo: {latest_entry.title}\n{latest_entry.link}"
            send_telegram_message(message)
            last_entry = latest_entry.link
    time.sleep(60)  # Controlla ogni minuto
