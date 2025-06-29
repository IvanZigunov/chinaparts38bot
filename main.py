import telebot
from flask import Flask, request

API_TOKEN = '8042972723:AAF0xgS5ln1dyKQyQ2BrVLWpAcjGjBOZUWI'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Здравствуйте! Отправьте VIN или артикул, и я подберу автозапчасти.")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, f"Вы ввели: {message.text}. Подбор скоро будет доступен!")

@app.route('/', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://chinaparts38bot.onrender.com/')
    app.run(host='0.0.0.0', port=10000)
