# Los strings son "inmutables" o de sólo lectura. Una vez creados, su valor no puede ser cambiado.
# Esto implica que las operaciones y métodos que manipulan cadenas deben crear nuevas cadenas para almacenar su resultado.

# Caracteres de escape
# '\n'      Avanzar una línea
# '\r'      Retorno de carro
# '\t'      Tabulador
# '\''      Comilla literal
#
#  '\"'      Comilla doble literal
# '\\'      Barra invertida literal

a = 'Hello world'
d = a[:5]         # 'Hello'
e = a[6:]         # 'world'
f = a[3:8]        # 'lo wo'
g = a[-5:]        # 'world'

s = 'Hello'
# Test de pertenencia (in, not in)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replicación (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'

s.endswith()           # Verifica si termina con el sufijo
s.find(t)              # Primera aparición de t en s (o -1 si no está)
s.index(t)             # Primera aparición de t en s (error si no está)
s.isalpha()            # Verifica si los caracteres son alfabéticos
s.isdigit()            # Verifica si los caracteres son numéricos
s.islower()            # Verifica si los caracteres son minúsculas
s.isupper()            # Verifica si los caracteres son mayúsculas
s.join()               # Une una lista de cadenas usando s como delimitador
s.lower()              # Convertir a minúsculas
s.replace('he','asd')  # Reemplaza texto
s.split([])            # Parte la cadena en subcadenas
s.startswith()         # Verifica si comienza con un prefijo
s.strip()              # Elimina espacios en blanco al inicio o al final
s.upper()              # Convierte a mayúsculas

# F-STRINGS
# Las f-Strings son cadenas en las que ciertas expresiones son formateadas

nombre = 'Naranja'
cajones = 100
precio = 91.1
a = f'{nombre:>10s} {cajones:10d} {precio:10.2f}'
a
# '   Naranja        100      91.10'
b = f'Costo = ${cajones*precio:0.2f}'
# 'Costo = $9110.00'
