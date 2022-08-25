import sys
import csv

def costo_camion(nombre_archivo):
    costoTotal=0
    with open(nombre_archivo, 'rt') as file:
        rows=csv.reader(file)
        encabezados = next(rows)
        for n_fila, row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            try:
                costoTotal += int(record['cajones']) * float(record['precio'])
            except:
                print(f'Fila {n_fila}: No pude interpretar: {row}')
    print(f'Costo total: ${costoTotal:.2f}')

if(len(sys.argv) > 2):
    costo_camion(sys.argv[1])
else:
    costo_camion('../Data/fecha_camion.csv')

