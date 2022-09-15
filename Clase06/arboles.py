# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:21:03 2022

@author: Nicolas
"""
import csv
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

#%%
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        types = [str, str, str, float, float, int, str, str, str, str, str, str, str, str, str, str, str]
        arboleda = [{ name: func(val) for name, func, val in zip(encabezados, types, row) } for row in rows]
        
    return arboleda

#%%
def medidas_de_especies(especies,arboleda):
    diccionario = [{ especie: [
                        (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if (arbol['nombre_com'] == especie)] 
                    } for especie in especies]
    return list(diccionario[2])

#%%
if(len(sys.argv) >= 2):
   raise Exception("El programa esta armado para el archivo arbolado-en-espacios-verdes.csv, correré este automáticamente.")
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
   
#%% Ejercicio 5.16
H = [arbol['altura_tot'] for arbol in arboleda if (arbol['nombre_com'] == 'Jacarandá')]

#%% Ejercicio 5.17
HD = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if (arbol['nombre_com'] == 'Jacarandá')]

#%% Ejercicio 5.18
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
diccionario_especies = medidas_de_especies(especies,arboleda)

#%%Ejercicio 6.10
def mostrarAlturas(lista_de_alturas):
    altos = [lista_de_alturas]
    plt.hist(altos,bins=100)
    plt.show()
mostrarAlturas(H)
#%%Ejercicio 6.11
def scatter_hd(lista_de_pares):
    H, D = [h for h, d in lista_de_pares], [d for h, d in lista_de_pares]

    plt.scatter(D,H, s=D, c=H, alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
    
scatter_hd(HD)

#%%Ejercicio 6.12
