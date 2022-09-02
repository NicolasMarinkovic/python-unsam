# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:29:11 2022

@author: infolab
"""

def propagar(lista):
    '''
        Recorro la lista y saco los índices de -1
        Luego vuelvo a recorrer la lista de a partes(entre los índices del -1)
        Ahí pregunto si encuentra un 1, si es así agrego en un nuevo array los 1s o 0s y al final un -1.
    '''
    listaMenosUno = []
    newArr = []
    f = 0               # variable bandera
    s = 0
    
    #----------------------------
    # Saco los índices de -1 y le agrego la longitud de la lista al final.
    for i, currentNumber in enumerate(lista):
        if currentNumber == -1:
            listaMenosUno.append(i)
            
    listaMenosUno.append(len(lista))         
    #----------------------------
    
    #----------------------------
    for n in range(len(listaMenosUno)):
        for i in range(len(lista)):
            if n>0:                     #Sin este if no leeria si hay un 1 en la primera posición.
                i = listaMenosUno[n-1]
            while (i < listaMenosUno[n]):
                if lista[i] == 1:
                    f = 1               # Si encuentra un 1, cambio la bandera a 1. Sino seguira siendo 0.    
                i+=1
            break;                      # Utilizo break para que el programa no corra innecesariamente. Si sale del while no es necesario que siga recorriendo el array.              
        while (s < listaMenosUno[n]):
            newArr.append(f)            # Agrego f (puede ser 0 o 1) hasta el proximo indice de -1
            s += 1
        if (listaMenosUno[n] != listaMenosUno[-1]):     # Si este no se encuentra en el extremo pasado del array
            newArr.append(-1)                           # Agrego un -1 luego de agregar 1s o 0s.
        s = listaMenosUno[n]+1
        f = 0                           # Reseteo la variable bandera
    #----------------------------
    print(newArr)
    return newArr

propagar([ -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, 0])
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
propagar([ 0, 0, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ 1, 0,-1, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ 0, 1,-1, 0,0, 0, 0, 0, 0,-1, 1, 0])