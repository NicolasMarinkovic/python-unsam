# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:56:11 2022

@author: nicol
"""

# IDENTIDAD Y REFERENCIA
# Podés usar el operador is (es) para verificar si dos valores corresponden al mismo objeto.

a = [1,2,3]
b = a
a is b
#True


# is compara la identidad del objeto. Esta identidad también la podés obtener usando id().
id(a)
#3588944
id(b)
#3588944


# COPIAS SUPERFICIALES  (superficiales en el sentido de poco profundas)
# Las listas y diccionarios tienen métodos para hacer copias (no meras referencias, sino duplicados):

a = [2,3,[100,101],4]
b = list(a) # Hacer una copia
a is b
# False

# A pesar de esto, los elementos de a y de b siguen siendo compartidos.
a[2].append(102)
b[2]
#[100,101,102]

a[2] is b[2]
#True

# PERO B ES OTRA LISTA
a.append(5)
a
#[2, 3, [100, 101], 4, 5]
b
#[2, 3, [100, 101], 4]



# COPIAS PROFUNDAS
# Podés usar la función deepcopy del módulo copy para esto:
a = [2,3,[100,101],4]
import copy
b = copy.deepcopy(a)
a[2].append(102)
b[2]
#[100,101]
a[2] is b[2]
#False


    
    
    
    
    



