def costo_camion(nombre_archivo):
	import csv
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
	return costoTotal
costo= costo_camion('./Ejercicios/ejercicios_python/Data/fecha_camion.csv')
print(f'Costo total: ${costo:.2f}')
