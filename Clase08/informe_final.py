# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:30:37 2022

@author: nicol
"""

# Ejercicio 3.1: Lista de tuplas
from fileparse import parse_csv
#%%
def leer_camion( nombre_archivo : str, select = None, types = None , has_headers= True , silence_errors = False) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un encabezado y la segunda los datos.
    Devuelve un diccionario {nombre:fruta, ...}
    '''
    camion = []
    
    camion = parse_csv(nombre_archivo,select = select, types= types,has_headers = has_headers, silence_errors = silence_errors)
    
    return camion
	
#%%	
def leer_precios( nombre_archivo : str, select = None, types = None , has_headers= True , silence_errors = False) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precio = []
    
    precio = parse_csv(nombre_archivo,select = select, types= types,has_headers = has_headers, silence_errors = silence_errors)

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
def f_principal(params):
    if len(params) < 3:
        params.append(open('../Data/precios.csv'))
    
    informe_camion(params[1], params[2])
    print()

#%%
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        camion = open(sys.argv[1])
        precios = open(sys.argv[2])
        f_principal([sys.argv[0],camion,precios])
    else:
        f_principal([sys.argv[0],open('../Data/camion.csv'),open('../Data/precios.csv')])
        #raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    




    
