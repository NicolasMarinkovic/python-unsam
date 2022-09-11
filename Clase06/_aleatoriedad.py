# VALORES DISCRETOS
# randint genera números enteros aleatorios entre dos extremos. 

import random

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) # devuelve un entero aleatorio entre 1 y 6

print(tirada)

#%%
# Si fijamos una semilla con el comando random.seed(semilla), donde semilla es un número entero, la secuencia de números aleatorios que obtengamos será reproducible utilizando la misma semilla.
# SEMILLAS
random.seed(31415)
tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) # devuelve un entero aleatorio entre 1 y 6

print(tirada)

#%%
# ELECCIONES CON REPOSICIÓN
# La función random.choice() toma una secuencia y devuelve un elemento aleatorio.

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

# Si queremos realizar múltiples elecciones aleatorias de la lista podemos usar la función random.choices()
print(random.choices(caras,k=5))

#%%
# ELECCIONES SIN REPOSICIÓN
# No repite el mismo valor más de una vez
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

random.sample(naipes,k=3)
# la variable k no puede ser mayor que la cantidad de naipes (es decir 40) ya que no se puede sacar sin reposición más elementos que la cantidad total.

#%%
# MEZCLAR
# la función shuffle 'mezcla' la lista
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.shuffle(naipes)
print(naipes)

# Podemos consultar las tres cartas que quedaron al final:
naipes[-3:]

# O directamente sacarlas del mazo:
n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')


#%%
# Valores continuos
# La funcion random.random() genera un número de punto flotante entre 0 y 1.
x = random.random()
print(x)
