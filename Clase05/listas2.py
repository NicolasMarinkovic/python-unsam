# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:34:21 2022

@author: nicol
"""

import csv
# Primero, leamos el encabezado (header) del archivo CSV:
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

# Definamos una lista que tenga las columnas que nos importan:
select = ['nombre', 'cajones', 'precio']

# Ubiquemos los índices de esas columnas en el CSV:
indices = [headers.index(ncolumna) for ncolumna in select]

# Leamos los datos y armemos un diccionario usando comprensión de diccionarios:

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]









