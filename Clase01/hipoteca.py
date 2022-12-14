# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    pago_mensual = 2684.11
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_mensual += pago_extra
    if saldo * (1+tasa/12) < pago_mensual:
        pago_mensual = saldo * (1+tasa/12)
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print(mes, round(total_pagado,2), round(saldo,2))

print(f'El total pagado es ${total_pagado:0.2f} en {mes} meses')
