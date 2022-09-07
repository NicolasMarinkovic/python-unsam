# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:11:07 2022

@author: infolab
"""

def invertir_lista(lista):
    '''
        Devuelve una lista invertida
    '''
    invertida = []
    for i in range(len(lista)): # Recorro la lista
        lastIndex = (len(lista)-i)-1 # Guardo la posicion del ultimo dato de la lista.
        invertida.append(lista[lastIndex]) # Agrego la posicion del ultimo indice a la lista invertida
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))