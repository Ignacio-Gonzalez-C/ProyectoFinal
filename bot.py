import telebot
import time
import urllib
from ploter import *
import matplotlib

help_message = "FUNCIONES:\n \
    1-Visualización de funciones simples:\n \
    Sintaxis de ejemplo 'y= 2*x+5'\nPuntos a seguir:\n \
    \r•Las funciones soportadas son seno (sin), coseno(cos), raiz cuadrada(sqrt) y exponencial(exp)\n \
    \r•Cualquier función no soportada no mostrará el gráfico\n \
    2-Gráfico de torta: \n \
    •Para utilizar ploteo de torta la sintaxis es la siguiente:\ntortaplot(dato1 dato2 daton)"

bot = telebot.TeleBot("token")
@bot.message_handler(commands=["help","start"])
def enviar(message):
    bot.reply_to(message, help_message)

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    normalizado=message.text.lower()
    if normalizado.count('tortaplot')>0:
        normalizado=normalizado.replace('tortaplot','')
        normalizado=normalizado.replace('(','')
        normalizado=normalizado.replace(')','')
        listado = list(normalizado.split(" "))
        createtorta(listado)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('torta.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()
    else:
        string_plot_func(normalizado)
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('plot.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

bot.polling()
