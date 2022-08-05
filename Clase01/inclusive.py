# inclusive.py
# Consinga:
# completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'. 

frase =  'todos somos programadores'
palabras = frase.split()
i = 0
for palabra in palabras:
    if palabra[-2:] == 'os': #busco si la palabra termina en os
        newWord = palabra[:-2] + 'es'   #agrego a una nueva variable el resto de la palabra + 'es'. Porque no puedo modificar el valor de un string
        del palabras[i]
        palabras.insert(i, newWord)
    i += 1

print(' '.join(palabras))
