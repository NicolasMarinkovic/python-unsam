# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:23:16 2022

@author: Nicolas
"""
import matplotlib.pyplot as plt
import numpy as np

#%%  Ejercicio 9.2: Caminatas al azar

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

#%% Ejercicio 9.3: Gráficos de barras
n = 12 
X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va='bottom')

for x, y in zip(X, -Y2):
    plt.text(x + 0.4, y + 0.00001, '%.2f' % y, ha='right', va='top')
    
plt.ylim(-1.25, +1.25)

plt.show()

#%% Ejercicio 9.4: Coordenadas polares

plt.axes([0, 0, 1, 1],polar=True)

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)


#%% Ejercicio 9.5: Setear el color de un scatter plot
import math as math

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

A = dict(zip(X,Y))
colors = []

for x in A.keys():
    if x > 0 and A[x] > 0:
        colors.append('Blue')
    if x > 0 and A[x] < 0:
        colors.append('Red')
    if x < 0 and A[x] > 0:
        colors.append('Green')
    if x < 0 and A[x] < 0:
        colors.append('Purple')

plt.scatter(X,Y, c=colors, alpha=0.5)
plt.xticks([]), plt.yticks([])

plt.show()
#%%

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()





