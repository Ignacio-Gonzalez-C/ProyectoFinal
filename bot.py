import telebot
import time
import urllib
#import matplotlib


bot = telebot.TeleBot("2136991575:AAHTOyeac5Id4PPOiK0wy7KX0oQlV6DILt0")
@bot.message_handler(commands=["help"])
def enviar(message):
    bot.reply_to(message, "Sintaxis de ejemplo 'y=2x+5'")


@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.send_chat_action(message.chat.id, 'Hello')

bot.polling()