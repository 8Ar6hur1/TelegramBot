import telebot
from telebot import types

TOKEN = telebot.TeleBot('7478465201:AAHmj3KuKW7IXonkz6s-eSRRHHFPYyBmDv8')

# Кнопки під текстом вводу
@TOKEN.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton('Перейти на сайт')
    btn2 = types.KeyboardButton('Видалити фото')
    btn3 = types.KeyboardButton('Змінити текст')
    markup.row(btn1)
    markup.row(btn2, btn3)
    TOKEN.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}!', reply_markup=markup)

# Кнопки під фото
@TOKEN.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://youtube.com')
    btn2 = types.InlineKeyboardButton('Видалити фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('...', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    TOKEN.reply_to(message, 'Яке чудове фото!', reply_markup=markup)

@TOKEN.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        TOKEN.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        TOKEN.edit_message_text('Змінити текст', callback.message.chat.id, callback.message.message_id)


TOKEN.polling(non_stop=True)