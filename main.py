import telebot

bot = telebot.TeleBot('7478465201:AAHmj3KuKW7IXonkz6s-eSRRHHFPYyBmDv8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}')

bot.polling(non_stop=True)