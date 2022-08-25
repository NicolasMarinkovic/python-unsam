# Ejercicio 3.1: Lista de tuplas
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for n_fila, row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            try:
                falla = int(record['cajones']) * float(record['precio'])
                camion.append(record)
            except:
                print(f'Fila {n_fila}: No pude interpretar: {row}. Archivo: {nombre_archivo}')
                
    return camion
	
	
def leer_precios(nombre_archivo):
	precio = {}

	f = open(nombre_archivo, 'rt')
	rows = csv.reader(f)
	for n_fila, row in enumerate(rows, start=1):
		try:
			precio[row[0]] = float(row[1])
		except:
			print(f'Fila {n_fila}: No pude interpretar: {row}. Archivo: {nombre_archivo}')
	return precio
	f.close()

def hacer_informe(camiones,precios):
    informe = []
    
    for camion in camiones:
        for key in precios:
            if (key == camion['nombre']):
                diferencia = precios[key] - float(camion['precio'])
                s = (camion['nombre'], int(camion['cajones']),
                     float(camion['precio']), float(diferencia))
                informe.append(s)
                
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} %2s ${precio:>6.2f} {cambio:>10.2f}' % '')

camiones = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camiones, precios)
imprimir_informe(informe)
