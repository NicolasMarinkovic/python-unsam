# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:34:42 2022

@author: nicol
"""

'''

Una cola es una estructura de datos. Se caracteriza por contener una secuencia de 
elementos y dos operaciones: encolar y desencolar. La primera, encolar, agrega 
un elemento al final de la secuencia que contiene la cola. Desencolar, por su parte, 
devuelve el primer elemento de la secuencia y lo elimina de la misma.

Las colas también se llaman estructuras FIFO (del inglés First In First Out), 
debido a que el primer elemento en entrar a la cola será también el primero en salir. 
El nombre cola se le da por su analogía con las colas que hacemos (o hacíamos cuando 
podíamos salir de casa) para entrar al cine, por ejemplo.

'''


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0