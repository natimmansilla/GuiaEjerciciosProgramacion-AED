__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

random.seed(95)
n = 45000
segundo_numero = primer_numero = None
cant_menores_seg_num = 0
cant_mult_6 = cant_mult_9 = cant_mult_69 = 0
primer_mult_4 = True
mayor_mult = None

for i in range(n):
	num = random.randint(1, 95000)

	# incluyendo el primer numero del secuencia
	if i == 0:
		primer_numero = num

	if i == 1:
		segundo_numero = num
		if primer_numero < segundo_numero:
			cant_menores_seg_num += 1

	if i > 1 and num < segundo_numero:
		cant_menores_seg_num += 1

	if num % 6 == 0 and num % 9 == 0:
		cant_mult_69 += 1

	if num % 6 == 0:
		cant_mult_6 += 1

	if num % 9 == 0:
		cant_mult_9 += 1

	if num % 4 == 0:
		if primer_mult_4:
			mayor_mult = num
			primer_mult_4 = False
		elif num > mayor_mult:
			mayor_mult = num

porcentaje = cant_menores_seg_num * 100 // n

print('La cantidad de numeros que son menores al segundo numero de la serie son:', cant_menores_seg_num,
      'y representan un', porcentaje, '% sobre el total de numeros leidos')
print('La cantidad de numeros que son multiplos de 6 son:', cant_mult_6)
print('La cantidad de numeros que son multiplos de 9 son:', cant_mult_9)
print('La cantidad de numeros que son multiplos de 6 y de 9 son:', cant_mult_69)
print('El mayor de los numeros de multplo de 4 es:', mayor_mult)
