__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

# Programa de cálculo de peajes
print('Bienvenido a Pase-Pase')
print('=' * 20)

# Ingreso de datos
digitos_patente = int(input('Ingrese dígitos:'))

# Sorteo del dígito
sorteo = random.randint(0, 9)
print('Sorteo: ', sorteo)

# Extracción del último dígito de la patente
ultimo_digito = digitos_patente % 10

# Cálculo de la tarifa
if sorteo == ultimo_digito:
    print('Tarifa Promocional')
    # Si coincide el último dígito con lo sorteado
    # Es precio promocional
    tarifa = 50
else:
    print('Tarifa Completa')
    # Si no coincide, es precio completo
    tarifa = 90

# Cálculo del descuento
if ultimo_digito == 7:
    print('Descuento del 50%')
    # Si la patente termina en 7, el
    # descuento es de 50%
    descuento = tarifa * 0.5
else:
    print('Descuento del 10%')
    # Si la patente NO termina en 7, el
    # descuento es del 10%
    descuento = tarifa * 0.1

# Monto final a pagar
monto = tarifa - descuento

# Resultados
print('=== RESULTADOS ===')
print('Debe abonar: $', monto)
