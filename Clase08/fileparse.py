# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:57:05 2022

@author: nicol
"""
# fileparse.py

def parse_csv(rows, select = None, types = None , has_headers= True, silence_errors = False) -> dict:
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    registros = []
    for i, row in enumerate(rows):
        # Lee los encabezados
        if not row:    # Saltea filas sin datos
            continue
        
        try: 
            if has_headers and i==0:
                headers = [x.strip() for x in row.split(',')]
                continue
                
        except UnboundLocalError as e:
            raise RuntimeError('Para seleccionar, necesito encabezados.',e)
            
        if select:
            indices = [headers.index(header) for header in headers]
            headers = select
        
        if select:
            row = [row[index] for index in indices]
            
        try:
            if types:
                row = [func(val) for func, val in zip(types, row.split(','))]
            if has_headers:
                registro = dict(zip(headers, row))
                registros.append(registro)
            else:
                registros.append(tuple(row))     
                
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {i}: No pude convertir {row}')
                print(f'Fila {i}: Motivo: {e}')
                
    return registros

#cajones_retenidos = parse_csv(
#    '/home/datascience/Descargas/Ejercicios/ejercicios_python/Data/camion.csv', 
#    select=['nombre','cajones'],
#    has_headers = False
#    )

cajones_lote = parse_csv(open('../Data/fecha_camion.csv'),types=[str,str,str,int,float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)'
