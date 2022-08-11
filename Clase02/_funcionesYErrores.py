# Funciones
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
# Llamada a una funcion
suma = sumcount(100)

# Importar librerias
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()

# Atrapar y administrar excepciones

numero_valido=False
while not numero_valido:
    try: #Intenta correr un codigo y cuando hay un error salta directamente al except
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
#este except agarra todos los tipos de errores. Por ej:(RuntimeError, TypeError, NameError, ValueError):
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

# Generar excepciones
raise RuntimeError('¡Qué moco!')

#Traceback (most recent call last):
#  File "foo.py", line 21, in <módulo>
#    raise RuntimeError("¡Qué moco!")
#RuntimeError: ¡Qué moco!

#Alternativamente, esa excepción puede ser atrapada por un bloque try-except, pudiendo de esta forma evitar que el programa termine. 
