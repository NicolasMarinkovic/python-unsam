# -*- coding: utf-8 
"""
Created on Sun Sep 11 12:43:16 2022

@author: nicol
"""

import random
from collections import Counter

#%%
# Función que devuelve la mano, o sea 3 cartas
def mano():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(palo,valor) for valor in valores for palo in palos]

    return random.sample(naipes,k=3)

#%%
# Función que calcula el envido
def calculoEnvido(valores):
    envido = 0
    sumaCero = [10,11,12]
    
    if len(valores) == 1: # Si viene 1 solo valor significa que no habia dos cartas del mismo palo
        return 0
    
    for valor in valores:
        if valor in sumaCero: # Si se un [10,11,12], borro el valor y agrego un 0
            valores.pop(valores.index(valor)) 
            valores.insert(-1,0)
            
    # Le sumo al envido los dos máximos valores(lo hice asi en caso que haya flor)
    for i in range(2):
        envido += valores.pop(valores.index(max(valores))) 
    
    # Después sumo los 20 que corresponden del envido
    envido += 20
    
    return envido
        
#%%
# Función que separa las cartas del mismo palo y calcula el envido con las que son del mismo palo
def envido():
    manoActual = mano()
    palos = []
    valores = []
    
    palos = [palo for palo, valor in manoActual]
    
    conteo=Counter(palos)
    paloMaximo = [key for key in conteo if conteo[key] == max(conteo.values())]
    
    valores = [valor for palo, valor in manoActual if palo == paloMaximo[0]]
    
    return calculoEnvido(valores)

#%%    
N = 10
G = 0
for i in range(N):
    value = envido()
    if value in [31,32,33]:
        G += 1
        
prob = G/(N)

print(f'Hice un cálculo de {N} veces, dónde en {G} casos, tuve más de 31 de envido.')
print(f'Podemos estimar la probabilidad de que toque más de 31 de envido como: {prob*100:.2f} %.')
