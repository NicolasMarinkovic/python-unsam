# diccionario_geringoso.py
# Archivo de ejemplo
# Ejercicio de hipoteca

def geringoso(lista):
    capadepenapa = ''
    s = {}
    for cadena in lista:
        for c in cadena:
            capadepenapa += c
            if c == 'a' or c =='A':
                capadepenapa += 'pa'
            elif c == 'e' or c =='E':
                capadepenapa += 'pe'
            elif c == 'i' or c =='I':
                capadepenapa += 'pi'
            elif c == 'o' or c =='O':
                capadepenapa += 'po'
            elif c == 'u' or c =='U': 
                capadepenapa += 'pu'
        s[cadena] = capadepenapa
        capadepenapa = ''
    return s
    
diccionario_geringoso = geringoso(['banana', 'manzana', 'mandarina'])
print(diccionario_geringoso)

'''
Construí una función que, a partir de una lista de palabras, 
devuelva un diccionario geringoso. Las claves del diccionario
deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso 
(como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 
Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.
'''