# Se ven detalles técnicos sobre cómo hacer que la salida por pantalla sea más amena para el usuario

# Códigos de formato

#Lo códigos de formato (lo que va luego de : dentro de {}) son similares a

#d       Entero decimal
#b       Entero binario
#x       Entero hexadecimal
#f       Flotante como [-]m.dddddd
#e       Flotante como [-]m.dddddde+-xx
#g       Flotante, pero con uso selectivo de la notación exponencial E.
#s       Cadenas
#c       Caracter (a partir de un entero, su código)


#:>10d   Entero alineado a la derecha en un campo de 10 caracteres
#:<10d   Entero alineado a la izquierda en un campo de 10 caracteres
#:^10d   Entero centrado en un campo de 10 caracteres
#:0.2f   Flotante con dos dígitos de precisión

nombre = 'Naranja'
cajones = 100
precio = 91.1
f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}'
'''   Naranja        100      91.10'''
f'{nombre:<10s} {cajones:<10d} {precio:>10.2f}'
'''Naranja    100             91.10'''

value = 42863.1
print(f'{value:*>16,.2f}')
#*******42,863.10

# -------------------------------------------------
# Formato a diccionarios

# Podés usar el método format_map() para aplicarle un formato a los valores de un diccionario:
s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}

print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s))
#'       Naranja        100      91.10'

# -------------------------------------------------
# Tambien existe el estilo tipo .format() pero es horrible.
#Formato estilo C

#También podés usar el operador %.

'The value is %d' % 3
#'The value is 3'
'%5d %-5d %10d' % (3,4,5)
#'    3 4              5'
'%0.2f' % (3.1415926,)
#'3.14'

# Tiene la dificultad de que hay que contar posiciones y todas las variables van juntas al final.

# -----------------------------------------------

#EL formato en cadenas se puede simplemente asignar a una variable.

f = '%0.4f' % value
f
#'42863.1000'





