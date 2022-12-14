# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:22:09 2022

@author: nicol
"""
import csv
import sys

def costo_camion(nombre_archivo):
    costoTotal = 0
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        try:
            costoTotal = sum(int(row[1]) * float(row[2]) for i,row in enumerate(rows))
        except ValueError:
            print("Los datos están incompletos.")
    return costoTotal

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    # Si no le pasas un archivo como parametro toma el camion.csv
    # py .\camion_commandline.py ../Data/missing.csv

costo = costo_camion(nombre_archivo)
print('Costo total: $', costo)