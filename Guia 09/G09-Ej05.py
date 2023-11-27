__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Simulacro 1 del Parcial 1')
print('=' * 60)

random.seed(49)

# acumulador de TODOS los números generados, como elemento de control...
st = 0

cont_mult5 = cont_mult7 = cont_mult9 = 0
cont_pares = 0
mayor = None
n = 20000

for i in range(n):
	numero = random.randint(1, 45000)
	st += numero

	if numero % 5 == 0:
		cont_mult5 += 1
	if numero % 7 == 0:
		cont_mult7 += 1
	if numero % 9 == 0:
		cont_mult9 += 1

	ultimo = numero % 10
	if 5 <= ultimo <= 8:
		if mayor is None or numero > mayor:
			mayor = numero

	es_par = numero % 2 == 0
	if es_par and numero < 15000:
		cont_pares += 1

porcentaje = cont_pares * 100 // n

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Resultados pedidos por el enunciado:')
print('La cantidad de numeros multiplo de 5 fueron:', cont_mult5)
print('La cantidad de numeros multiplo de 7 fueron:', cont_mult7)
print('La cantidad de numeros multiplo de 9 fueron:', cont_mult9)
print('El mayor numero que terminan con un numero entre 5 y 8 es:', mayor)
print('La cantidad de numeros pares menores a 15000 son:', cont_pares)
print('y representan el', porcentaje, '%')
