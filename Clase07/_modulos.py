# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:02:56 2022

@author: Nicolas
"""

#Namespaces
'''
Se puede decir que un módulo es una colección de valores asignados a nombres. 
A ésto se lo llama un namespace (espacio de nombres). Es el contexto en el cual 
esos nombres existen: todas las variables globales y las funciones definidas en 
un módulo pertenecen a ese módulo. Una vez importado, el nombre del módulo se usa 
como un prefijo al nombrar esas variables y funciones. Por eso se llama un namespace.
'''
import foo

a = foo.grok(2)
b = foo.spam('Hello')

# FROM MÓDULO IMPORT NOMBRE
# Este comando toma ciertos nombres selectos de un módulo, y los hace accesibles localmente.

import math
# vs
import math as m   # sólo cambia el nombre local del módulo
# vs
from math import cos, sin
# vs
from math import * 

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y


import fileparse # Es un archivo mio de la clase 7
help(fileparse)
# mirá la salida ...
dir(fileparse)
# mirá la salida ...
camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
# Importá sólo la función para evitar escribir el nombre del módulo:
from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])