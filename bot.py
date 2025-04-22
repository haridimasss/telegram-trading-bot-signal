import os
import telegram
from flask import Flask, request

app = Flask(__name__)
bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])

@app.route('/send', methods=['POST'])
def send_signal():
    data = request.json
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    message = data.get("message", "No message provided.")
    
    bot.send_message(chat_id=chat_id, text=message)
    return "Signal sent", 200

if __name__ == '__main__':
    app.run(debug=True)