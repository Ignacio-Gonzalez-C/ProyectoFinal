import telebot
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import os
bot = telebot.TeleBot("2140834086:AAEDss6nw-P3Cq7kdo2oaW-KxrfH7VOg9Y4")

@bot.message_handler(commands=["help"])
def enviar(message):
    bot.reply_to(message, "para hacer un histograma la sintaxis es la siguiente:histo=(dato1 dato2 dato3){bins}")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        normalizado=message.text.lower()
        if normalizado.count('histo')>0 :
            s = normalizado
            s = s[s.find('(')+1:s.rfind(')')]
            nbins = normalizado
            nbins = nbins[nbins.find('{')+1:s.rfind('}')]
            nbins = int(nbins)
            list1 = s.split(",")
            list2 = [int(i) for i in list1]
            plt.hist(list1, nbins, facecolor='blue', alpha=0.5, ec='black')
            plt.savefig('histo.png')
            bot.send_chat_action(message.chat.id, 'upload_photo')
            img = open('histo.png', 'rb')
            bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
            img.close()
            os.remove("histo.png")
            plt.clf()
        else:
            bot.reply_to(message,"rola")
bot.infinity_polling()
