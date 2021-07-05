import matplotlib.pyplot as plt
import numpy as np
#matplotlib es para grafica, numpy vectoriza python

def graf(x,y,z):
    #necesario para exportar grafica
    fig=plt.figure()

    fig.add_subplot(1,1,1)
    #graficador + etiquetas
    plt.plot(x,y,'b.',label=r'$y_1$')
    plt.xlabel('x')
    plt.ylabel(r'$y=x^2$') #se pone r para formato "raw" y los $ encierran el texto para armarlo mas legible

    plt.title('f(x)')
    plt.legend(loc=1)
    plt.grid(True)

    plt.xticks(np.linspace(-3,3,14)) #(punto inicial, punto final, cantidad de separaciones entre a y b)
    #si se quiere separar pero en y se escribe: plt.yticks

    #linea horizontal o vertical
    plt.axhline(4,color='r',lw=2)
    #si se quiere la linea recta vertical es: plt.axvline. Horizontal: plt.axhline

    #*******************************SEPARACION GRAFICAS 1 Y 2 ********************************************

    fig.add_subplot(2,1,1) #para hacer dos graficas en una foto
    #graficador + etiquetas
    plt.plot(z,y,'b.',label=r'$y_1$')
    plt.xlabel('z')
    plt.ylabel(r'$y=x^2$') #se pone r para formato "raw" y los $ encierran el texto para armarlo mas legible

    plt.title('f(z)')
    plt.legend(loc=1)
    plt.grid(True)

    plt.xticks(np.linspace(-3,3,14)) #(punto inicial, punto final, cantidad de separaciones entre a y b)
    #si se quiere separar pero en y se escribe: plt.yticks

    #linea horizontal o vertical
    plt.axhline(4,color='g',lw=2)
    #si se quiere la linea recta vertical es: plt.axvline. Horizontal: plt.axhline


    plt.show()
    #exportador de grafica
    fig.savefig('grafica.png')

x=[1,-1,2,-2,3,-3,4,-4,5,-5]
y=[-5,-4,-3,-2,-1,0,1,2,3,4]
z=[10,-10,12,-12,13,-13,14,-14,15,-15]
graf(x,y,z)