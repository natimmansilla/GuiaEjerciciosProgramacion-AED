__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Ejercicio de Proceso de Secuencias - Tipo Parcial')
print('=' * 80)

random.seed(76)
contador_par_mul6 = contador_mult_primer_num = contador_segundo_millar = 0
primer_numero = None

for i in range(5000):
    numero = random.randint(1, 65000)
    if numero % 2 == 0 and numero % 6 == 0:
        contador_par_mul6 += 1

    if primer_numero is None:
        primer_numero = numero
    else:
        if numero > primer_numero:
            contador_mult_primer_num += 1

    if 1000 < numero < 2000:
        contador_segundo_millar += 1

porcentaje = contador_mult_primer_num * 100 // 5000

print('La cantidad de números pares que sean múltiplos de 6:', contador_par_mul6)
print('La cantidad de números son múltiplos del primer número de la serie es:', contador_mult_primer_num)
print('La cantidad de números que perteneces al segundo millar de números es:', contador_segundo_millar)
print('El porcentaje que representan la cantidad de números del punto 2:', porcentaje)
