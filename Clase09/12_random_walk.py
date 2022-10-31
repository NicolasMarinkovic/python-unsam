# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:34:40 2022

@author: nicol
"""


'''
En el siguiente ejemplo creamos un índice que contenga un elemento por minuto a partir 
del comienzo de la clase y durante 8 horas.
Armamos también una lista de nombres.
'''
import pandas as pd
import numpy as np

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

#Luego usamos el módulo random de numpy para generar pasos para cada persona a cada minuto. 
#Los acumulamos con cumsum y los acomodamos en un DataFrame, usando el índice generado antes y poniéndoles nombres adecuados a cada columna.

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

#Ahora suavizamos los datos, usando min_periods para no perder los datos de los extremos.

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
