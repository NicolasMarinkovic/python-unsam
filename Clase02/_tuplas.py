# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:30:19 2022

@author: Nicolas
"""

#Tuplas
#Una tupla es una colección con valores agrupados juntos.

s = ('Manzanas', 100, 490.1)
nombre = s[0]                   # 'Manzana'
cantidad = s[1]                 # 100
precio = s[2]                   # 490.1

#El contenido de las tuplas no puede ser modificado.
s[1] = 75                   #TypeError: object does not support item assignment
#Podés, sin embargo, hacer una nueva tupla basada en el contenido de otra, que no es lo mismo que modificar el contenido.
s = (s[0], 75, s[2])      # ('Manzanas', 75, 490.1)

# Desempaquetar tuplas
#Para usar una tupla en otro lado, debemos desempaquetar su contenido en diferentes variables.

fruta, cajones, precio = s      #El número de variables a la izquierda debe ser consistente con la estructura de la tupla.
print('Costo:', cajones * precio)

# TUPLAS vs LISTAS
#Las tuplas parecieran ser listas de solo-lectura. Sin embargo, las tuplas suelen usarse para un solo ítem que consiste de múltiples partes mientras que las listas suelen usarse para una colección de diferentes elementos, típicamente del mismo tipo.

record = ('Manzanas', 100, 490.1)                # Una tupla representando un registro dentro de un pedido de frutas

symbols = [ 'Manzanas', 'Peras', 'Mandarinas' ]  # Una lista representando tres frutas diferentes.

# Si tenés tuplas como en items podés crear un diccionario usando la función dict().
nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
#[('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
d = dict(nuevos_items)
#{'nombre': 'Manzanas', 'cajones': 100, 'precio': 490.1, 'fecha': (13, 8, 2020)}