import telebot from telebot import types

API_TOKEN = '8042972723:AAF0xgS5ln1dyKQyQ2BrVLWpAcjGjBOZUWI' ADMIN_ID = 1015179786

bot = telebot.TeleBot(API_TOKEN)

Показывать кнопки при любом новом сообщении в начале

@bot.message_handler(func=lambda message: True, content_types=['text']) def handle_all_messages(message): markup = types.ReplyKeyboardMarkup(resize_keyboard=True) item1 = types.KeyboardButton("🛠 Подбор запчасти") markup.add(item1)

if message.text == "🛠 Подбор запчасти":
    bot.send_message(message.chat.id, "Пожалуйста, отправьте VIN или артикул детали.", reply_markup=markup)
else:
    bot.send_message(message.chat.id, "Ваш запрос отправлен. Ожидайте ответа оператора.", reply_markup=markup)
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

Ответ оператора по ID пользователя

@bot.message_handler(commands=['ответ']) def reply_to_user(message): try: parts = message.text.split(maxsplit=2) user_id = int(parts[1]) reply_text = parts[2] bot.send_message(user_id, f"Ответ от оператора:\n{reply_text}") bot.reply_to(message, "Сообщение отправлено.") except: bot.reply_to(message, "Формат команды: /ответ <user_id> <сообщение>")

bot.polling(none_stop=True)

