# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:24:47 2022

@author: nicol
"""

import numpy as np
import matplotlib.pyplot as plt

#%%

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=100)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.
    
plotear_temperaturas()