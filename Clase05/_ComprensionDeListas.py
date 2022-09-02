# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:05:26 2022

@author: nicol
"""

#Sintaxis general
#[<expresión> for <variable> in <secuencia> if <condición>]

# ES IGUAL A 
resultado = []
for variable in secuencia:
    if condición:
        resultado.append(expresión)

#-------------------------------------

a = [1, 2, 3, 4, 5]
b = [2*x for x in a]
#[2, 4, 6, 8, 10]


nombres = ['Edmundo', 'Juana']
a = [nombre.lower() for nombre in nombres]
#['edmundo', 'juana']


# FILTROS
a = [1, -5, 4, 2, -2, 10]
b = [2*x for x in a if x > 0]
# [2, 8, 4, 20]

# CASOS DE USO
# Podés recolectar los valores de un campo específico de un diccionario:
frutas = [s['nombre'] for s in camion]

#O podés hacer consultas (queries) como si las secuencias fueran bases de datos.
a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50]

#También podés combinar la comprensión de listas con reducciones de secuencias:
costo = sum([s['cajones']*s['precio'] for s in camion])

#--------------------------

# Si cambiás los corchetes ([,]) por llaves ({, }), obtenés algo que se conoce como comprensión de conjuntos. 
# Vas a obtener VALORES ÚNICOS.

nombres = {s['nombre'] for s in camion}
#{'Caqui', 'Durazno', 'Lima', 'Mandarina', 'Naranja'}

# Si especificás pares clave:valor, podés construir un diccionario.

camion_precios = {nombre: precios[nombre] for nombre in nombres}
#{'Caqui': 105.46, 'Durazno': 73.48, 'Lima': 40.22, 'Mandarina': 80.89, 'Naranja': 106.28}


#----------------------------
# Ejemplos usando informe.py
# Generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.
mas100 = [s for s in camion if s['cajones'] > 100]
#[{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 #{'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23}]

# Ahora, una con la info sobre cajones de Mandarina y Naranja.
myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]


# O una con la info de las frutas que costaron más de $10000.
costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
#[{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 #{'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23}]

# Construí una lista de tuplas (nombre, cajones) que indiquen la cantidad de cajones de cada fruta tomando los datos de camion.
nombre_cajones =[(s['nombre'], s['cajones']) for s in camion]
#[('Lima', 100), ('Naranja', 50), ('Caqui', 150), ('Mandarina', 200), ('Durazno', 95), ('Mandarina', 50), ('Naranja', 100)]









