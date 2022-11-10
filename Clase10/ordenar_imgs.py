# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 03:18:58 2022

@author: nicol
"""
from listar_imgs import archivos_png

from datetime import datetime
import re
import os
from pathlib import Path

#%%
def procesar_nombre(fname):
    '''
    Toma el nombre de un archivo y devuelve la fecha y el nombre corregido.
    pre: nombre de un archivo, puede venir con su extension
    '''
    
    nombre, extension = os.path.splitext(fname)
    
    fecha = re.findall('[0-9]+', nombre) ## Utilizo regex para tomar los nros
    letras = '_'.join(re.findall('[a-z]+', nombre)) ## Utilizo regex para tomar las letras

    date_object = datetime.strptime(fecha[0], '%Y%m%d')
    
    return letras, date_object    
#%%   
def procesar(nuevo_nombre, fecha_mod, pathPng) :
    '''
    Procesa cada archivo.
    Usa la función procesar_nombre para renombrar, mover y modificar la fecha de cada archivo.
    pre:
        Recibe los dos valores de procesar_nombre
        Y además el path del archivo png
    '''
    nuevo_nombre += '.png'
    
    ts_fechamod = fecha_mod.timestamp()
    os.utime(pathPng, (ts_fechamod, ts_fechamod))
    
    if not os.path.exists('../imgs_procesadas/'):
        os.mkdir('../imgs_procesadas/')
    os.rename(pathPng, os.path.join('../imgs_procesadas/',nuevo_nombre))
    
#%%  
def principal(directorio):
    '''
    Funcion Principal
    Recibe un directorio
    Busca todos los archivos pngs que se encuentra en el directorio
    El nombre del archivo debe ser -> letras_minusculas_YYYYDDMM, como fecha codificada
    Mueve todos los pngs a la carpeta imgs_procesadas modificando su fecha de creacion
    '''
    
    paths_pngs = archivos_png(directorio) # archivos_png trae el path del archivo png
    
    for png in paths_pngs:
        nombre_archivo, fecha_ult_mod = procesar_nombre(Path(png).stem) # Le paso solo el nombre del archivo
        procesar(nombre_archivo, fecha_ult_mod, png)
                
    ## Elimino las carpetas que quedaron vacias
#    '''
    subdirec_borrados = 1
    while (subdirec_borrados != 0):
        subdirec_borrados = 0
        for root, dirs, files in os.walk(directorio):
            for name in dirs:
                 
                dir = os.path.join(root, name, '..') ## Me paro en la carpeta anterio al subdirectorio
                os.chdir(dir)
                
                if (os.listdir(name) == []): ## Pregunto si el subdirectorio esta vacio
                    os.rmdir(name)
                    subdirec_borrados += 1
#    '''
            
#%%

if (__name__ == '__main__'):
    import sys
    path = 'C:/Users/nicol/OneDrive/Escritorio/Facultad/Programacion1/Ejercicios/ejercicios_python'
    directorio = 'Data/ordenar'
    if len(sys.argv) == 2:
        directorio = sys.argv[1]
        principal(directorio)
    else:
        principal(os.path.join(path,directorio))