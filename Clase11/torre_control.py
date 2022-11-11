# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:38:23 2022

@author: nicol
"""

class TorreDeControl:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, x):
        '''Encola el elemento x.'''
        self.arribos.append(x)
    
    def nueva_partida(self, y):
        '''Encola el elemento y.'''
        self.partidas.append(y)
    
    def ver_estado(self):
        '''Devuelve las colas de arribos
        y partidas'''
        print('Vuelos esperando para aterrizar:', end=' ')
        for x in self.arribos:
            print(x, end = '')
            if x != self.arribos[-1]:
                print(', ', end='')
            
        
        print('\nVuelos esperando para despegar:', end=' ')
        for x in self.partidas:
            print(x, end = '')
            if x != self.partidas[-1]:
                print(', ', end='')
    
    def asignar_pista(self):
        '''Elimina el primer vuelos de la cola 
        Le da prioridad a los arribos
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia(self.arribos):
            if self.esta_vacia(self.partidas):
                return 'No hay vuelos en espera'
            return f'El vuelo {self.partidas.pop(0)} aterrizó con éxito'
        return f'El vuelo {self.arribos.pop(0)} aterrizó con éxito'

    def esta_vacia(self, tipo):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(tipo) == 0

#%%

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
# Vuelos esperando para aterrizar: AR156, AR32
# Vuelos esperando para despegar: KLM1267
torre.asignar_pista()
# El vuelo AR156 aterrizó con éxito.
torre.asignar_pista()
# El vuelo AR32 aterrizó con éxito.
torre.asignar_pista()
# El vuelo KLM1267 despegó con éxito.
torre.asignar_pista()
# No hay vuelos en espera.    
    
    
