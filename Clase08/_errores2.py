# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:57:05 2022

@author: Nicolas
"""

# ERRORES
try:
    ...
except RuntimeError as e:   
    # `e` contiene la excepción lanzada con su mensaje específico
    print(e)
    
try:
    pass    
except RuntimeError as e:
    print('Fracasé. Motivo:', e)
    
'''
Podés atrapar múltiples excepciones
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...

LAS PODÉS AGRUPAR:
try:
  ...
except (IOError, LookupError, RuntimeError) as e:
  ...

'''
