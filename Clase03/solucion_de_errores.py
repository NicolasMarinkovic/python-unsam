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
#Ejercicio 3.6: Sintaxis
#Comentario: Los errores eran sintácticos.
#    Lo corregí agregando los ":" y cambiando "Falso" por "False".
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
print(tiene_a('La novela 1984 de George Orwell'))
#%%
#Ejercicio 3.7: Tipos
#Comentario: El error era "TypeError: 'int' object is not subscriptable" y estaba ubicado en la llamada a la función.
#    Lo corregí convirtiendo a String el valor ingresado. También podría haber cambiado la llamada pero no esto no aseguraría que la función corra siempre.
#    A continuación va el código corregido
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
#%%
#Ejercicio 3.8: Alcances
#Comentario: El error era semantico y ocurria ya que la funcion no devolvia nada.
#    Lo corregí cambiando "c =" por return.
#    A continuación va el código corregido
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
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
