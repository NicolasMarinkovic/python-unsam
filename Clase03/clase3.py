#Búsquedas en un diccionario

#Podés verificar si una clave existe:
d = {}
if key in d:
    # YES
else:
    # NO
    
#Claves compuestas

#Casi cualquier valor puede usarse como clave en un diccionario de Python. La principal restricción es que una clave debe ser de tipo inmutable. Por ejemplo, tuplas:

feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}

#Conjuntos

#Un conjunto es una colección de elementos únicos sin orden y sin repetición.

citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])

#Los conjuntos también son útiles para eliminar duplicados.

nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']

unicos = set(nombres)
# unicos = {'Manzana', 'Banana', 'Naranja', 'Pera'}

#Más operaciones en conjuntos:

citricos.add('Banana')        # Agregar un elemento
citricos.remove('Limon')    # Eliminar un elemento

A | B                 # Unión de conjuntos A y B
A & B                 # Intersección de conjuntos
A - B                 # Diferencia de conjuntos
