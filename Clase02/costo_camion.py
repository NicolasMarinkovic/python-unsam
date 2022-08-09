# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:09:09 2022

@author: nicol
"""
#%% Ejercicio 2.2
costoTotal = 0
with open('../Data/camion.csv', 'rt') as file:
    headers = next(file)
    for line in file:
        row = line.strip("\n").split(',')
        costoTotal += int(row[1]) * float(row[2])
    print('Costo total:', costoTotal)
    
#%% Ejercicio 2.3
f = open('../Data/precios.csv', 'rt')
headers = next(f)
for line in f:
    row = line.strip("\n").split(',')
    if (row[0] == 'Naranja'):
        print('El precio de la naranja es:', row[1])
f.close()

#%% Ejercicio 2.4
import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
