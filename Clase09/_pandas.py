# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:06:23 2022

@author: nicol
"""

import pandas as pd
import os
#%%
directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)   #DataFrame 


df.head()
#df.head(n) podés ver las primeras líneas de datos. 
df.tail(5)
#df.tail(n) verás las últimas n líneas de datos.
df.columns
#df.columns pandas te va a devolver un índice con los nombres de las columnas del DataFrame.
df.index
#df.index te mostrará el índice. En este caso el índice es numérico y se corresponde con el número de la línea leída del archivo.
df[['altura_tot', 'diametro', 'inclinacio']].describe()
#df.describe(). Para ver mejor una parte, podemos seleccionar algunas columnas de interés antes de pedirle la descripción.

#%%
'''
SELECCION
'''

df['nombre_com']
#df['nombre_com'] veremos la columna (que es una serie) de nombres comunes de los árboles en la base
df['nombre_com'].unique()
# Podemos usar unique para ver una vez cada nombre:
 
df['nombre_com'] == 'Ombú'
#Retornara true or false por todas las filas
(df['nombre_com'] == 'Ombú').sum()
#Suma los TRUE
cant_ejemplares = df['nombre_com'].value_counts()
#Suma los true pero para todos los nombres


#%%
'''
SELECCIÓN DE UNA COLUMNA
'''
# Recordemos que al tomar una sola columna obtenemos una serie en lugar de un DataFrame:
df_jacarandas_diam = df[df['nombre_com'] == 'Jacarandá']['diametro']



#%%
'''
FILTROS BOOLEANOS
'''
# La serie booleana que obtuvimos con df['nombre_com'] == 'Ombú' puede 
# usarse para seleccionar esas filas del DataFrame. Probemos con Jacarandá:

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
# Filtramos solo las líneas que tengan de nombre común Jacarandá

# Si vas a querer modificar df_jacarandas es conveniente crear una copia 
# de los datos de df en lugar de simplemente una vista. Esto se puede hacer 
# con el método copy() como en el siguiente ejemplo.
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()    

#%%

'''
FILTROS POR ÍNDICE Y POR POSICIÓN
'''
#Podemos acceder a una fila de un DataFarme o una Serie tanto a través de su posición como a través de su índice. 
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.index

#Para acceder con el índice usá loc[]
df.loc[165]
cant_ejemplares.loc['Eucalipto']

#Para acceder por número de posición usá iloc, como se muestra a continuación.
#Observá que esto nos devuelve los datos de la primera fila de df_jacarandas que corresponde al índice 165 
df_jacarandas.iloc[0]
'''
altura_tot     5
diametro      10
inclinacio     0
Name: 165, dtype: int64
'''
# Slices
cant_ejemplares.iloc[0:3]
#Podemos seleccionar tanto filas como columnas, si separamos con comas las respectivas selecciones:
df_jacarandas.iloc[-5:,2]
'''
51104     4
51172     8
51180     0
51207     0
51375    20
Name: inclinacio, dtype: int64
'''

#%%
'''
SCATTERPLOTS
'''

df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')
#Hay otro módulo para hacer gráficos que interactúa muy bien con pandas y se llama Seaborn
# "usar pandas para manejar los datos y seaborn para visualizarlos, es la posta"
import seaborn as sns

sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')



