import telebot
from telebot import types

TOKEN = '8042972723:AAF0xgS5ln1dyKQyQ2BrVLWpAcjGjBOZUWI'
bot = telebot.TeleBot(TOKEN)

# ID оператора
operator_id = 1015179786

# Обработка всех текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_message(message):
    chat_id = message.chat.id
    user_text = message.text.strip()

    # Создание клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍 Подобрать запчасть")
    markup.add(item1)

    if user_text == "🔍 Подобрать запчасть":
        bot.send_message(chat_id, "Пожалуйста, пришлите VIN-номер или артикул детали.", reply_markup=markup)
    else:
        response = (
            f"Спасибо, Вы отправили: {user_text}\n\n"
            "Ваш запрос принят. В ближайшее время мы подберём подходящие запчасти и свяжемся с Вами."
        )
        bot.send_message(chat_id, response)

        # Уведомление оператору
        bot.send_message(
            operator_id,
            f"📩 Новый запрос от пользователя @{message.from_user.username or 'без username'}:\n\n{user_text}"
        )

    # Показываем кнопку при любом сообщении
    if not message.text.startswith("🔍"):
        bot.send_message(chat_id, "Нажмите кнопку ниже для подбора запчастей 👇", reply_markup=markup)

# Запуск бота
bot.infinity_polling()
