# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:29:11 2022

@author: infolab
"""

def propagar(lista):
    '''
        Si el algoritmo encuentra 1 agrega 1 a una nueva lista
        hasta encontrar un -1
    '''
    listaMenosUno = []
    newArr = []
    f = 0               # variable bandera
    s = 0
    
    ########################## SACO EL INDICES DE LOS -1 y le agrego el fin de la lista al final.
    for i, currentNumber in enumerate(lista):
        if currentNumber == -1:
            listaMenosUno.append(i)
            
    listaMenosUno.append(len(lista))         
    ##########################
    
    for n in range(len(listaMenosUno)):
        for i, currentNumber in enumerate(lista):
            while (i < listaMenosUno[n]):
                if currentNumber == 1:
                    f = 1      # Si encuentra un 1, cambio la bandera a 1. Sino seguira siendo 0.    
                i+=1
        while (s < listaMenosUno[n]):
            newArr.append(f)            # Agrego f (puede ser 0 o 1) hasta el proximo indice de -1
            s += 1
        if (listaMenosUno[n] != listaMenosUno[-1]):     # Luego agrego un -1 si este no se encuentra en el extremo pasado del array
            newArr.append(-1)
        s = listaMenosUno[n]+1
        f = 0                           # Reseteo la variable
        
    print(newArr)
                
    return newArr

propagar([ -1, 0, -1,0, -1, 1, -1, 0,-1, 1, 0])
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
propagar([ 0, 0, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ 1, 0,-1, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ 0, 1,-1, 0,0, 0, 0, 0, 0,-1, 1, 0])