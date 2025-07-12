
import os
import telegram
from flask import Flask

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def send_message():
    bot.send_message(chat_id=CHAT_ID, text="O Messias e a Mônica são brilhantes!")
    return "Mensagem enviada com sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
