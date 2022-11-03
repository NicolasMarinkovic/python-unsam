# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:38:09 2022

@author: nicol
"""

from datetime import timedelta , date

def dias_hasta_primavera() -> str:
    '''
    Calcula cuántos días faltan para primavera
    '''
    
    hoy = date.today()
    prim_inicio = date(hoy.year ,9 ,21)
    prim_fin = date(hoy.year, 12, 21)
    
    mensaje = 'Aún faltan'
    
    if (hoy >= prim_fin):
        '''
        Si terminó primavera y aún no cambio de año debe calcular cuánto falta
        para la primavera del año siguiente.
        '''
        prim_inicio = date(hoy.year+1 , 12, 21)
    
    dias_hasta = prim_inicio - hoy
    
    if (hoy >= prim_inicio and hoy < prim_fin):
        dias_hasta = prim_fin - hoy
        mensaje = 'Es primavera! Aún quedan'
    
    return f'{mensaje} {dias_hasta} '

def reincorporacion(days, comienzoLicencia):
    '''
    Le suma n dias a una fecha.
    
    pre: days -> puede ser cualquier valor entero
         comienzoLicencia -> debe ser date o timedate
    '''

    return comienzoLicencia + timedelta(days)
    
print(reincorporacion(200, date(2020,9,26)))

print(dias_hasta_primavera())