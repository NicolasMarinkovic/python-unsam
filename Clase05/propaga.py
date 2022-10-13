# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:29:11 2022

@author: infolab
"""
# %%
def propagar(lista):
    '''
        Recorro la lista y saco los índices de -1
        Luego vuelvo a recorrer la lista de a partes(entre los índices del -1)
        Ahí pregunto si encuentra un 1, si es así agrego en un nuevo array los 1s o 0s y al final un -1.
    '''
    listaMenosUno = []
    newArr = []
    valor = 0               # De esto dependera si se agrega 1s o 0s
    s = 0
    
    # Saco los índices de -1 y le agrego la longitud de la lista al final.
    for i, currentNumber in enumerate(lista):
        if currentNumber == -1:
            listaMenosUno.append(i)
            
    listaMenosUno.append(len(lista))         # Agrego el indice de la lista para ponerle fin al siguiente ciclo
    
    for n, indexMenosUno in enumerate(listaMenosUno):
        for i in range(len(lista)):
            if n>0:                     # Sin este if no leeria si hay un 1 en la primera posición.
                i = s                   # S es el índice de la lista que está recorriendo. Para cada vez que encuentra el -1.
            while (i < indexMenosUno):
                if lista[i] == 1:
                    modif = 1               # Si encuentra un 1, cambio la modif a 1. Porque debera insertar todos 1.
                i+=1
            break;                      # Utilizo break para que el programa no corra innecesariamente. Si sale del while no es necesario que siga recorriendo el array.
            
        while (s < indexMenosUno):
            newArr.append(modif)            # Agrego el valor (puede ser 0 o 1 depende de modif) hasta que encuentre -1
            s += 1
            
        if (indexMenosUno != listaMenosUno[-1]):     # Si este no se encuentra en el extremo pasado del array
            newArr.append(-1)                        # Agrego un -1 luego de agregar 1s o 0s.
            
        s = indexMenosUno+1                 # Declaro s con el proximo valor a comparar
        modif = 0                           # Reseteo el valor a 0. Cambiará si encuentra un 1 entre este índice de -1 y el siguiente.
    #----------------------------
    print(newArr)
    return newArr

propagar([ -1, 0, -1, 0, -1, 1, -1, 0, -1, 1, 0])
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
propagar([ 0, 0, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ 1, 0,-1, 0,0, 0, 0, 0, 0,-1, 1, 0])
propagar([ -1, -1,-1, -1,0, -1, 1, 0, -1,-1, 1, 1])