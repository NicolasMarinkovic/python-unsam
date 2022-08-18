# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:20:21 2022

@author: Nicolas
"""

# Tres tipos de errores:
    # Los errores sintácticos
    # Los errores en tiempo de ejecución, que se dan cuando el programa empieza a ejecutarse pero se produce un error durante su ejecución
    # Son los errores semánticos, que se dan cuando el programa no hace lo que está diseñado para hacer
    
# FORMAS DE DEBUGGEAR A MANO
# ¿Qué dice un traceback?
# Usá el modo REPL de Python
'''
python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>     print( repr(x) )
'''
# Debuggear con print
# Debuggear con lápiz y papel
# Disenar casos de prueba
'''
Un método útil para detectar errores de este tipo es diseñar "casos de prueba": 
conjuntos de datos de entrada cuya salida es conocida, que podés usar para tratar 
de poner en evidencia errores de escritura. Cuidado: pasar airosamente un caso de
prueba no verifica que tu programa funcione bien. Sólo dice que no pudiste detectar 
un error en su lógica. El diseño de casos de prueba es un arte en sí mismo. 
Ejercitar en esa técnica desde temprano puede serte muy útil.
'''