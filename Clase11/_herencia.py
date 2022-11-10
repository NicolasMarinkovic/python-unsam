#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:48:18 2022

@author: datascience
"""
'''
HERENCIA
'''
#Se usa herencia para crear objetos más especializados a partir de objetos existentes.

class Padre:
    ...

class Hijo(Padre):
    ...
    
# Ejemplo
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones
        
'''        
Agregar un método nuevo
'''

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)

c = MiLote('Pera', 100, 490.1)
c.vender(25)
c.cajones
#75
c.rematar()
c.cajones
#0

#Esta clase heredó los atributos y métodos de Lote y la extendío con un nuevo método (rematar()).

'''
Redefinir un método existente
'''

class MiLote(Lote):
    def costo(self):
        return 1.25 * self.cajones * self.precio

#Un ejemplo de uso:

c = MiLote('Pera', 100, 490.1)
c.costo()
#61262.5

# El método nuevo simplemente reemplaza al definido en la clase base. Los demás métodos y atributos no son afectados. ¿No es buenísimo?

'''
Utilizar un método prevalente
'''
#Hay veces en que una clase extiende el método de la superclase a la que pertenece, pero necesita ejecutar el método original como parte de la redefinición del método nuevo. Para referirte a la superclase, usá super():

class Lote:
    ...
    def costo(self):
        return self.cajones * self.precio
    ...

class MiLote(Lote):
    def costo(self):
        # Fijate cómo usamos `super`
        costo_orig = super().costo()
        return 1.25 * costo_orig
# Usá super() para llamar al método de la clase base (del la cual ésta es heredera).

'''
Herencia múltiple.
'''

#Podés heredar de varias clases simultáneamente si los especificás en la definición de clase.

class Madre:
    ...

class Padre:
    ...

class Hijo(Madre, Padre):
    ...
