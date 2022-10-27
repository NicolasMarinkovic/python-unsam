# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:23:16 2022

@author: Nicolas
"""
#%%  Ejercicio 9.2: Caminatas al azar
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 3x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la quinta figura si fuera una grilla regular de 3x3
plt.plot([0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la sexta figura si fuera una grilla regular de 3x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])


plt.show()

#%%