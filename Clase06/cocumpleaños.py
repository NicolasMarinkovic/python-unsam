# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:02:02 2022

@author: nicol
"""
import random

def tirar():
	tirada=[]
	for i in range(30):
		tirada.append(random.randint(1,365))
	return tirada

def cumplenMismoDia():
    tirada = tirar()
    tirada.sort()
    valores = [value for i,value in enumerate(tirada) if i != 0 and value == tirada[i-1]]
    
    if len(valores) > 0:
        return 1
    return 0

N = 10000
G = sum([cumplenMismoDia() for i in range(N)])
prob = G/(N)
print(f'Hice un cálculo de {N} veces, dónde en {G} casos, dos o más personas cumplen años el mismo día.')
print(f'Podemos estimar la probabilidad de que en un grupo de 30 haya dos que cumplan años el mismo día de: {prob*100:.2f} %.')