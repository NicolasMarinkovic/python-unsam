# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:53:35 2022

@author: infolab
"""

def donde_insertar(lista, x, verbose = False):
    '''Utiliza Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve el índice dónde se debe colocar x;
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2 ## Usamos doble // para que devuelva el entero
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            
    if pos == -1:   # Si no encontro el valor
        if lista[medio] < x:  # Modifica si el indice va en el anterior o en el siguiente
            return medio + 1
        return medio
    return pos

print(donde_insertar([0,2,4,6,8], 11, verbose=True))