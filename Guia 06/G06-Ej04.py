__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Calcular promedio de aleatorios')
print('=' * 80)

acumulador = 0
i = 0
while i < 1000:
    n = random.randint(0, 100000)
    acumulador += n
    i += 1
promedio = acumulador / i
print("El promedio es", promedio)

print("Fin del programa :)")
