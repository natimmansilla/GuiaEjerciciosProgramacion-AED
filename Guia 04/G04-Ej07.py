__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Tirada de la moneda')
print('=' * 80)

caras = 'cara', 'cruz'

apuesta = int(input('Seleccion que cara desea apostar (0 Cara 1 Cruz): '))
jugada = random.choice(caras)

if jugada == caras[apuesta]:
    print('El jugador ha ganado el juego, acerto, salio', jugada)
else:
    print('El jugador ha perdido el juego salio', jugada, 'y el jugador aposto a', caras[apuesta])
