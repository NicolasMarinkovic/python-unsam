# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:18:21 2022

@author: nicol
"""
#%%
import datetime

'''
En Python podemos usar la función dir() para obtener una lista de todos los atributos de un módulo.
'''
print(dir(datetime))

'''
    ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
     '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round',
     'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
'''
# Más conocidos
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#%%

# Usamos el método now() de la clase datetime del módulo (con el mismo nombre) para crear el objeto fecha_hora que va a contener la fecha y la hora actuales.
fecha_hora = datetime.now()
# 2022-11-02 18:25:45.076670

# Podemos obtener solo la fecha:
fecha = date.today()
# 2022-11-02

# Podés generar objetos de tipo fecha con la clase date. Tres argumentos: año, mes y día.
d = date(2019, 4, 13)
# 2019-04-13

# Así podés obtener el año, el mes, el día y el día de la semana:
hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes

#%%
'''
        TIMESTAMP
'''
# En los sistemas operativos derivados de Unix (Mac OS X, Linux, etc.) se toma como medida de tiempo el número de segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar. 
# Se lo conoce como Unix timestamp.  Podés convertir un timestamp a fecha usando el método fromtimestamp().
# Esto es importante porque las fechas de modificación de los archivos usan timestamps por ejemplo.

timestamp = date.fromtimestamp(1326244364)
print('Fecha =', timestamp)
#Fecha = 2012-01-10

#%%
'''
    STRFTIME()   &&     STRPTIME()
'''
# El método strftime() está definido en las clases date, datetime y time

now = datetime.now()

t = now.strftime('%H:%M:%S') # %Y, %m, %d, %H etc. son códigos de formato
print('hora:', t)
# hora: 14:40:06

s1 = now.strftime('%m/%d/%Y, %H:%M:%S') # en formato mm/dd/YY H:M:S
print('s1:', s1)
# s1: 09/24/2020, 14:40:06


s2 = now.strftime('%d/%m/%Y, %H:%M:%S') # en formato dd/mm/YY H:M:S
print('s2:', s2)
# s2: 24/09/2020, 14:40:06

'''
%Y - año [0001,..., 2018, 2019,..., 9999]
%m - mes [01, 02, ..., 11, 12]
%d - día [01, 02, ..., 30, 31]
%H - hora [00, 01, ..., 22, 23
%M - minuto [00, 01, ..., 58, 59]
%S - segundo [00, 01, ..., 58, 59]
'''

# El método STRPTIME() crea un objeto datetime a partir de una cadena.

cadena_con_fecha= '21 September, 2021'
date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object =', date_object)
# date_object = 2021-09-21 00:00:00

'''
El método strptime() toma dos argumentos:

una cadena que representa una fecha y hora
un código de formato correspondiente al primer argumento

Los códigos de formato %d, %B, %Y significan day, month (full name) y year respectivamente.
'''

