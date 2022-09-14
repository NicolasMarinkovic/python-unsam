# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:56:41 2022

@author: Nicolas
"""

import random
import numpy as np

#%%
def medir_temp(n):
    lista = [random.normalvariate(0,0.2) + 37.5 for i in range(n)]
    npLista = np.array(lista)
    np.save('../Data/temperaturas', npLista)
    return lista

#%%
def resumen_temp(n):
    lista = medir_temp(n)
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista) / len(lista)
    lista.sort()
    
    indiceMedio = int(len(lista)/2)
    mediana = lista[indiceMedio]
    if len(lista) % 2 == 0: # En el caso de tratarse de una cantidad par de valores, la mediana se obtiene promediando los dos valores centrales
        mediana = (lista[indiceMedio] + lista[indiceMedio +1])/2
    return maximo, minimo, promedio, mediana
    
#%%
encabezados = ('Maximo','Minimo','Promedio','Mediana')
temperatura = zip(encabezados,resumen_temp(999))

for key,value in temperatura:
    print(f'{key}: {value:.4f}')