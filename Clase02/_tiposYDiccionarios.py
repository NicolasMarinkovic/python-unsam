# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:21:02 2022

@author: Nicolas
"""

#TIPOS Y ESTRUCTURAS DE DATOS
#Tipos de datos primitivos

#Int
#Float
#String

#Tipo None
email_address = None
#None suele utilizarse como un comodín para reservar el lugar para un valor opcional o faltante. En los condicionales, evalúa como False.


# Diccionarios
#Los diccionarios son útiles cuando hay muchos valores diferentes y esos valores pueden 
#ser modificados o manipulados. Dado que el acceso a los elementos se hace por clave, 
#no es necesario recordar una posición para cierto dato, lo que muchas veces cumple
#un objetivo fundamental: hacer que el código sea más legible (y con esto menos propenso a errores).
#Un diccionario es una función que manda claves en valores. Las claves sirven como índices para acceder a los valores.

s = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}

# Operaciones usuales
# Para obtener el valor almacenado en un diccionario usamos las claves.
print(s['fruta'], s['cajones'])         #Manzanas 100

#Para agregar o modificar valores, simplemente asignamos usando la clave.
s['cajones'] = 75
s['fecha'] = '6/8/2020'

#para borrar un valor, usamos el comando del.
del s['fecha']

# Una manera más elegante de trabajar con claves y valores simultáneamente es usar el método items(). Esto te devuelve una lista de tuplas de la forma (clave,valor) sobre la que podés iterar.
d = {
        'nombre' : 'Lima',
        'cajones' : 75,
        'precio'  : 32.2
    }

items = d.items() # dict_items([('nombre', 'Lima'), ('cajones', 75), ('precio', 32.2), ('fecha', (14, 8, 2020))])
for k, v in d.items():
        print(k, '=', v)
#nombre = Lima
#cajones = 75
#precio = 32.2

#Si pasás un diccionario a una lista, obtenés sus claves.

list(d)
#['nombre', 'cajones', 'precio', 'fecha', 'cuenta']

#También podés obtener todas las claves del diccionario usando el método keys():
claves = d.keys()
#dict_keys(['nombre', 'cajones', 'precio', 'fecha', 'cuenta'])