__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Tarjeta de Bingo')
print("=" * 80)

print("\nCarga de Datos")
print('-' * 80)

billete = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
    random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
    random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
    random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

primer_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))
segundo_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))
tercer_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))

# Proceso y salida de resultados
print('La tarjeta del usuario es: ', billete)
if primer_numero in billete or segundo_numero in billete or tercer_numero in billete:
    print('El jugador marco algun numero de la tarjeta')
else:
    print('El jugador tiene mala suerte, no marco ninguna casilla')
