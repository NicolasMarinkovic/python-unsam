'''
    Pensá cuál es el contrato de la función.
    Agregale la documentación adecuada.
    Comentá el código si te parece que aporta.
    Detectá si hay invariantes de ciclo y comentalo al final de la función
'''

#%%
def valor_absoluto(n):
    '''
    pre: el valor ingresado debe ser un numero
    pos: devuelve su valor absoluto
    '''
    if n >= 0:
        return n
    else:
        return -n

#%%
def suma_pares(l):
    '''
    Calcula la suma de todos los valores pares de una lista.

    pre: los valores de la lista deben ser numeros enteros
    pos: devuelve la suma de los valores pares
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
# Invariantes -> res acumula la suma de las pares

#%%
def veces(a, b):
    '''
    Suma (a), (b) cantidad de veces
    
    pre: b debe ser un numero entero
    pos: devuelve la multiplicacion de (a) por (b)
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
# Invariantes -> res acumula las veces y no puede ser menor a 0,nb no debe ser menor o igual 0

#%%
def collatz(n):
    '''
    Itera con un elemento hasta que su divisíon entera de 1.

    pre: el elemento debe ser un numero entero
    pos: devuelve la cantidad de veces que itera el ciclo
    '''
    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
# Invariantes -> res debe ser mayor o igual a 1

