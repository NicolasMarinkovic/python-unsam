# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:09:09 2022

@author: nicol
"""
#%%
with open('../Data/camion.csv', 'rt') as file:
    headers = next(file)
    for line in file:
        print(line, end = '')