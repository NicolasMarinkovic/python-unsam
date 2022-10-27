'''
Líneas en blanco

Separar las definiciones de las clases y funciones con dos líneas en blanco. Los métodos dentro de clases se separan con una línea en blanco. Se recomienda utilizar líneas en blanco para separar partes del código, por ejemplo dentro de una función, que realizan tareas diferenciadas.
'''
#%%

'''
Espacios en blanco en expresiones

Evitar espacios en blanco extra en:

Dentro de paréntesis, corchetes o llaves.

# Sí: 
spam(ham[1], {eggs: 2})

# No:  
spam( ham[ 1 ], { eggs: 2 })

Antes de una coma.

# Sí: 
if x == 4: print x, y; x, y = y, x 

# No: 
if x == 4 : print x , y ; x , y = y , x
'''
#%%

'''
Estilos de nombres

Hay muchos estilos para nombrar variable, funciones, etc. Es útil reconocer qué estilo se está usando, independientemente de para qué se está usando.

Éstos son algunos estilos:

    b (una sola letra, en minúscula)
    B (una sola letra, en mayúscula)
    minusculas
    minusculas_con_guiones_bajos
    MAYUSCULAS
    MAYUSCULAS_CON_GUIONES_BAJOS
    PalabrasConMayusculas (también llamado estilo camello por las jorobas)
    mixedCase (difiere del camello en la inicial)
    Con_Mayusculas_Y_Guiones_Bajos (horrible!)

'''

#%%
'''
Zen de Pyhton

Ya que estamos hablando de los PEPs, queremos mencionar el PEP 20 (PEP viene de Python Enhancement Proposals), también conocido como el Zen de Python

El Zen de Python es una colección de principios de software que influyen en el diseño del lenguaje. El texto, que copiamos a continuación se puede encontrar en el sitio oficial de Python y también se incluye como sorpresa en el intérprete de Python al escribir la instrucción import this.​

Zen de Pyhton

    Bello es mejor que feo.

    Explícito es mejor que implícito.

    Simple es mejor que complejo.

    Complejo es mejor que complicado.

    Plano es mejor que anidado.

    Espaciado es mejor que denso.

    La legibilidad es importante.

    Los casos especiales no son lo suficientemente especiales como para romper las reglas.

    Sin embargo la practicidad le gana a la pureza.

    Los errores nunca deberían pasar silenciosamente.

    A menos que se silencien explícitamente.

    Frente a la ambigüedad, evitá la tentación de adivinar.

    Debería haber una, y preferiblemente solo una manera obvia de hacerlo.

    A pesar de que esa manera no sea obvia a menos que seas Holandés.

    Ahora es mejor que nunca.

    A pesar de que nunca es muchas veces mejor que justo ahora.

    Si la implementación es difícil de explicar, es una mala idea.

    Si la implementación es fácil de explicar, puede que sea una buena idea.

    Los espacios de nombres son una gran idea, ¡hagamos más de ellos!

'''

