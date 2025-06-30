import telebot
from telebot import types

# Токен бота
TOKEN = '8042972723:AAF0xgS5ln1dyKQyQ2BrVLWpAcjGjBOZUWI'
bot = telebot.TeleBot(TOKEN)

# Удаляем активный webhook, чтобы не было конфликта
bot.remove_webhook()

# Telegram ID оператора (твой)
operator_id = 1015179786

# Стартовое сообщение с кнопкой
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍 Подобрать запчасть")
    markup.add(item1)

    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋\n\nОтправьте, пожалуйста, VIN-номер или артикул детали.",
        reply_markup=markup
    )

# Обработка кнопок и текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_text = message.text
    username = message.from_user.username or "Без username"

    if user_text == "🔍 Подобрать запчасть":
        bot.send_message(chat_id, "Пожалуйста, пришлите VIN-номер автомобиля или артикул детали:")
    else:
        # Ответ пользователю
        response = (
            f"Спасибо, Вы отправили: {user_text}\n\n"
            "Ваш запрос принят. В ближайшее время мы подберём подходящие запчасти и свяжемся с Вами."
        )
        bot.send_message(chat_id, response)

        # Уведомление оператору
        operator_message = (
            f"📩 Новый запрос от пользователя @{username}:\n\n"
            f"{user_text}\n\n"
            f"`chat_id: {chat_id}`"
        )
        bot.send_message(operator_id, operator_message, parse_mode="Markdown")

# Запуск бота
bot.infinity_polling()
