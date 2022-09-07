# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:53:35 2022

@author: infolab
"""

def buscar_u_elemento(arr,e):
    '''
        Devuelve el indice de e en una lista(array), 
    '''
    for index, currentNumber in enumerate(arr):
        if currentNumber == e:
            return index
    return -1


def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía
    '''
    if (len(lista) > 0):
        # m guarda el máximo de los elementos a medida que recorro la lista. 
        m = -9999999999999 # Lo inicializo en 0
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e > m:
                m = e
        return m
    raise Exception(f"Perdón, la lista no puede ser vacía! -> {lista}")
    
def minimo(lista):
    '''Devuelve el mínima de una lista, 
    '''
    if (len(lista) > 0):
        # m guarda el mínimo de los elementos a medida que recorro la lista. 
        m = 9999999999999999 # Lo inicializo en 0
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e < m:
                m = e
        return m    
    raise Exception(f"Perdón, la lista no puede ser vacía! -> {lista}")

print(buscar_u_elemento([ -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, 0],-1))
print(maximo([-5,10,7,3,9,34]))
print(minimo([-5,10000]))

