# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:03:42 2022

@author: nicol
"""

'''

Una pila (stack en inglés) es una estructura de datos. Se trata de una lista ordenada 
que permite almacenar y recuperar datos, con un modo de acceso de tipo LIFO 
(del inglés Last In, First Out, «último en entrar, primero en salir»). 
Funcionan de manera opuesta que las colas que mencionamos antes.


Las pilas y colas son estructuras de datos que se aplican en multitud de contextos 
debido a su simplicidad y capacidad de modelar diferentes procesos.

La operaciones (métodos) elementales de las pilas son apilar (coloca un objeto en la pila)
y desapilar (retira el último elemento apilado). En inglés se llaman push y pop y
son análogos al encolar y el desencolar de la colas.
 
'''

# La pila de llamadas (en inglés call stack) de un lenguaje (por ejemplo Python), es una pila manejada por el intérprete que almacena la información sobre las subrutinas activas en cada instante. También se la conoce como pila de ejecución o pila de control y se usa para llevar registro de las funciones que se fueron llamando y el de las variables definidas en cada contexto.


def f():
    x = 50
    a = 20
    print("En f, x vale", x)

def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)
    
#la ejecución de g() resulta en:

g()
#En g, antes de llamar a f, x vale 10
#En f, x vale 50
#En g, después de llamar a f, x vale 10. 