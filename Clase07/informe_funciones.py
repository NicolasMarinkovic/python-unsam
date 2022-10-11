# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:30:37 2022

@author: nicol
"""

# Ejercicio 3.1: Lista de tuplas
import csv
#%%
def leer_camion( nombre_archivo : str ) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un encabezado y la segunda los datos.
    Devuelve un diccionario {nombre:fruta, ...}
    '''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for n_fila, row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            try:
                falla = int(record['cajones']) * float(record['precio'])
                camion.append(record)
            except:
                print(f'Fila {n_fila}: No pude interpretar: {row}. Archivo: {nombre_archivo}')
                
    return camion
	
#%%	
def leer_precios( nombre_archivo : str ) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precio = {}

    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    for n_fila, row in enumerate(rows, start=1):
        try:
            precio[row[0]] = float(row[1])
        except:
            print(f'Fila {n_fila}: No pude interpretar: {row}. Archivo: {nombre_archivo}')
    f.close()
    return precio

#%%
def informe_camion(nombre_archivo_camion : str , nombre_archivo_precios : str ):
    '''
    Hace un informe en base a dos archivos csv.
    Estos archivos deben ser de un producto con su precio y su respectiva venta.
    Devuelve un array de tuplas del informe ('Nombre', 'Cajones', 'Precio', 'Diferencia').
    '''
    informe = []
    camiones = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    
    for camion in camiones:
        for key in precios:
            if (key == camion['nombre']):
                diferencia = precios[key] - float(camion['precio'])
                s = (camion['nombre'], int(camion['cajones']),
                     float(camion['precio']), float(diferencia))
                informe.append(s)
    return imprimir_informe(informe)

#%%
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} %2s ${precio:>6.2f} {cambio:>10.2f}' % '')

#%%
files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    informe_camion(name, '../Data/precios.csv')
    print()
