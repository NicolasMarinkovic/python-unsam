#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:12:16 2022

@author: datascience
"""
#%%
try:
    print('hacer_algo()')
except Exception as e:
    print('Hubo un error. Porque...', e)
    


#finally especifica que esa porción de código debe ejecutarse sin importar si una excepción fue atrapada o no.

lock = 'Lock()'
#...
lock.acquire()
try:
    print('hola')
finally:
    lock.release()  # esto SIEMPRE se ejecuta. Haya o no haya excepciones.

#Una estructura como ésa resulta en un manejo seguro de los recursos disponibles (seguros, archivos, hardware, etc.)
#%%

# Módulo principal en Python

# Python no tiene una función o método principal. En su lugar existe un módulo principal y éste será el archivo con código fuente que se ejecuta primero.

'bash % python3 prog.py'

#Chequear __main__

# prog.py

if __name__ == '__main__':
    # Soy el programa principal ...
    print('comandos')
    
'bash % python3 prog.py' # Corriendo como principal

import prog   # Corriendo como módulo importado    

'''
La variable __name__ es el nombre del módulo. 
Sin embargo, esta variable __name__ valdrá __main__ 
si ese módulo está siendo ejecutado como el script principal.
'''

#%%
#Standard I/O
'''
Los archivos de entrada y salida estándard (Standard Input / Output (stdio)) 
son archivos que se portan como archivos normales, pero están definidos 
por el sistema operativo.
'''

#sys.stdout
#sys.stderr
#sys.stdin

'''
Por omisión, la salida impresa es dirigida a sys.stdout (usualmente la pantalla), 
la entrada se lee de sys.stdin (usualmente el teclado), 
y la recapitulación de errores es dirigida a sys.stderr (usualmente, la pantalla otra vez).

Las entradas y salidas de stdio pueden estar ligadas al teclado, 
a la pantalla, a una impresora, a diferentes archivos o incluir 
cosas más extrañas como pipes, etc.
'''

#bash % python3 prog.py > resultados.txt
# o si no
#bash % cmd1 | python3 prog.py | cmd2

'''
Esta sintaxis se llama "piping" o redireccionamiento y significa: 
    ejecutar cmd1, enviar su salida como entrada a prog.py 
    invocado desde la terminal, y la salida de éste será la entrada para cmd2.
'''

#Terminación del programa

#La terminación y salida del programa se administran a través de excepciones.

raise SystemExit
raise SystemExit('codigo_salida')

#O, alternativamente:

import sys
sys.exit('codigo_salida')

#Es estándar que un codigo de salida de 0 indica que no hubo problemas y otro valor, que los hubo, donde el valor indica que tipo de problema hubo.

# El comando #!
#Bajo Unix (Linux es un Unix) una línea que comienza con #! ejecutará un script en el intérprete Python.
#!/usr/bin/env python3
#Al iniciar un script Python en Windows, se lee la línea que comienza con #! dentro del script para saber qué versión del intérprete invocar.

'''
Bajo Linux, para ejecutar el archivo prog.py vas a necesitar habilitar su 
permiso de ejecución. Podés habilitar este permiso de ejecución así ... 
(bajo windows esto no es necesario, ya que el programa que estás ejecutando 
 es formalmente el interprete de python):
'''
'bash % chmod +x prog.py'
# Ahora lo podés ejecutar
'bash % ./prog.py'

# Para terminar, éste es un modelo usual de programa en Python que se ejecuta invocado desde la terminal.

#!/usr/bin/env python3
# prog.py

# Import (bibliotecas)
import modules

# Funciones
def spam():
    ...

def blah():
    ...

# Funcion principal
def f_principal(parametros):
    # Analizar la línea de comandos, 
    # usando la variable parámetros en lugar 
    # de sys.argv, donde corresponda
    ...

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)













