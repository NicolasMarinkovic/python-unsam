import random
from collections import Counter

######
# La función devuelve 5 números al azar entre el 1 y el 6
def tirar(N):
	tirada=[]
	for i in range(N):
		tirada.append(random.randint(1,6))
	return tirada
	
######
# Verifica si los 5 números son iguales, por lo que sería generala
def es_generala(tirada):
	if len(tirada) == 5:
		boo = True
		for n,i in enumerate(tirada):
			if i > 0:
				if i != tirada[n-1]:
					boo = False
		return boo
	else:
		return False

######
# Devuelve la mayor cantidad de un número, en caso de igualdad, yo decidí tomar el primero que venga
def mayorCantidad(tirada):
    conteo=Counter(tirada)
    maximo = [(key,value) for key,value in conteo.items() if value == max(conteo.values())]
    
    ### ITEM EXTRA
    maximo = maximo[0]
    while maximo[1] == 1:
        maximo = mayorCantidad(tirar(5))
    ### ITEM EXTRA
    
    return maximo

######
# Agrega a un nuevo array los mayores valores de la primer tirada
def agregarTirada(tiradaFinal,mayorCantidad):
	[tiradaFinal.append(mayorCantidad[0]) for i in range(mayorCantidad[1])]
		
	return tiradaFinal

######
# El segundo y tercer tiro, pregunta si esta tirada contiene el mayor valor antes mencionado.
def nuevoTiro(tiradaFinal):
	[tiradaFinal.append(r) for r in tirar(5-len(tiradaFinal)) if r == tiradaFinal[0] ]

	return tiradaFinal

######
# Función general que integra todo
def prob_generala():
		tirada = tirar(5)
		tiradaFinal = []

		agregarTirada(tiradaFinal,mayorCantidad(tirada))
		nuevoTiro(tiradaFinal)
		nuevoTiro(tiradaFinal)
		
		return es_generala(tiradaFinal)
	

N = 10000
G = sum([prob_generala() for i in range(N)])
prob = G/(N*3) # multiplico por 3 porque siempre hago 3 tiradas.
print(f'Tiré {N*3} veces, de las cuales {G} logré sacar generalas.')
print(f'Podemos estimar la probabilidad de sacar generala en 3 turnos mediante {prob:.6f}.')


