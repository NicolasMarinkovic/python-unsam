# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:05:46 2022

@author: Nicolas
"""
import csv
import sys
from collections import Counter
from pprint import pprint

#%%
# Esta funcion toma un archivo y un parque y devuelve toda la informacion de las lineas del parque
def leer_parque(nombre_archivo, parque):
    lista_parque = []
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for n_fila, row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            if (record['espacio_ve'] == parque):
                lista_parque.append(record)
    if (lista_parque == []):
        raise RuntimeError(f'Parque no encontrado: {parque}')
    return lista_parque

#%%
# Devuelve las especies del parque antes filtrado
def especies(lista_arboles):
    nombre_com = []
    for x in lista_arboles:
        nombre_com.append(x['nombre_com'])
    unicas_especies = set(nombre_com)
    return unicas_especies

#%%
# Devuelve las especies mas comunes y su cantidad de ejemplares del parque antes filtrado
def contar_ejemplares(lista_arboles):
    tenencias = Counter()
    for s in lista_arboles:
        tenencias[s['nombre_com']] += 1
    print('-------------------\nResultado de las 5 mayores cantidades de ejemplares:')
    for x in tenencias.most_common(5):
        print(f'{x[0]}: {x[1]}')
    print('-------------------')
    return tenencias.most_common(5)[0][0]

#%%
# Devuelve las alturas de una especie dada
def obtener_alturas(lista_arboles, especie):
    contenido = []
    for x in lista_arboles:
        if (x['nombre_com'] == especie ):
            contenido.append(float((x['altura_tot'])))

    print(f'Altura máxima de la especie {especie}: {max(contenido):.2f}\nAltura promedio de la especie {especie}: {(sum(contenido)/len(contenido)):.2f}')

#%%
# Devuelve la inclinacion de una especie dada
def obtener_inclinaciones(lista_arboles, especie):
    contenido = []
    for x in lista_arboles:
        if (x['nombre_com'] == especie ):
            contenido.append(int((x['inclinacio'])))
    incli_unicas = set(contenido)
    return incli_unicas

#%%
# Calcula el especimen mas inclinado de un parque previamente filtrado
def especimen_mas_inclinado(lista_arboles):
    contenido = []
    inclinacionXEspecie = {}
    unicas_especies = especies(lista_arboles)
    
    for especie in unicas_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        inclinacionXEspecie[especie] = max(inclinaciones) # Le agrego el max inclinaciones a un objeto con key del nombre de la especie
        contenido.append(max(inclinaciones))
        
    for nombreEspecie in inclinacionXEspecie:
        if (int(inclinacionXEspecie[nombreEspecie]) == max(contenido)):
            print(f'El ejemplar más inclinado es: {nombreEspecie} con {inclinacionXEspecie[nombreEspecie]}º') #Guarde el nombre de la especia para poder imprimirlo aca
    

#%%
# Calcula el promedio mas inclinado en especie de un parque previamente filtrado
def especie_promedio_mas_inclinada(lista_arboles):
    contenido = []
    inclinacionXEspecie = {}
    unicas_especies = especies(lista_arboles)
    
    for especie in unicas_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        promedioInclinaciones = sum(inclinaciones)/len(inclinaciones)
        inclinacionXEspecie[especie] = promedioInclinaciones
        contenido.append(promedioInclinaciones)
        
    for nombreEspecie in inclinacionXEspecie:
        if (int(inclinacionXEspecie[nombreEspecie]) == max(contenido)):
            print(f'La especie con mayor grado de inclinacion es: {nombreEspecie} con {inclinacionXEspecie[nombreEspecie]}º')

#%%
if(len(sys.argv) >= 2):
   if(len(sys.argv) >= 3):
        for i in range(2,len(sys.argv)):
            sys.argv[1] += ' ' + sys.argv[i] 
   arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', sys.argv[1])
else:
   arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
    
arbolConMayorEspecies = contar_ejemplares(arboles)
obtener_alturas(arboles, arbolConMayorEspecies)
especimen_mas_inclinado(arboles)
especie_promedio_mas_inclinada(arboles)





