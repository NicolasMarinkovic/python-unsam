# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:20:38 2022
#solucion_de_errores.py
#Ejercicios de errores en el código
@author: Nicolas
"""
#%%
#Ejercicio 3.5: Semántica
#Comentario: El error era semántico y estaba ubicado la línea 19(solo tomaba la primera letra y devolvia true or false).
#    Lo corregí cambiando el return false, poniendolo fuera del ciclo while.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.9: Pisando memoria
#Comentario: El error era semantico y se debía a que estaba mal donde iniciaba el diccionario registro.
#    Lo corregí inicianizandolo dentro del for asi se reiniciaba cada vez que se ejecuta.
#    Creo que el error se debia ya que cada vez que se ejecutaba el ciclo modificaba las posiciones de memoria de los anteriores registrs y por eso modificaba todos juntos.
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
