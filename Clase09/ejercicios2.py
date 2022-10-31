# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:42:02 2022

@author: nicol
"""

import pandas as pd
import os
import seaborn as sns

#%% Ejercicio 9.6: Lectura y selección
directorio = '../Data'
archivo =  'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)   #DataFrame

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel].copy() 
cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()


especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


#%% Ejercicio 9.7: Boxplots

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')


#%% Ejemplo de pairplot (seaborn)

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

'''
El gráfico va a tener una fila (y columna) por cada variable numérica en el DataFrame pasado como data. En la diagonal del gŕafico, va a haber kdeplots (kernel density estimation plots, una versión suavizada de los histogramas) y fuera de la diagonal scatterplots combinando todos los pares de variables (cada combinación aparece dos veces, una sobre y otra debajo de la diagonal).

El hue selecciona la variable categórica a usar para distinguir subgrupos y asociarles colores. En la diagonal de este ejemplo (y en los scatterplots también) se ve por ejemplo que las Tipas suelen ser más anchas y más altas que los Tilos y los Jacarandás.
'''