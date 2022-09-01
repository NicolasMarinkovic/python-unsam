# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:44:02 2022

@author: infolab
"""

#%%
'''
Presentamos ahora uno de los problemas más clásicos de la computación: 
    el problema de la búsqueda. El mismo se puede enunciar de la siguiente manera:

Problema: Dada una lista lista y un elemento e devolver el índice de e en lista 
si e está en lista, y devolver -1 si e no está en lista.
'''
# Se puede usar la funcion index pero si no está en la lista devuelve un error, no -1
[1, 3, 5, 7].index(5)
#2
[1, 3, 5, 7].index(20)
#Traceback (most recent call last):

#  File "<ipython-input-177-1bcce50c5c91>", line 1, in <module>
#    [1, 3, 5, 7].index(20)

#ValueError: 20 is not in list


# Usar e in lista es correcto pero de esta forma hace innecesarias iteraciones
5 in [1, 3, 5, 7]
#True
20 in [1, 3, 5, 7]
#False

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos