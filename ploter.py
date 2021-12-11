import matplotlib.pyplot as plt
import numpy as np

replacements = {
    ' ' : '',
    'y' : '',
    '=' : '',
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**'
}

def string_plot_func(string):
    original_name = string
    #Se limpian la entrada para ser consistente 
    for old, new in replacements.items():
        string = string.replace(old, new)
    
    def func(x):
        return eval(string)

    x= np.arange(-10, 10, 0.1)

    plt.plot(x, [func(i) for i in x])
    plt.title(original_name)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.savefig('plot.png', bbox_incehs='thigth')
    plt.close()
    print("Gráfico creado")

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
    plt.close()
    print("torta creada")
