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
    #Se limpian la entrada para ser consistente 
    for old, new in replacements.items():
        string = string.replace(old, new)
    
    def func(x):
        return eval(string)

    x=range(-20,20)

    plt.plot(x, [func(i) for i in x])
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.show()

string_plot_func("y = 2*x + 1")