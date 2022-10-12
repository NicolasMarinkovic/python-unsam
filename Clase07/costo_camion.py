import sys
import csv
from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    costoTotal=0
    camiones = leer_camion(nombre_archivo,types=[str,str,str,int,float])
    for n_fila, fila in enumerate(camiones, start=1):
        try:
            costoTotal += fila['cajones'] * fila['precio']
        except:
            print(f'Fila {n_fila}: No pude interpretar: {nombre_archivo}')
    print(f'Costo total: ${costoTotal:.2f}')


if(len(sys.argv) > 2):
    costo_camion(sys.argv[1])
else:
    costo_camion('../Data/fecha_camion.csv')
