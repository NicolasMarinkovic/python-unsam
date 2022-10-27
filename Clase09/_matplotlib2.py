# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:51:23 2022

@author: Nicolas
"""

# FIGURAS, SUBPLOTS, EJES Y MARCAS (TICKS)

'''
Es bueno saber que al invocar plot() matplotlib llama a gca() (get current axes) 
para obtener acceso a los ejes, y gca() a su vez llama a gcf() (get current figure) 
para obtener acceso a la figura. Si no existe tal figura, llama a figure() para crearla 
o más estrictamente hablando, para crear un un único subplot (el número 1 en una grilla de 1x1)
'''

'''
Argumento	Por Omisión	            Descripción
num	           1	            número de figura
figsize	    figure.figsize	    tamaño de figura en pulgadas (ancho, alto)
dpi	        figure.dpi	        resolución en puntos por pulgada
facecolor	figure.facecolor	color del fondo
edgecolor	figure.edgecolor	color del borde rodeando el fondo
frameon	     True	            dibujar un recuadro para la figura ?
'''

# SUBPLOTS
# Podés disponer tus plots en una grilla de intervalos regulares si usás subplots. 
# Sólo tenés que especificar el número de filas, el de columnas y finalmente el 
# número de subplot para activar el subplot correspondiente.

# sublot(fila,columna,nroSubplot)
# subplot(1,2,1) --- subplot(1,2,2)

# EJES
# Podés usar los ejes para ubicar los plots en cualquier lugar de la figura. 
# Si queremos poner un pequeño gráfico como inserto en uno más grande, 
# lo podemos hacer moviendo sus ejes.

# axes([0.1, 0.1, 0.8, 0.8])   ---   axes([0.2, 0.2, 0.3, 0.3])





















