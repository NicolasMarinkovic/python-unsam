#Python tiene tres tipos de datos que son secuencias.
# String - Listas - Tupla

# Las secuencias pueden ser replicadas: s * n.
a = 'Hello'
a * 3
#'HelloHelloHello'
b = [1, 2, 3]
b * 2
#[1, 2, 3, 1, 2, 3]

#Las secuencias del mismo tipo pueden ser concatenadas: s + t.
a = (1, 2, 3)
b = (4, 5)
a + b
#(1, 2, 3, 4, 5)
c = [1, 5]
a + c
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: can only concatenate tuple (not "list") to tuple

# ----------------------------------------------------------

# Rebanadas (SLICE)
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]

#En listas, una rebanada puede ser reasignada o eliminada.
# Reasignación
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]

#--------------------------------------------------
#				ACCIONES EN SECUENCIAS
# Reducciones de secuencias con funciones
s = [1, 2, 3, 4]
sum(s)	#10
min(s)	#1
max(s)	#4

# Iterar sobre una secuencia
for i in s:
	print(i)


# 		BREAK
#Podés usar el comando break para romper un ciclo antes de tiempo.
for name in namelist:
    if name == 'Juana':
        break
#Cuando el comando break se ejecuta, sale del ciclo y se mueve a las siguientes instrucciones.


# 		CONTINUE
#Para saltear un elemento y moverse al siguiente, usá el comando continue.
for line in lines:
    if line == '\n':    # Salteo las instrucciones que procesan líneas
        continue
    # Instrucciones que procesan líneas
#Éste es útil cuando el elemento encontrado no es de interés o es necesario ignorarlo en el procesamiento.

# ---------------------------------------------------------
# 			FUNCIONES
# range(). Sirve para iterar sobre un rango de números enteros,

for i in range(100):
    # i = 0,1,...,99
# La sintaxis es range([comienzo,] fin [,paso])
for k in range(10,50,2):
    # k = 10,12,...,48
    # Observá que va de a dos.
for n in range(10,0,-1):       # Contar 10 ... 1
        print(n, end=' ')


# enumerate()
# enumerate(secuencia [, start = 0]) (start es opcional)
with open(nombre_archivo) as f:
    for nlinea, line in enumerate(f, start=1):
    # nlinea = 1, line = 'blabla'
    # nlinea = 2, line = 'blablab'
    # nlinea = 3, line = 'blablabla'
    # No crea un diccionario sino nombre suplanta al nombres[i]

# zip(). Toma múltiples secuencias y las combina en un iterador.

columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
# ('nombre','Pera'), ('cajones',100), ('precio',490.1)
# Un uso frecuente de zip es para crear pares clave/valor y construir diccionarios.

d = dict(zip(columnas, valores))

# items(),Es para diccionarios ,obtenés pares (clave,valor):
precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
    
precios.items()

#dict_items([('Pera', 490.1), ('Lima', 23.45), ('Naranja', 91.1), ('Mandarina', 34.23)])

# por si necesita(valor,clave)
lista_precios = list(zip(precios.values(),precios.keys()))
# [(490.1, 'Pera'), (23.45, 'Lima'), (91.1, 'Naranja'), (34.23, 'Mandarina')]

min(lista_precios)
#(23.45, 'Lima')
max(lista_precios)
#(490.1, 'Pera')
sorted(lista_precios)
#[(23.45, 'Lima'), (34.23, 'Mandarina'), (91.1, 'Naranja'), (490.1, 'Pera')]















