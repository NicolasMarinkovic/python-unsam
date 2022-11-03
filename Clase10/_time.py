# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:38:31 2022

@author: nicol
"""
#%%

'''
 TIME
'''
from datetime import time

a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)
# a = 00:00:00

b = time(11, 34, 56)
print('b =', b)
# b = 11:34:56

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)
# c = 11:34:56

d = time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
print('d =', d)
# d = 11:34:56.234566

# Una vez que creaste un objeto time, podés extraer sus atributos así:
a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)

#%%

'''
 DATETIME
'''

# El módulo datetime tiene una clase con su mismo nombre que permite almacenar información de fecha y hora en un solo objeto.

from datetime import datetime

# datetime(year, month, day)
a = datetime(2020, 4, 21)
# 2020-04-21 00:00:00

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2021, 4, 21, 6, 53, 31, 342260)
# 2021-04-21 06:53:31.342260

print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())

#%%
'''
    TIMEDELTA
'''

# Un objeto timedelta representa una duración, es decir, la diferencia entre dos instantes de tiempo.
from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)

t3 = t1 - t2 
# 241 days, 0:00:00

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minutejm = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)

t6 = t4 - t5 
# -333 days, 1:14:20

print('tipo de t3 =', type(t3))
# tipo de t3 = <class 'datetime.timedelta'>

print('tipo de t6 =', type(t6))
# tipo de t6 = <class 'datetime.timedelta'>

'''
Diferencia entre objetos timedelta
'''
from datetime import timedelta

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2 # <class 'datetime.timedelta'>
# 2 days, 13:55:39
print(abs(t3))
# days=2, seconds=50139

# total_seconds() obtiene el tiempo medido en segundos
t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())
# segundos totales = 93630.1





















