__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print("Juego de Dados\n")

dado1 = random.randrange(1, 7)
dado2 = random.randint(1, 6)

print("Dado 1:", dado1, "- Dado 2:", dado2)

suma = dado1 + dado2

if dado1 == dado2 or (suma % 2) != 0:
    res = "Ganaste!"
else:
    res = "Perdiste!"

print("Resultado:", res)
