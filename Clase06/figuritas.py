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

#%% Valores globales que declare aca para cambiarlas una sola vez

figus_total = 670      ## VARIABLE PARA EL TOTAL DE FIGURITAS QUE TENDRA EL ALBUM
n_repeticiones = 1000    ## VARIABLE PARA EL TOTAL DE REPETICIONES DE LA FUNC EXPERIMENTO
cant_p = 850            ## VARIABLE PARA LA CANTIDAD DE FIGURITAS DE LA FUNC EXPERIMENTO

# Ejercicio 6.25: 1200 paquetes

#%% Función que crea el álbum de figuritas

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=int)

#%% Chequea si el álbum está completo, devuelve True si está incompleto

def album_incompleto(A):
    if (np.all(A)):
        return False
    return True
    
    # Ejercicio 6.27:
    '''    
    if (np.all(A > 5)):
        return False
    return True
    '''


#%% Función que simula comprar figuritas

def comprar_paquete(figus_total, cantidad_figus):
    paquete = [ random.randint(0,figus_total-1) for i in range(cantidad_figus)]
    return paquete

#%% Función que compra paquetes hasta llenar el álbum y guarda la cantidad de paquetes en i

def cuantos_paquetes(figus_total):
    album = crear_album(figus_total)
    
    i= 0
    while (album_incompleto(album)):
        paquete = comprar_paquete(figus_total,5)
        for jugador in paquete:
            ''' Ejercicio 6.26:
            while album[jugador] == 1:
                jugador = comprar_paquete(figus_total,1)
            '''
            album[jugador] += 1
        i += 1
        
    return i

#%% Función general que llama a cuantos_paquetes y calcula el promedio

def experimento_figus(N, figus_total, cant_p):
    
    G = np.array([cuantos_paquetes(figus_total) for i in range(N)])
    prob = (G <= cant_p).sum()/N
    print(f'De {N} intentos, en {(G <= cant_p).sum()} pudimos completar el album con menos de {cant_p} paquetes')
    print(f'Podemos estimar la probabilidad de {prob*100:.2f}%.')
    print(f'El promedio de paquetes comprados para completar el álbum es de {G.sum()/N:.2f}')
    
    return G

#%%

def calcular_historia_figus_pegadas(figus_total):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total,5)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
        
    return historia_figus_pegadas

#%% ploteo de la funcion calcular_historia_figus_pegadas
'''
plt.plot(calcular_historia_figus_pegadas(figus_total))

plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
'''
#%% histograma de la funcion experimento_figus
# Ejercicio 6.24:

plt.hist(experimento_figus(n_repeticiones, figus_total, cant_p),bins=25)
plt.xlabel("Cantidad de paquetes comprados hasta llenar el álbum.")
plt.ylabel("Cantidad de veces x Paquete comprados.")
plt.title(f'Histograma de paquetes comprados en {n_repeticiones} intentos')

plt.plot([cant_p,cant_p],[0, 10], color='red', linewidth=2.5, linestyle="--")
plt.scatter(cant_p, 0, color='red')
plt.annotate(f'{cant_p}',
             xy=(cant_p, 0), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()

#%%

