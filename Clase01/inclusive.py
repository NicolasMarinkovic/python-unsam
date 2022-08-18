# inclusive.py
# Consinga:
# completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'. 

frase =  'todos somos, programadores'
palabras = frase.split()
i = 0
def descontruir_palabras(palabra):
    palabra.strip(',')
    if palabra[-2:] == 'os': #busco si la palabra termina en os
        palabra = palabra[:-2] + 'es'   #agrego a una nueva variable el resto de la palabra + 'es'. Porque no puedo modificar el valor de un string
    return palabra

def reemplaza_palabra(palabrasArray):
    del palabrasArray[i]
    palabrasArray.insert(i, newWord)

for palabra in palabras:
    newWord = descontruir_palabras(palabra)
    reemplaza_palabra(palabras)
    i += 1
    

print(' '.join(palabras))
