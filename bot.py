import telebot
import time
import urllib
from ploter import *

help_message = "Sintaxis de ejemplo 'y= 2*x+5'\nPuntos a seguir:\n \
    \r•Las funciones soportadas son seno (sin), coseno(cos), raiz cuadrada(sqrt) y exponencial(exp)\n \
    \r•Cualquier función no soportada no mostrará el gráfico"

bot = telebot.TeleBot("2136991575:AAHTOyeac5Id4PPOiK0wy7KX0oQlV6DILt0")
@bot.message_handler(commands=["help"])
def enviar(message):
    bot.reply_to(message, help_message)


@bot.message_handler(func=lambda message:True)
def mensaje(message):
    new_message=message.text.lower()
    string_plot_func(new_message)
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open('plot.png', 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    img.close()

bot.polling()