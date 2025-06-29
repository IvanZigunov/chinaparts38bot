import telebot
from telebot import types

TOKEN = '8042972723:AAF0xgS5ln1dyKQyQ2BrVLWpAcjGjBOZUWI'
bot = telebot.TeleBot(TOKEN)

# Стартовое сообщение с кнопкой
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍 Подобрать запчасть")
    markup.add(item1)
    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋\n\nОтправьте, пожалуйста, VIN-номер или артикул детали, и мы подберём нужные запчасти.",
        reply_markup=markup
    )

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_text = message.text

    if user_text == "🔍 Подобрать запчасть":
        bot.send_message(
            chat_id,
            "Пожалуйста, пришлите VIN-номер автомобиля или артикул детали:"
        )
    else:
        response = (
            f"Спасибо, Вы отправили: {user_text}\n\n"
            "Ваш запрос принят. В ближайшее время мы подберём подходящие запчасти и свяжемся с Вами."
        )
        bot.send_message(chat_id, response)

        # Отправка сообщения оператору
        operator_id = 1015179786  # Ваш Telegram ID
        bot.send_message(
            operator_id,
            f"📩 Новый запрос от пользователя @{message.from_user.username or 'без username'}:\n\n{user_text}"
        )

bot.infinity_polling()
