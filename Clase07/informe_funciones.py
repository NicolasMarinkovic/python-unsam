# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:30:37 2022

@author: nicol
"""

# Ejercicio 3.1: Lista de tuplas
import csv
from fileparse import parse_csv
#%%
def leer_camion( nombre_archivo : str, select = None, types = None , has_headers= True ) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un encabezado y la segunda los datos.
    Devuelve un diccionario {nombre:fruta, ...}
    '''
    camion = []
    try:
        camion = parse_csv(nombre_archivo,select = select, types= types,has_headers = has_headers)
    except:
        print(f' No pude interpretar: . Archivo: {nombre_archivo}')       
    return camion
	
#%%	
def leer_precios( nombre_archivo : str, select = None, types = None , has_headers= True ) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precio = []

    try:
        precio = parse_csv(nombre_archivo,select = select, types= types,has_headers = has_headers)
    except:
        print(f'No pude interpretar Archivo: {nombre_archivo}')
    return dict(precio)

#%%

def informe_camion(nombre_archivo_camion : str , nombre_archivo_precios : str ) -> dict:
    '''
    Hace un informe en base a dos archivos csv.
    Estos archivos deben ser de un producto con su precio y su respectiva venta.
    Devuelve un array de tuplas del informe ('Nombre', 'Cajones', 'Precio', 'Diferencia').
    ''' 
    informe = []
    camiones = leer_camion(nombre_archivo_camion,types = [str,int,float])
    precios = leer_precios(nombre_archivo_precios ,types = [str,float], has_headers = False)
    
    for camion in camiones:
        for key in precios:
            if (key == camion['nombre']):
                diferencia = precios[key] - camion['precio']
                s = (camion['nombre'], camion['cajones'],
                     camion['precio'], diferencia)
                informe.append(s)
                
    imprimir_informe(informe)
    
    return informe

#%%
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} %2s ${precio:>6.2f} {cambio:>10.2f}' % '')

#%%
'''
files = ['../Data/camion.csv', '../Data/camion2.csv']

for name in files:
    print(f'{name:-^43s}')
    informe_camion(name, '../Data/precios.csv')
    print()

'''
    
