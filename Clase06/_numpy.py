# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:39:16 2022

@author: Nicolas
"""

'''
Ocasionalmente vas a ver que alguien se refiere a un arreglo como un “ndarray” 
que es una forma breve de decir arreglo n-dimensional. Un arreglo n-dimensional
 es simplemente un arreglo con n dimensiones. Recordemos que cuando son UNIDIMENSIONALES 
 los llamamos VECTORES y si son BIDIMENSIONALES los llamamos MATRICES.
'''


import numpy as np

#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[0]) # si tiene múltiples dimensiones, esto me da una "rebanada" de una dimensión menos
#[1 2 3 4]
print(a[2]) # otra rebanada
#[ 9, 10, 11, 12]
print(a[2][3]) # accedo al cuarto elemento del tercer vector de a
#12
print(a[2,3]) # o, equivalentemente, accedo al elemento en la tercera fila y cuarta columna de a
#12

#%%
# CREACION DE ARREGLOS

# Crea un arreglo lleno de 0's
np.zeros(2)
#array([0., 0.])

# lleno de 1’s:
np.ones(2)
#array([1., 1.])

# Crea un arreglo cuyo contenido inicial depende del estado de la memoria. Lo bueno de usar empty en lugar de zeros (o ones) es la velocidad - al no inicilizar los valores no perdemos tiempo. 
# ¡Pero asegurate de ponerle valores con sentido luego!
np.empty(2)
#array([ 3.14, 42.  ])  # puede variar

# Crear vectores a partir de un rango de valores:
np.arange(4)
#array([0, 1, 2, 3])
np.arange(2, 9, 2) # o np.arange(2, 10, 2)
#array([2, 4, 6, 8])

# Crea un vector de valores equiespaciados especificando el primer número, el último número, y la cantidad de elementos:
np.linspace(0, 10, num=5)
#array([ 0. ,  2.5,  5. ,  7.5, 10. ])


#%%
# ESPECIFICAR TIPO DE DATOS

np.ones(2, dtype=np.int64)
#array([1, 1])

#%%
# AGREGAR, BORRAR Y ORDENAR ELEMENTOS

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

# Ordenar un vector es sencillo usando np.sort()
np.sort(arr)        # no modificó el original.
#array([1, 2, 3, 4, 5, 6, 7, 8])


#  la concatenación
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
#array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)
#array([[1, 2],
# [3, 4],
# [5, 6]])

#%%
# CONOCER EL TAMAÑO, DIMENSIONES Y FORMA DE UN ARREGLO

'''
ndarray.ndim te dice la cantidad de ejes (o dimensiones) del arreglo.

ndarray.shape te va a dar una tupla de enteros que indican la cantidad de elementos en cada eje. 
Si tenés una matriz con 2 filas y 3 columnas de va a dar (2, 3).

ndarray.size te dice la cantidad de elementos (cantidad de números) de tu arreglo. 
Es el producto de la tupla shape. En el ejemplo del renglón anterior, el size es 6.
'''
array_ejemplo = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],
                          
                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],
                           
                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])


array_ejemplo.ndim # cantidad de dimensiones
#3
array_ejemplo.shape # cantidad de elementos en cada eje 
#(3, 2, 4)
array_ejemplo.size # total de elementos 3*2*4
#24

#  Usando arr.reshape() le podés dar una NUEVA FORMA a tu arreglo sin cambiar los datos. 
a = np.arange(6)
#[0 1 2 3 4 5]

b = a.reshape(3, 2)
#[[0 1]
# [2 3]
# [4 5]]

#%%
# AGREGAR UN NUEVO EJE A UN ARREGLO
# Usando np.newaxis una vez podés incrementar la dimensión de tu arreglo en uno. 
# Por ejemplo podés pasar de un vector a una matriz o de una matriz a un arreglo tridimensional


a = np.array([1, 2, 3, 4, 5, 6])
a.shape
#(6,)

#Podés usar np.newaxis para agregarle una dimensión y convertirlo en un vector fila:
vec_fila = a[np.newaxis, :]
vec_fila.shape
#(1, 6)

#O, para convertirlo en un vector columna, podés unsertar un eje en la segunda dimensión:
vec_col = a[:, np.newaxis]
vec_col.shape
#(6, 1)


#%%
# ÍNDICES Y REBANADAS
data = np.array([1, 2, 3])
data[1]
#2
data[0:2]
#array([1, 2])
data[1:]
#array([2, 3])
data[-2:]
#array([2, 3])

# OTRA OPERACIÓN MUY ÚTIL ES SELECCIONAR LOS ELEMENTOS QUE CUMPLEN CIERTA CONDICIÓN

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#Podés imprimir todos los valores menores que cinco.
print(a[a < 5])
#[1 2 3 4]

#También podés seleccionar, por ejemplo, aquellos elementos mayores o iguales que 5 y usar el resultado para indexar el arreglo.
five_up = (a >= 5)
a[five_up]
#[ 5  6  7  8  9 10 11 12]
#Es interesante que five_up da un arreglo de valores booleanos. True si satisface la condición y False si no la satisface.

#Podés seleccionar los elementos pares:

pares = a[a%2==0]
#[ 2  4  6  8 10 12]

#Usando los operadores lógicos & y | podés combinar dos o más condiciones.
c = a[(a > 2) & (a < 11)]
#[ 3  4  5  6  7  8  9 10]

#o para definir una nueva variable booleana:

five_up = (a > 5) | (a == 5)
#[[False False False False]
# [ True  True  True  True]
# [ True  True  True True]]

#Finalmente, podés usar np.nonzero() para obtener las coordenadas de ciertos elementos de un arreglo.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#Podés usar np.nonzero() para imprimir los índices de los elementos que son, digamos, menores que 5:
b = np.nonzero(a < 5)
#(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
#En este ejemplo, la respuesta es una tupla de arreglos: uno por cada dimensión. El primer arreglo representa las filas de los elementos que satisfacen la condición y el segundo sus columnas.
lista_de_coordenadas = list(zip(b[0], b[1]))

for coord in lista_de_coordenadas:
     print(coord)
#(0, 0)
#(0, 1)
#(0, 2)
#(0, 3)
#Podés usar np.nonzero() para imprimir o seleccionar los elementos del arreglo que son menores que 5:

print(a[b])
#[1 2 3 4]

#Si la condición que ponés no la satisface ningún elemento del arreglo entonces el arreglo de índices que obtenés con np.nonzero() será vacío. Por ejemplo:
no_hay = np.nonzero(a == 42)
#(array([], dtype=int64), array([], dtype=int64))






