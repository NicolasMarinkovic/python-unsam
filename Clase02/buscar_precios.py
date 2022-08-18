# buscar_precios.py
# Archivo de ejemplo
# Ejercicio de hipoteca

def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    for line in f:
        row = line.strip("\n").split(',')
        if (row[0] == fruta.capitalize()):
            return print(f'El precio de la {fruta} es: ${row[1]}')   
    f.close()
    return print(f'{fruta} no figura en el listado de precios.')
fruta = input('Porfavor ingrese la fruta o verdura que desea consultar:\n--> ')
buscar_precio(fruta)
