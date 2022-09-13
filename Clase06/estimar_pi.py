# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:32:36 2022

@author: nicol
"""
import random

#%%
def generar_punto():
    x = random.random()
    y = random.random()
    if pow(x,2) + pow(y,2) < 1:
        return True
    return False
    
#%%
N = 10000
G = sum([generar_punto() for i in range(N)])
pi = 4*G/(N)
print(pi)