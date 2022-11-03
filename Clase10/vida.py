# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:10:12 2022

@author: nicol
"""
from datetime import datetime

def vida_en_segundos(fecha_nac):
    fecha_act = datetime.now()
    
    date_object = datetime.strptime(fecha_nac, '%d/%m/%Y')
    # La mayuscula es para cuando su formato es YYYY, minuscula para cuando es YY
    
    dias_vividos = fecha_act - date_object
    
    return dias_vividos.total_seconds()


vida_en_segundos('08/03/2001')