# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:47:19 2022

@author: nicol
"""

import os

'''
Otra libreria interesante es shutil. Pero es de alto nivel.

rmtree() del módulo shutil. Borra directorios aunque no esten vacios
move() del módulo shutil. Copia y borra
'''



#%%
'''
OBTENER EL DIRECTORIO ACTUAL
'''
os.getcwd()
# 'C:\\Users\\nicol\\OneDrive\\Escritorio\\Facultad\\Programacion1\\Ejercicios\\ejercicios_python\\Clase10'

#%%
'''
CAMBIAR EL DIRECTORIO DE TRABAJO
'''
os.chdir('../Data')              # entro en ../Data
os.getcwd()
# 'etcetc..\\ejercicios_python\\Data'

# En diferentes sistemas operativos las barras de directorio se escriben de diferentes maneras. 
# Es recomendable usar el comando os.path.join como en el siguiente ejemplo de manera que 
# tu código funcione independientemente del sistema operativo en el que se lo corra.
directorio = os.path.join('c:\\', 'usuario', 'ejercicios_python')
os.chdir(directorio)

#%%
'''
LISTAR DIRECTORIOS Y ARCHIVOS
'''
os.listdir('../Data')

#%%
'''
CREAR UN NUEVO DIRECTORIO
'''
# Toma como argumento el path del nuevo directorio. por default tiene el actual
os.mkdir('test')          # creo el directorio test
os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
os.listdir('test')
# ['carpeta']
#%%

'''
RENOMBRAR UN DIRECTORIO O UN ARCHIVO
'''
# rename() toma dos argumentos, el viejo nombre y el nuevo nombre.
os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
os.listdir()
#['carpeta_nueva']
os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja') # cambio el path
os.listdir('test')                                  # test quedó vacío
# []

#%%
'''
ELIMINAR UN DIRECTORIO O UN ARCHIVO
'''
# Estas acciones no pueden deshacerse: Usar con precaución
os.remove('archivo.txt')    # elimino el archivo
os.listdir()
# ['subcarpeta']

os.rmdir('subcarpeta')      # elimino la subcarpeta
# rmdir() solamente puede borrar directorios si están vacíos
os.listdir()
# []

#%%
'''
RECORRIENDO DIRECTORIOS CON OS.WALK()
'''
# walk() del módulo os genera una lista con los nombres de todos los archivos del árbol de subdirectorios de un directorio dado.
# Unico parámetro obligatorio el directorio donde comenzar a mirar
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

#%%
'''
CAMBIAR ATRIBUTOS DE UN ARCHIVO
'''
# Vamos a cambiar la fecha de modificación de un archivo. Para ello necesitás 
# importar os y datetime. Después, convertís la fecha elegida a timestamp y se 
# la asocías al archivo con utime, como se muestra acá abajo

import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))



