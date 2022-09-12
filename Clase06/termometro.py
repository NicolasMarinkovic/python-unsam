# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:56:41 2022

@author: Nicolas
"""

import random

#%%
def medir_temp(n):
    lista = [random.normalvariate(0,0.2) for i in range(n)]
    return lista

#%%
def resumen_temp(n):
    lista = medir_temp(n)
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista)
    lista.sort()
    
    mediana = lista[int(len(lista)/2)]
    if len(lista) % 2 == 0:
        mediana = (lista[int(len(lista)/2)] + lista[int(len(lista)/2) +1])/2
    return maximo, minimo, promedio, mediana
    
#%%
encabezados = ('Maximo','Minimo','Promedio','Mediana')
temperatura = zip(encabezados,resumen_temp(10))

for key,value in temperatura:
    print(f'{key}: {value:.4f}')