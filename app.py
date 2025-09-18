from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Замени на свой токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN', 'ВАШ_ТОКЕН_СЮДА')

@app.route('/getUpdates')
def get_updates():
    offset = request.args.get('offset', '0')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}"
    try:
        resp = requests.get(url, timeout=5)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@app.route('/sendMessage')
def send_message():
    chat_id = request.args.get('chat_id')
    text = request.args.get('text')
    if not chat_id or not text:
        return {"error": "chat_id and text required"}
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    try:
        resp = requests.get(url, timeout=5)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return "Proxy for ESP8266EX Telegram Bot — by @yourname"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
