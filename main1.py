import telebot

bot = telebot.TeleBot("2140834086:AAEDss6nw-P3Cq7kdo2oaW-KxrfH7VOg9Y4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
	#bot.reply_to(message, message.text)
        #bot.reply_to(message,"rola")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        normalizado=message.text.lower()
        if normalizado.count('histo')>0 :
            #bot.reply_to(message,normalizado.split("=",1)[1])
            #bot.reply_to(message,list1[1]+list1[2]) son strings
            s = normalizado
            s = s[s.find('(')+1:s.rfind(')')]
            d = normalizado
            d = d[d.find('[')+1:s.rfind(']')]
            list1 = s.split(",")
            list3 = d.split(",")
            list2 = [int(i) for i in list1]
            bot.reply_to(message,list2[2]+list2[1])
            bot.reply_to(message,list3[2]+list3[1])
        else:
            bot.reply_to(message,"rola")
bot.infinity_polling()
