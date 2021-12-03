#-----------------------------------------------------------
#Librerias
import telebot
import numpy as np
import matplotlib.pyplot as plt
#matplotlib para efectos matematicos.

#Datos iniciales, valores para grafico lineal:
tipo = "line"
X = None
Y = None
x_datos = None
y_datos = None
titulo = ""

#Inicio con comando:
@bot.message_handler(commands=['lineainicio'])
def inicio_linea(message):
	chat_id = message.chat.id

	bot.send_message(chat_id,"Buenas, esta funcionalidad te permitira hacer un gráfico lineal a partir de datos.")
	bot.send_message(chat_id, "Primero se necesitan los valores para los ejes X e Y. "
							  "Usa el formato \"X:\" antes de escribir los datos, los datos debes ser separados con comas, sin espacios, lo mismo para Y. "
							  "\nEl primer valor que coloques será utilizado como nombre del eje."
							  "\nSi deseas un título escribe el comando /linearotulo.")
	bot.send_message(chat_id, "Un ejemplo sería 'X:Personas,4,5,6,7' y 'Y:Repositorios,1,2,3,4' ")									  
	bot.send_message(chat_id, "Recuerda que se forman pares de puntos, por lo que si hay distinto número de datos en X e Y habrá un error.")							  
	bot.send_message(chat_id, "Finalmente y con los datos guardados, escribe /lineaplot para graficar.")

#Valores de X
@bot.message_handler(regexp=(r'x:'))
def valores_x(message):
	chat_id = message.chat.id
	global X
	global x_datos
	try:
		values = np.array(message.text.split(":")[1].split(","))
		X = values[1:]
		x_datos = values[0]
		bot.send_message(chat_id, "¡Guardado!")
	except:
		bot.send_message(chat_id, "Lo siento, hay un error, revise si está bien el formato.")

#Valores de Y
@bot.message_handler(regexp=(r'y:'))
def valores_y(message):
	chat_id = message.chat.id
	global Y
	global y_datos
	try:
		values = np.array(message.text.split(":")[1].split(","))
		Y = np.array(values[1:], dtype = np.float64)
		y_datos = values[0]
		bot.send_message(chat_id, "¡Guardado!")
	except:
		bot.send_message(chat_id, "Lo siento, hay un error, revise si está bien el formato.")

#Titulo		
@bot.message_handler(commands=['linearotulo'])
def pregunta_titulo(message):
	chat_id = message.chat.id
	respuesta = bot.send_message(chat_id, "Escriba el título que desea: ")
	bot.register_next_step_handler(respuesta, agregar_titulo)
#Para el plot
def agregar_titulo(message):
	global titulo
	chat_id = message.chat.id
	titulo = str(message.text)
	bot.send_message(chat_id, "¡Entendido!")

#Plot
@bot.message_handler(commands=['lineaplot'])
def plotteador(message):
	chat_id = message.chat.id
	global X,Y,y_datos,x_datos, tipo,titulo

	print(x_datos);print(X)
	print(y_datos);print(Y)
	print(tipo)

	try:
		if tipo == "line":
			plt.figure(figsize=(8,4.5))
			plt.plot(X, Y, alpha = 0.7, c = "#bf280a")
			plt.scatter(X, Y, alpha=0.7, c="#bf280a")
			plt.ylabel(y_datos)
			plt.xlabel(x_datos)
			plt.title(titulo)
			plt.savefig("grafico.png")
		# plt.ylim(0,np.max(Y))


		bot.send_photo(chat_id, photo=open('grafico.png', 'rb'))
		bot.send_message(chat_id, "Aquí está su gráfico.")
	except:
		bot.send_message(chat_id, "Ha ocurrido un error durante el desarrollo, intente de nuevo.")

bot.polling()
#-----------------------------------------------------------