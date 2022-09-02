# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 02:31:13 2022

@author: nicol
"""

# Cambiemos este código
import csv
camion = []
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
    lote = {}
    lote['nombre']=row[0]
    lote['cajones']=int(row[1])
    lote['precio']=float(row[2])
    camion.append(lote)



# --------------
# Hagamos una lista de Python con los nombres de las funciones de conversión que necesitamos para convertir cada columna al tipo apropiado:
types = [str, int, float]
types[1]
#<type 'int'>
row[1]
#'100'

types[1](row[1])     # Es equivalente a int(row[1])
types[1](row[1])*types[2](row[2])
#3220.0000000000005

r = list(zip(types, row))
#[(<type 'str'>, 'Lima'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
#row = "Lima",100,32.20

converted = []
for func, val in zip(types, row):
          converted.append(func(val))
...

#['Lima', 100, 32.2]
converted[1] * converted[2]
#3220.0000000000005

#---------------------

# COMPRENSIÓN DE LISTAS

# El código de arriba puede comprimirse en una sola instrucción.
converted = [func(val) for func, val in zip(types, row)]
#['Lima', 100, 32.2]

# Podés escribir una sola línea usando comprensión de diccionarios:
{ name: func(val) for name, func, val in zip(headers, types, row) }
#{'precio': 32.2, 'name': 'Lima', 'cajones': 100}


