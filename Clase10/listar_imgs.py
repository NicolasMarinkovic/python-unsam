# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 02:36:53 2022

@author: nicol
"""

import os

def archivos_png(directorio):
    '''
    Devuelve todos los archivos png de un directorio
    '''
    pngs = []
    os.chdir(directorio)
    for root, dirs, files in os.walk(directorio):
        for name in files:
            archivo, extension = os.path.splitext(name)
            if (extension == '.png'):
                pngs.append(os.path.join(root,name))
            
    return pngs
    
if (__name__ == '__main__'):
    import sys
    path = 'C:/Users/nicol/OneDrive/Escritorio/Facultad/Programacion1/Ejercicios/ejercicios_python'
    directorio = 'Data/ordenar'
    if len(sys.argv) == 2:
        directorio = sys.argv[1]
        archivos_png(directorio)
    else:
        print(archivos_png(os.path.join(path,directorio)))
    

    
    