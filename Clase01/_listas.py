nombres = [ 'Rosita', 'Manuel', 'Luciana' ]
nums = [ 39, 38, 42, 65, 111]

line = 'Pera,100,490.10'
row = line.split(',') #la coma indica el elemento que separa
# ['Pera', '100', '490.10']
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
a = ','.join(line)

# Las listas pueden almacenar elementos de cualquier tipo. Podés agregar nuevos elementos usando append():
nombres.append('Mauro')     # Lo agrega al final

# Usá el símbolo de adición + para concatenar listas:
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
# Se puede replicar una lista (s * n).
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Y podés insertar elementos en una posición. Acordate que los índices comienzan a contar desde el 0.
nombres.insert(2, 'Iratxe') # Lo inserta en la posición 2. 
nombres.insert(0, 'Iratxe') # Lo inserta como primer elemento. 

# La función len permite obtener la longitud de una lista.
nombres = ['Rosita','Manuel','Luciana']
len(nombres)  # 3

# Borrar elementos: 
# Usando el valor
nombres.remove('Luciana')
# Usando la posición
del nombres[1]


#Ordenar una lista
# Las listas pueden ser ordenadas "in-place", es decir, sin usar nuevas variables.
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Orden inverso
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Funciona con cualquier tipo de datos que tengan orden
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']

t = sorted(s)               # s queda igual, t guarda los valores ordenados

# Slices
lista_frutas = ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Sandía', 'Pera']
lista_frutas[0:3]
# ['Frambuesa', 'Manzana', 'Granada']
lista_frutas[-2:]
# ['Sandía', 'Pera']
