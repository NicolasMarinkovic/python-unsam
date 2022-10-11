# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:57:05 2022

@author: nicol
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv')

