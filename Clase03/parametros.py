# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 15:42:46 2022

@author: nicol
"""
import sys
# Sys sirve para pasarle datos como parametros desde la consola
# El primer parámetro(indice 0) es el nombre del script a ejecutar.
# consola: py parametros.py 300

def rebotes(altura):
    i = 0
    while altura >= 0 and i < 10:
        altura = altura * 0.6
        i = i + 1
        print(f'{i} {altura:.2f}')

while (len(sys.argv) < 2):
    try:
        altura = input("Ingresa la altura: \n")
        sys.argv.append(int(altura))
    except:
        print('Debes ingresar un numero entero.')

# Toma el dato del primer argumento
rebotes(int(sys.argv[1]))