#%%
# Aseveraciones (assert)

#Si la expresión que queremos verificar es False, se levanta una excepción de tipo AssertionError. 
#La sintaxis de assert es la siguiente.
#assert <expresion> [, 'Mensaje']
assert isinstance(10, int), 'Necesito un entero (int)'

#%%
# Programación por contratos
# Es una forma de programar en la que el programador define, para cada parte del 
# programa, el tipo y formato de datos con que llamarla y el tipo de datos que devolverá.

def add(x, y):
    assert isinstance(x, int), 'Necesito un entero (int)'
    assert isinstance(y, int), 'Necesito un entero (int)'
    return x + y

add('2', '3')
#Traceback (most recent call last):
#...
#AssertionError: Necesito un entero (int)

#%%
# El debugger de Python (pdb)
# La función breakpoint () inicia el debugger. https://docs.python.org/3/library/pdb.html
def mi_funcion():
    #...
    breakpoint()      # Iniciar el debugger (Python 3.7+)
    #...

#%%
# DEBUGGER DE SPYDER
'''
Debug (ctrl+f5) ---->	inicia el modo debug
Step (ctrl+f10) ---->	da un paso en el programa
Step Into (ctrl+f11) ---->	entra en la función referida
Step Return (ctrl+shift+f11) ---->	ejecuta hasta salir de la función
Continue (ctrl+f12) ---->	retoma la ejecución normal
Stop (ctrl+shift+f12) ---->	detiene el programa
'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

rta = tiene_a ('palabra')
print(rta)


#%%
# Ejercicio 5.1

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append(lista[i]) #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')



#%%
# Ejercicio 5.2

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)


#%%