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

#%% Ejercicio 2.6       FUNCIONES(2.2) 
def costo_camion(nombre_archivo):
    costoTotal = 0
    with open(nombre_archivo, 'rt') as file:
        next(file)
        for line in file:
            row = line.strip("\n").split(',')
            costoTotal += int(row[1]) * float(row[2])
        return costoTotal
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)

#%% Ejercicio 2.7     FUNCIONES(2.3) (buscar_precios.py)
def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    for line in f:
        row = line.strip("\n").split(',')
        if (row[0] == fruta.capitalize()):
            return print(f'El precio de la {fruta} es: ${row[1]}')   
    f.close()
    return print(f'{fruta} no figura en el listado de precios.')
fruta = input('Porfavor ingrese la fruta o verdura que desea consultar:\n--> ')
buscar_precio(fruta)
 
#%% Ejercicio 2.8       ERRORES (costo_camion.py)
def costo_camion(nombre_archivo):
    import csv
    costoTotal = 0
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                costoTotal += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Los datos están en incompletos. Línea: {row}")
    return costoTotal
costo = costo_camion('../Data/missing.csv')
print(f'Costo total: ${costo:.2f}')

#%% Ejercicio 2.9       Funciones de la Biblioteca (csv)
import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)

for row in rows:
        print(row)
f.close()
