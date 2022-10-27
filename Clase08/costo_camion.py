#!/usr/bin/env python3
from informe_final import leer_camion

#%%
def costo_camion(nombre_archivo):
    costoTotal=0
    camiones = leer_camion(nombre_archivo,types=[str,str,str,int,float])
    for n_fila, fila in enumerate(camiones, start=1):
        try:
            costoTotal += int(fila['cajones']) * float(fila['precio'])
        except:
            print(f'Fila {n_fila}: No pude interpretar: {nombre_archivo}')
    print(f'Costo total: ${costoTotal:.2f}')
#%%
def f_principal(params):
    print(f'{params[1]:-^43s}')
    costo_camion(params[1])
    print()
    
#%%
if __name__ == '__main__':
    import sys
    
    if(len(sys.argv) == 2):
        archivo_camion = sys.argv[1]
        f_principal([sys.argv[0],archivo_camion])
    else:
#        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_precios')
        costo_camion(open('../Data/fecha_camion.csv'))



