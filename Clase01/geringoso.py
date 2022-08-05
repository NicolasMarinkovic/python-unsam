# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if c == 'a' or c =='A':
        capadepenapa += 'pa'
    elif c == 'e' or c =='E':
        capadepenapa += 'pe'
    elif c == 'i' or c =='I':
        capadepenapa += 'pi'
    elif c == 'o' or c =='O':
        capadepenapa += 'po'
    elif c == 'u' or c =='U': 
        capadepenapa += 'pu'       

print(capadepenapa)
