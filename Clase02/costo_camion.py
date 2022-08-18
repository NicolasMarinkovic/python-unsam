# costo_camion.py
# Archivo de ejemplo
# Ejercicio de hipoteca

def costo_camion(nombre_archivo):
    import csv
    costoTotal = 0
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                costoTotal += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Los datos están incompletos. Línea: {row}")
    return costoTotal
costo = costo_camion('../Data/camion.csv')
print(f'Costo total: ${costo:.2f}')
