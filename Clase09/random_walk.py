# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:30:39 2022

@author: Nicolas
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo)    
    return pasos.cumsum()
    

def graficar():
    mayor = -9999
    menor = 9999
    
    plt.subplot(2,1,1)
    for i in range(12):
        
        p = randomwalk(N)
        a = plt.plot(p)
        
        if (max(abs(p)) > mayor):
            mayor = max(abs(p))
            listaMayor = np.copy(p)
            colorMayor = a[0].get_color()
            
        if (abs(p.mean()) < menor):
            menor = abs(p.mean())
            listaMenor = np.copy(p)
            colorMenor = a[0].get_color()
        
        plt.title("12 Caminatas al Azar")
        plt.xlabel("tiempo (s)")
        plt.ylabel("Distancia al origen (km)")
        plt.xticks([]), plt.yticks([-500,0,500]) 
        plt.ylim(-650, 650)

    
    plt.subplot(2,2,3)
    plt.plot(listaMayor, color= colorMayor)
    plt.title("La caminata que más se aleja en su punto máximo")
    plt.xticks([]), plt.yticks([-500,0,500]) 
    plt.ylim(-650, 650)
    
    
    plt.subplot(2,2,4)
    plt.plot(listaMenor, color= colorMenor)
    plt.title("La caminata que menos se aleja(en promedio)")
    plt.plot([0, 100000],[0, 0], color='black', linewidth=2.5, linestyle="--")
    plt.scatter([0,100000],[0,0],50, color='black')
    plt.xticks([]), plt.yticks([0]) 
    plt.ylim(-650, 650)
    
    plt.show()


N = 100000
fig = plt.figure()
graficar()




