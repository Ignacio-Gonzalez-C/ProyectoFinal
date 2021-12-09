import telebot
import matplotlib
from ploter import createtorta


bot = telebot.TeleBot("token")
@bot.message_handler(commands=["help","start"])
def enviar(message):
    bot.reply_to(message, "para utilizar ploteo de torta la sintaxis es la siguiente:\ntortaplot(dato1 dato2 daton)")


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

            
        


bot.polling()
