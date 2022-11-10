#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:50:24 2022

@author: datascience
"""

import lote
import fileparse
with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
camion
# [<lote.Lote object at 0x10c9e2128>, <lote.Lote object at 0x10c9e2048>, <lote.Lote object at 0x10c9e2080>,
# <lote.Lote object at 0x10c9e25f8>, <lote.Lote object at 0x10c9e2630>, <lote.Lote object at 0x10ca6f748>,
# <lote.Lote object at 0x10ca6f7b8>]
print(sum([c.costo() for c in camion]))
#47671.15
