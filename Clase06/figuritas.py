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

#%% Valores globales del total de figus y la cantidad de repeticiones

figus_total = 670
n_repeticiones = 100

#%% Función que crea el álbum de figuritas

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=int)

#%% Chequea si el álbum está completo, devuelve True si está incompleto

def album_incompleto(A):
    if (np.all(A)):
        return False
    return True

#%% Función que simula comprar figuritas

def comprar_paquete(figus_total):
    paquete=[ random.randint(0,figus_total-1) for i in range(5)]
    return paquete

#%% Función que compra paquetes hasta llenar el álbum y guarda la cantidad de paquetes en i

def cuantos_paquetes(figus_total):
    album = crear_album(figus_total)
    
    i= 0
    while (album_incompleto(album)):
        paquete = comprar_paquete(figus_total)
        for jugador in paquete:
            album[jugador] += 1
        i += 1
        
    return i

#%% Función general que llama a cuantos_paquetes y calcula el promedio

def experimento_figus(N, figus_total):
    G = sum([cuantos_paquetes(figus_total) for i in range(N)])
    prob = G/N
    print(f'Podemos estimar la probabilidad de completar un album comprando {prob:.2f} sobres.')

experimento_figus(n_repeticiones , figus_total)
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

plt.plot(calcular_historia_figus_pegadas(figus_total))

plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()



#%%