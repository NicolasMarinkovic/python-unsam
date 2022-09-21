# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:59:40 2022

@author: nicol
"""

'''
Creado por: Nicolás Marinkovic
La idea es calcular cuánto se gasta en llenar un álbum de figuritas
'''

#%%

import numpy as np
import random
from matplotlib import pyplot as plt

#%% El primer valor es el total de figus y el segundo es la cantidad por equipo.
# El primer valor es igual a ( cantidadEquipos * cantidadFigusXEquipo )
cantidad_figuritas = (670,1) # Lo hice en forma de filas y columnas porque me parecia mas real pensarlo separando por 'equipos'
n_repeticiones = 100

#%% Función que crea el álbum de figuritas

def crear_album(figus_total):
    cantidadEquipos = int(figus_total[0]/figus_total[1])
    return np.zeros(figus_total[0], dtype=int).reshape(cantidadEquipos ,figus_total[1])

#%% Chequea si el álbum está completo, devuelve True si está incompleto

def album_incompleto(A):
    if (np.all(A)):
        return False
    return True

#%% Función que simula comprar figuritas

def comprar_paquete(figus_total):
    cantidadEquipos = (figus_total[0]/figus_total[1])
    paquete=[]
    for i in range(5):
        paquete.append( (random.randint(0,cantidadEquipos-1) , #Random Equipo
                         random.randint(0,figus_total[1]-1)    #Random Jugador
                       ) ) 
    return paquete

#%% Función que compra paquetes hasta llenar el álbum y guarda la cantidad de paquetes en i

def cuantos_paquetes(figus_total):
    album = crear_album(figus_total)
    
    i= 0
    while (album_incompleto(album)):
        paquete = comprar_paquete(figus_total)
        for equipo, jugador in paquete:
            album[equipo][jugador] += 1
        i += 1
        
    return i

#%% Función general que llama a cuantos_paquetes y calcula el promedio

def experimento_figus(N, figus_total):
    G = sum([cuantos_paquetes(figus_total) for i in range(N)])
    prob = G/N
    print(f'Podemos estimar la probabilidad de completar un album comprando {prob:.2f} sobres.')

experimento_figus(n_repeticiones , cantidad_figuritas)
#%%

def calcular_historia_figus_pegadas(figus_total):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)   
        
    return historia_figus_pegadas

plt.plot(calcular_historia_figus_pegadas(cantidad_figuritas))

plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()



#%%