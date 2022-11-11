# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:19:16 2022

@author: nicol
"""

# MI CODIGO ERA MUY SIMILAR, POR NO DECIR IDENTICO.
# PERO ME GUSTO MAS ESTE POR LOS COMENTARIOS
# PREFIERO DEJARLO ASI PARA TENER EN CONSIDERACION LOS DETALLES

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy()
        # Le agregue el .copy() porque sino pasaba la dirreccion de la lista

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
    

'''
madre_canguro = Canguro('Madre')

madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')

cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio(cangurito)
cangurito.meter_en_marsupio('juegos')

print(madre_canguro)
print(cangurito)
'''
# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.