# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:08:44 2022

@author: Nicolas
"""
import sys

def tablamult(n):
    # Titulo
    print('%5s' %'', end='')
    for i in range(n+1):        # Hago +1 para que muestre los valores buscados. Sino mostraria uno menos.
        print('%4d' % i, end='')
    print('\n-----',end='')
    for i in range(n+1):
        print('----',end='')    # Es para que las lineas del titulo se adapten al valor. Proba con 18 o 5 por ej
    print(end='\n')
    # Titulo
    
    # Calculo
    for i in range(1,n+2):                  # hago n+2 porque tenia problemas que en el siguiente range() el indice no podia ser 0
        print(f'{i-1:>2d}: %1s' %'',end='') # Imprimo el i por linea. Ej 1: 2: 3: 4:
        print('%4d' %0 ,end = '')           # Esto es una truchada, creo yo que hay mejores formas pero no se me ocurrio.
        
        for r in range(0, n*i ,i):
            i -= 1                          # resto lo que antes le sume, ya que i no podia ser 0 antes pero ahora si necesito que sea 0
            print('%4d' %(i + r),end = '')
        print(end='\n')
    # Calculo
    
    
if(len(sys.argv) >= 2):
    tablamult(int(sys.argv[1]))
else:
    tablamult(9)