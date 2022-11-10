#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:06:25 2022

@author: datascience
"""


'''
METODOS ESPECIALES
'''
# Una clase puede tener definidos métodos especiales. 
# Estos métodos tienen un significado particular para el intérprete de Python. 
# Sus nombres empiezan y terminan en __ (doble guión bajo). Por ejemplo __init__.

class Lote(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
   
'''
Invocar métodos
'''

# El proceso de invocar un método puede dividirse en dos partes:

#    Búsqueda: Se usa el operator .
#    Llamado: Se usan ()

m = Lote('Pera', 100, 490.10)
c = m.costo  # Búsqueda
c
# <bound method Lote.costo of <Lote object at 0x590d0>>
c()          # Llamado
# 49010.0     
    
'''
Métodos especiales para convertir a strings
'''

from datetime import date
d = date(2020, 12, 21)
str(d)
# '2020-12-21'
repr(d)
# 'datetime.date(2020, 12, 21)'

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Con `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Con `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'

'''
Métodos matemáticos especiales
'''

#Las operaciones matemáticas sobre los objetos involucran llamados a los siguientes métodos.

'''
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()        
'''
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    ...
    ...
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
  
# Al definir un método __add__(b) en la clase Punto, por ejemplo, nos permitirá sumar dos instancias de esta clase usando el operador +.
a = Punto(1,2)  
b = Punto(3,4)  
repr(a + b)
# 'Punto(4, 6)'

'''
Métodos especiales para acceder a elementos
'''
#Los siguientes métodos se usan para implementar contenedores:

'''
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
'''

#Los podés implementar en tus clases.

class Secuencia:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...

'''
Acceso a atributos
'''

#Existe una forma alternativa de acceder, manipular, y administrar los atributos de un objeto.

'''
getattr(obj, 'name')          # Equivale a obj.name
setattr(obj, 'name', value)   # Equivale a obj.name = value
delattr(obj, 'name')          # Equivale a del obj.name
hasattr(obj, 'name')          # Mira si la propiedad existe
'''

if hasattr('obj', 'x'):
    x = getattr('obj', 'x')
else:
    x = None

# Nota: si getattr() no encuentra el atributo buscado (x en este ejemplo), devuelve el argumento opcional arg (None en este caso)

x = getattr('obj', 'x', None)


import lote
c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
    print(colname, '=', getattr(c, colname))

# nombre = Peras
# cajones = 100











