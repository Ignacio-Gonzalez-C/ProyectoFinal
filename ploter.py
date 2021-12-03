import matplotlib.pyplot as plt


def limpiar(lista):
    limpio=[]
    for item in lista:
        if item not in limpio:
            limpio.append(item)
    return limpio

def cantlista(acontar,crudo):
    cantidades=[]
    for i in range(0,len(acontar)):
        cantidades.append(crudo.count(acontar[i]))
    return cantidades

def listastrlistaint(lista):
    for i in range(0, len(lista)):
        lista[i] = int(lista[i])
    return lista


def createtorta(listado):
    labels=limpiar(listado)
    sizes=cantlista(labels,listado)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('torta.png', bbox_inches='tight')
    print("torta creada")
