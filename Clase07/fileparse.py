# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:57:05 2022

@author: nicol
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo : str, select = None, types = None , has_headers= True) -> dict:
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        if has_headers:
            headers = next(rows)
        
        if select:
            indices = [headers.index(header) for header in headers]
            headers = select
        
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            
            if select:
                row = [row[index] for index in indices]
            
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            
            if has_headers:
                registro = dict(zip(headers, row))
                registros.append(registro)
            else:
                registros.append(tuple(row))

    return registros

cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])
cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
