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
