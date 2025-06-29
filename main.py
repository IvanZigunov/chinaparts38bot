import telebot
import time
import logging

# Вставьте ваш токен сюда
TOKEN = "7557048741:AAGVb-34QQR05wE861WdF4fSivuFahYqa0U"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Пожалуйста, отправьте VIN или артикул для подбора запчастей.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Извините, автоматический подбор пока в разработке. Мы скоро всё подключим.")

if __name__ == "__main__":
    while True:
        try:
            print("Бот запущен.")
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            print("Пробуем перезапустить через 10 секунд...")
            time.sleep(10)
