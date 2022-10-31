# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:56:05 2022

@author: nicol
"""

import pandas as pd

def unionDataFrames(dataFrames , especieParque: str, especieVereda = None, colsParque = None, cols = None):   
    '''
    Une dos DataFrames filtrando por una especie y por columnas.
    
    pre:
        dataFrames -> ESPERA 2
        especieParque -> OBLIGATORIA, es la especie que se desea filtrar
        especieVereda -> Opcional, en caso de que las especies en los dataset no coincidan
        colsParque -> Opcional, columnas a modificar del primer Dataset
        cols -> Opcional, columnas del segundo dataset que se usaran para modificar las del primer dataset
    
    pos: Devuelve un DataFrame con la unión de ambos datasets
    
    '''
    df_veredas = dataFrames[0]
    df_parques = dataFrames[1]
    
    
    col_parques = ['altura_tot', 'diametro','nombre_cie']
    col_general = [ 'altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
    
    if colsParque:
        col_parques = colsParque    
        
    if cols:
        col_general = cols
    
    for i,x in enumerate(col_parques):
        df_parques = df_parques.rename(columns={x: col_general[i]})
     
    df_parques_selec = df_parques[col_general].copy()
    df_veredas_selec = df_veredas[col_general].copy()
    
    if especieVereda:
        df_tipas_veredas = df_veredas_selec[df_veredas_selec['nombre_cientifico'] == especieVereda]    
    else:
        df_tipas_veredas = df_veredas_selec[df_veredas_selec['nombre_cientifico'] == especieParque]    
    df_tipas_parques = df_parques_selec[df_parques_selec['nombre_cientifico'] == especieParque]
    
    
    df_tipas_parques['ambiente'] = 'parque'
    df_tipas_veredas['ambiente'] = 'vereda'
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    return df_tipas

def armadoDataFrames(directorio,archivos):
    '''
    Crea n dataFrames dependiendo de la cantidad de archivos
    '''
    import os
    dataFrames = []
    for x in archivos:
        fname = os.path.join(directorio,x)
        dataFrames.append(pd.read_csv(fname))  #DataFrames
    return dataFrames

def plotsDataFrames(df):
    '''
    Hace los plots del dataframe.
    Necesita de la Funcion unionDataFrames
    '''
    
    df.boxplot('diametro_altura_pecho',by = 'ambiente')
    df.boxplot('altura_arbol',by = 'ambiente')

def f_principal(params):
    '''
    Funcion Principal del programa
    '''
    dataFrames = armadoDataFrames(params[1], [params[2][0],params[2][1]]) # Le paso el Directorio y los Archivos
    
    df_tipas = unionDataFrames(dataFrames,'Tipuana Tipu','Tipuana tipu')
    
    plotsDataFrames(df_tipas)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        directorio = sys.argv[1]
        archivos =  [sys.argv[2], sys.argv[3]] # Un array de archivos
    else:
        directorio = '../Data'
        archivos =  ['arbolado-publico-lineal-2017-2018.csv','arbolado-en-espacios-verdes.csv']
    f_principal([sys.argv[0],directorio,archivos])
        
        



