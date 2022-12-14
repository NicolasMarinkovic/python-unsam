#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:35:10 2022

@author: datascience
"""

class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre 
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self):
        return f'Date(\'{self.nombre}\', {self.cajones}, {self.precio})'    
    
    def costo(self):
        return self.cajones * self.precio
        
    def vender(self, ncajones):
        self.cajones -= ncajones
    

'''
a = Lote('Pera', 100, 490.10)
b = Lote('Manzana', 50, 122.34)
c = Lote('Naranja', 75, 91.75)

lotes = [a, b, c]
for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
'''