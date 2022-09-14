# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:50:18 2022

@author: nicol
"""

import numpy as np

#%%
# CREAR ARREGLOS USANDO DATOS EXISTENTES

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr1 = a[3:8]
# array([4, 5, 6, 7, 8])

# Esto genera una vista.
# Si modificás un elemento de la vista, ¡también se modificará en el original!
arr1[0] = 44
# [ 1  2  3 44  5  6  7  8  9 10]

#Podés usar el método copy para copiar los datos. Por ejemplo:
b2 = a[1, :].copy()
# array([5, 6, 7, 8])

#%% 
# OPERACIONES BÁSICAS SOBRE ARREGLOS

data = np.array([1, 2])
ones = np.ones(2, dtype=int)

data + ones
# array([2, 3])
data - ones
# array([0, 1]
data * data
#array([1, 4])
data / data
#array([1., 1.])


# sum()
a = np.array([1, 2, 3, 4])
a.sum()
#10
# SUMAR VALORES POR FILA O COLUMNA
b = np.array([[1, 1], [2, 2]])
b.sum(axis=0) # Suma por columna
# array([3, 3])

#%%
# BROADCASTING
# Hay veces en que necesitás realizar una operación entre un arreglo y un número (en matemática le decimos, un escalar)
data = np.array([1.0, 2.0])
data * 1.6
# array([1.6, 3.2])
# Los tamaños deben ser compatibles. Si los tamaños no son compatibles, te va a dar un ValueError

'''
También se pueden sumar matrices de tamaños diferentes, 
pero sólo si una de ellas tiene una sola fila o una sola columna. 
En este caso, NumPy va a usar las reglas de broadcast para la operación.
'''

#%%
# OPERACIONES UN POCO MÁS COMPLEJAS
'''
Además de min, max, y sum, podés usar 
mean para obtener el promedio, 
prod para calcular el producto, 
std para obtener el desvío estándar de los datos, y más
'''
a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
a.sum()
4.8595784
a.min()
#0.05093587
a.min(axis=0)
#array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])x|

# .random.random genera vectores o matrices aleatorias.
np.random.random(3)
#array([0.63696169, 0.26978671, 0.04097352]) 
np.random.random((3, 2))
# array([[0.01652764, 0.81327024],
# [0.91275558, 0.60663578],
# [0.72949656, 0.54362499]])  # puede variar

#%%
# FÓRMULAS MATEMÁTICAS
# Existen fórmulas matématicas en numpy, si algún día necesitas, googlealo.

#%%
# GUARDAR Y CARGAR OBJETOS DE NUMPY
# Los objetos ndarray pueden guardarse y leerse de disco con las funciones loadtxt y savetxt
# Es sencillo guardar un arreglo con np.save()

a = np.array([1, 2, 3, 4, 5, 6])

np.save('filename', a)

b = np.load('filename.npy')

# [1 2 3 4 5 6]

# En formato de texto plano, lo podés guardar como .csv o .txt con np.savetxt.
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

np.savetxt('new_file.csv', csv_arr)

np.loadtxt('new_file.csv')
#array([1., 2., 3., 4., 5., 6., 7., 8.])








