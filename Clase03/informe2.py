# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:27:18 2022

@author: nicol
"""

# Ejercicio 3.1: Lista de tuplas
import csv

def leer_camion(nombre_archivo):
    camion = []
    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        types = [str,int,float]
        for row in rows:
            lote = [ {key: func(value) for key, func, value in zip(encabezado,types,row)}]
            camion.append(lote)
        
    return camion
	
	
def leer_precios(nombre_archivo):
	precio = {}

	f = open('../Data/precios.csv', 'r')
	rows = csv.reader(f)
	for row in rows:
		try:
			precio[row[0]] = float(row[1])
		except:
			pass
	return precio
	f.close()

def balance_total():
    costo_camion = 0.0
    precio_recaudado = 0.0
	
    for camion in camiones:
        camion = camion[0]
        costo_camion += camion['precio'] * camion['cajones']
        for key in precios:
            if (key == camion['nombre']):
                precio_recaudado += precios[key] * camion['cajones']
				
    diferencia = precio_recaudado - costo_camion
    print(f'El costo total del camión es: ${costo_camion}.\nLo que se recaudó con la venta fue: ${precio_recaudado}.')
    if (diferencia > 0):
        print(f'La ganancia es de ${diferencia:.2f}.')
    else:
        print(f'La pérdida es de ${diferencia * -1:.2f}.')

camiones = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
balance_total()

