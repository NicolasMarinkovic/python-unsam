# Ejercicio 3.1: Lista de tuplas
import csv

def leer_camion(nombre_archivo):
    camion = []
    costoTotal = 0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for n_fila, row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            try:
                costoTotal += int(record['cajones']) * float(record['precio'])
                camion.append(record)
            except:
                print(f'Fila {n_fila}: No pude interpretar: {row}')
                
    return camion
	
	
def leer_precios(nombre_archivo):
	precio = {}

	f = open(nombre_archivo, 'rt')
	rows = csv.reader(f)
	for n_fila, row in enumerate(rows, start=1):
		try:
			precio[row[0]] = float(row[1])
		except:
			print(f'Fila {n_fila}: No pude interpretar: {row}')
	return precio
	f.close()

def balance_total():
    costo_camion = 0.0
    precio_recaudado = 0.0
    
    for camion in camiones:
        costo_camion +=  int(camion['cajones']) * float(camion['precio'])
        for key in precios:
            if (key == camion['nombre']):
                precio_recaudado += precios[key] * int(camion['cajones'])
				
    diferencia = precio_recaudado - costo_camion
    print(f'El costo total del camión es: ${costo_camion}.\nLo que se recaudó con la venta fue: ${precio_recaudado}.')
    if (diferencia > 0):
        print(f'La ganancia es de ${diferencia:.2f}.')
    else:
        print(f'La pérdida es de ${diferencia * -1:.2f}.')

camiones = leer_camion('../Data/missing.csv')
precios = leer_precios('../Data/precios.csv')
balance_total()

