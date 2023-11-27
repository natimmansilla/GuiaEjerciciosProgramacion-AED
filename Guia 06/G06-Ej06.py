__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

menor = None
i = 0
suma = 0
cont = 0
while i < 5000:
    n = random.randint(0, 100000)
    if menor is None or menor > n:
        menor = n
    if n < 10000:
        suma += n
        cont += 1
    i += 1
if cont != 0:
    p = suma / cont
else:
    p = 0
print("El menor es", menor, "y el promedio de los menores a 10000 es:", p)
