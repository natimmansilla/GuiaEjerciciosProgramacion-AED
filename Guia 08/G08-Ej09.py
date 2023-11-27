__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

random.seed(37)
n = 27000
cant_entre_20k_y_5K = cant_entre_5k_y_15K = cant_may_15K = cant_mult_7 = 0
cant_may_100 = acu_may_100 = 0
primer_pos_impar = True
mayor_pos_impar = None

for i in range(n):
	num = random.randint(-20000, 30000)

	if -20000 <= num < -5000:
		cant_entre_20k_y_5K += 1

	elif -5000 <= num < 15000:
		cant_entre_5k_y_15K += 1

	elif num >= 15000 and num % 9 == 0:
		cant_may_15K += 1

	ult_dig = num % 10
	if num >= 1000 and (ult_dig == 4 or ult_dig == 6):
		cant_may_100 += 1
		acu_may_100 += num

	if num > 0 and num % 2 == 1 and ult_dig != 1:
		if primer_pos_impar:
			mayor_pos_impar = num
			primer_pos_impar = False
		elif num > mayor_pos_impar:
			mayor_pos_impar = num

	if num % 7 == 0:
		cant_mult_7 += 1

promedio = 0
if cant_may_100 > 0:
	promedio = acu_may_100 // cant_may_100

porcentaje = cant_mult_7 * 100 // n

print('La cantidad de numeros entre -20000 incluido y -5000 son:', cant_entre_20k_y_5K)
print('La cantidad de numeros entre -5000 incluido y 15000 son:', cant_entre_5k_y_15K)
print('La cantidad de numeros mayor a 15000 incluido y multiplos de 9 son:', cant_may_15K)
print('El promedio de los numeros mayores a 1000 y terminan con 4 o 6 son:', promedio)
print('El mayor de los numeros positivos impares que no terminan en 1 es:', mayor_pos_impar)
print('El Porcentaje de los numeros divisibles por 7 sobre el total de numeros leidos es:', porcentaje, '%')
