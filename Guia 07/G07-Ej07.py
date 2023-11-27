__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Busqueda de Mayores Pares y Menores Impares')
print('-' * 80)
primer_par = True
primer_impar = True

# Datos y proceso
for i in range(8):
    num = random.randint(1, 100)
    print(num, end=' ')
    if num % 2 == 0:
        if primer_par:
            may = num
        elif num > may:
            may = num
        primer_par = False
    else:
        if primer_impar:
            men = num
        elif num < men:
            men = num
        primer_impar = False

# Resultados
print()
print('-' * 80)
if primer_par == False:
    print('El mayor par es', may)
else:
    print('No hubo numeros pares')
if primer_impar == False:
    print('El menor impar es', men)
else:
    print('No hubo numeros impares')
