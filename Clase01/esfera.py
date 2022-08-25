# esfera.py
# Archivo de ejemplo
# Consigna:

# En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida a 
# le usuarie que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. 
# Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3.

import math
radio = input("Ingresa el radio de la esfera: ")

volumen = 4/3 * math.pi * (int(radio) ** 3)
print(round(volumen))
