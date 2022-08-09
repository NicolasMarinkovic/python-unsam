#Con estos comandos podés abrir dos archivos, una para lectura y otro para escritura:
f = open('foo.txt', 'rt')     # Abrir para lectura ('r' de read, 't' de text)
g = open('bar.txt', 'wt')     # Abrir para escritura ('w' de write, 't' de text)

#Para leer el archivo completo, o una parte:
data = f.read()
#Leer 'maxbytes' bytes
maxbytes = 255
data = f.read([maxbytes])

#Para escribir un texto en el archivo:
g.write('un texto')

#Finalmente, hay que cerrar los archivos cuando terminamos de usarlos.
f.close()
g.close()

#Preferimos abrir los archivos con el comando with de la siguiente forma, ya que este se cierra solo
with open('nombre_archivo', 'rt', encoding='utf8') as file:
    # Usá el archivo `file`
    '...comandos que usan el archivo'
    # No hace falta cerrarlo explícitamente
'...comandos que no usan el archivo'
#Esto cierra automáticamente el archivo cuando se termina de ejecutar el bloque indentado.


# Comandos usuales para leer un archivo
# Para leer un archivo entero, todo de una, como cadena:

with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` es una cadena con *todo* el texto en `foo.txt`

# Leer un archivo entero y cargarlo en memoria todo de una vez parece simple, pero sólo tiene ventajas si el archivo es pequeño. 
# Si estás trabajando con archivos enormes es mejor procesar las líneas de tu archivo una a una.

#Para leer línea por línea iterativamente:
with open('nombre_archivo', 'rt') as file:
    for line in file:
        # Procesar la línea
        print(line, end = '')

# El comando next() devuelve la siguiente línea de texto en el archivo, por ejemplo para no leer encabezados
f = open('../Data/camion.csv', 'rt')
headers = next(f)

for line in f:
    row = line.split(',')
    print(row)
    #['"Lima"', '100', '32.20\n']
    #['"Naranja"', '50', '91.10\n']
    #...

f.close()


# Comandos usuales para escribir un archivo
# Para escribir cadenas:
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...

# También podés simplemente redireccionar la salida del print (de la pantalla a un archivo).
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...


# ARCHIVOS COMPRIMIDOS
# Hay un módulo de la biblioteca de Python llamado gzip que lee archivos comprimidos.

import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
# nombre,cajones,precio
# Lima,100,32.
# Naranja,50,91.1
# Caqui,150,103.44
# Mandarina,200,51.23
# Durazno,95,40.37
# Mandarina,50,65.1
# Naranja,100,70.44