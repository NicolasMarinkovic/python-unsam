'''
Resumen

    El contrato de una función especifica qué condiciones se deben cumplir para que la función pueda ser invocada (precondición), y qué condiciones se garantiza que serán válidas cuando la función termine su ejecución (poscondición).
    La documentación tiene como objetivo explicar qué hace el código, y está dirigida a quien desee utilizar la función o módulo.
    Es una buena práctica incluir el contrato en la documentación.
    Si una función modifica un valor mutable que recibe por parámetro, eso debe estar explícitamente aclarado en su documentación.
    Los comentarios tienen como objetivo explicar cómo funciona el código y por qué se decidió implementarlo de esa manera, y están dirigidos a quien esté leyendo el código fuente.
    Los invariantes de ciclo son las condiciones que deben cumplirse al comienzo de cada iteración de un ciclo.

'''



# ASEVERACION
'''
Tanto las precondiciones como las poscondiciones pueden pensarse como 
aseveraciones (en inglés assertions). Es decir, afirmaciones realizadas en 
un momento particular de la ejecución sobre el estado computacional. Si una aseveración llegara 
a ser falsa, se levanta una excepción interrumpiendo la normal ejecución del programa.
'''

# Esta instrucción recibe una condición a verificar (o sea, una expresión booleana). Si la condición es True, la instrucción no hace nada; en caso contrario se produce un error.
'''
>>> assert True
>>> x = 0
>>> assert x != 0, 'El divisor no puede ser 0'
(^Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
AssertionError: El divisor no puede ser 0)
'''

'''
Atención: Es importante tener en cuenta que assert está pensado para ser 
usado en la etapa de desarrollo. Un programa terminado nunca debería dejar 
de funcionar por este tipo de errores.
'''

#%%
# DOCUMENTACION CON PRECONDICION Y POSCONDICION
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    n = 0
    '''
    while desde <= hasta:
        n += desde
        desde +=1
    '''
    if (desde <= hasta):
        n += desde
        n += sumar_enteros(desde+1,hasta)
    return n
    
print(sumar_enteros(1,5))
#%%

import math

def maximo(lista):
    '''
    Pre: La lista contiene elementos comparable entre sí y con math.inf
    Pos: La función devuelve el elemento máximo de la lista.
    '''

    max_elem = -math.inf
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem



# %%
# INVARIANTES DE CICLO
'''
Los invariantes se refieren a estados o situaciones que no cambian dentro de un contexto dado. Hay diferentes tipos de invariantes. A continuación veremos los invariantes de ciclo que nos ayudan a llegar desde las precondiciones hasta las postcondiciones.

Un invariante de ciclo es esencialmente una aseveración que debe ser verdadera al final de cada iteración. Pensar en términos de invariantes de ciclo nos ayuda a reflexionar y comprender mejor qué es lo que debe realizar nuestro código y nos ayuda a desarrollarlo.
'''

'''
En resumen, el concepto de invariante de ciclo es una herramienta que nos permite comprender (explicitar) mejor cómo funciona un algoritmo. Resulta fundamental en la teoría de algoritmos, donde es necesario para demostrar que:

    un algoritmo es correcto, es decir que realiza la tarea descripta por la pre y poscondición.
    un algoritmo termina (y no se cuelga).

'''