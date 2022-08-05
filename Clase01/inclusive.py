# inclusive.py
# Consinga:
# completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'. 

frase = 'todos somos programadores'
palabras = frase.split()
for palabra in palabras:
    if palabra[-1] == 's' and palabra[-2] == 'o':
        palabra.replace('o','e')
        print("Hola")
    frase_t = ' '.join(palabras)
    print(frase_t)
'todes somes programadores'
