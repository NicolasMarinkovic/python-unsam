# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:56:09 2022

@author: infolab
"""
#%%
import tqdm
## tqdm esta muy bueno buscalo
for i in tqdm(range(10000)):
    a = 0
#76%|████████████████████████████         | 7568/10000 [00:33<00:10, 229.00it/s]
#trange(N) can be also used as a convenient shortcut for tqdm(xrange(N)).


#%%
import csv
# NOTAS SOBRE EL TIPO DE DATOS
#También podés agregar, en la definición de funciones, notas sobre el tipo de datos de los parámetros y de la función.

def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
'''
Estas notas no modifican al programa y son puramente informativas. Aún así pueden ser usadas por IDEs, comprobadores de código, y otras herramientas.
Aunque -> dict indica al programador que la función devuelve un diccionario, es útil anotar en el doc-string la estructura del diccionario devuelto.
'''
#%%
#   LLAMANDO A UNA FUNCIÓN
#Imaginá la siguiente función:

def leer_precios(nombre_archivo, debug):
    a = 0
#Podés llamar a la función pasando los argumentos por orden:
precios = leer_precios('precios.csv', True)
#O podés llamarla usando palabras clave (keywords):
precios = leer_precios(nombre_archivo = 'precios.csv', debug = True)
#%%
#ARGUMENTOS POR OMISIÓN
'''
Si preferís que un argumento sea opcional (que tenga un valor por omisión o by default), en ese caso asignale un valor en la definición de la función. Ése será el valor del argumento si llamás a la función sin especificar un valor para ese argumento.
'''
def leer_precios(nombre_archivo, debug = False):
    a = 0
    
d = leer_precios('precios.csv')
e = leer_precios('precios.dat', True)
#%%
# DEVOLVER MÚLTIPLES RESULTADOS
'''
Las funciones sólo pueden devolver una cosa. Si necesitás devolver más de un valor, podés armar una tupla con ellos y devolver la tupla.
'''

def dividir(a,b):
    c = a // b      # Cociente
    r = a % b       # Resto
    return c, r     # Devolver una tupla con c y r

x, y = dividir(37,5) # x = 7, y = 2
x = dividir(37, 5)   # x = (7, 2)

#%%
# MODIFICAR EL VALOR DE UNA VARIABLE GLOBAL
'''
Si necesitás modificar el valor de una variable global desde dentro de una función, la variable tiene que estar declarada como global dentro de la misma función.

'''
nombre = 'Dave'

def spam():
    global nombre
    nombre = 'Guido' # Cambia el valor de la variable global



