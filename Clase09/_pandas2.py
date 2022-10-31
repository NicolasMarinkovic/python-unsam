# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:15:11 2022

@author: nicol
"""

import pandas as pd
import os
import numpy as np

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)   #DataFrame 

#%%

'''
SERIES TEMPORALES EN PANDAS
'''

#Pandas tiene un gran potencial para el manejo de series temporales. 
#Es muy sencillo crear índices con fechas y frecuencias seleccionadas.
pd.date_range('20200923 14:00', periods = 6, freq = 'H')
'''
DatetimeIndex(['2020-09-23 14:00:00', '2020-09-23 15:00:00',
               '2020-09-23 16:00:00', '2020-09-23 17:00:00',
               '2020-09-23 18:00:00', '2020-09-23 19:00:00'],
              dtype='datetime64[ns]', freq='H')
'''

#Luego, podés usar esos índices junto con datos para armar series temporales o DataFrames:

pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))
'''
2020-09-23 14:00:00    1
2020-09-23 15:00:00    2
2020-09-23 16:00:00    3
2020-09-23 17:00:00    4
2020-09-23 18:00:00    5
2020-09-23 19:00:00    6
Freq: H, dtype: int64
'''

#%%
'''
CAMINATAS AL AZAR
'''

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

s2.plot()

# O usar una media móvil (rolling mean) para suavizar los datos:
    
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w,min_periods = 1).mean()
s3.plot()

#Podés ver ambas curvas en un mismo gráfico para ver más claramente el efecto del suavizado:
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()
'''
Fijate que los datos de la curva suavizada empiezan más tarde, 
porque al principio no hay datos sobre los cuales hacer promedio. 
El parámetro min_periods = 1 del método rolling te permite controlar esto
'''

#%%

'''
GUARDANDO DATOS
'''

# Guardar una serie o un DataFrame en el disco es algo realmente sencillo. 
# Probá, por ejemplo, el efecto del comando
s3.to_csv('caminata_apostolica.csv')

