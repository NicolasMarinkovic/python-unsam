# El módulo collections ofrece objetos útiles para manejar datos
# Es muy poderoso pero meterse a ver sus detalles sería una distracción ahora. 

# Contar cosas

camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

# Hay dos entradas de Naranja y dos de Pera en esta lista. Estos cajones deben ser combinados juntos de alguna forma.
# Solución: Usá un Counter (contador).

from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

total_cajones
# Counter({'Pera': 175, 'Naranja': 150, 'Caqui': 150, 'Lima': 50})
total_cajones['Naranja']     # 150

#Podés listar las tres frutas con mayores tenencias:
total_cajones.most_common(3)
#[('Pera', 175), ('Naranja', 150), ('Caqui', 150)]


# ------
# Dos tenencias se pueden sumar por ej

tenencias
#Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
tenencias2
#Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
combinada = tenencias + tenencias2

#Counter({'Caqui': 150, 'Durazno': 220, 'Frambuesa': 250, 'Lima': 150, 'Mandarina': 275, 'Naranja': 150})




