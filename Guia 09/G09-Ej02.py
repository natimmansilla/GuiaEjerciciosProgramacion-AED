__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

# PEDIR EL VALOR N Y VALIDARLO
n = int(input("Ingrese la cantidad de números que quiere generar: "))
while n <= 0:
	n = int(input("Error!!! Ingrese la cantidad de números que quiere generar (mayor a cero): "))

# INICIALIZAR
# a) Cuántos números terminan en 5.
cantidad_termina_5 = 0
# b) El porcentaje de números pares en la secuencia.
cantidad_pares = 0
porcentaje_pares = 0

# c) Cual es el menor número múltiplo de 3 de la secuencia.
menor_multiplo_3 = None

# d) La cantidad de veces que aparece el primer número de la secuencia.
cantidad_primer_numero = 0
primer_numero = None

# CICLO DE N
for i in range(n):  # 0, 1, 2, 3, ...., n-1
	# GENERAR UN NUMERO ENTERO
	numero = random.randint(1, 100)

	# punto a
	if numero % 10 == 5:
		cantidad_termina_5 += 1

	# punto b
	if numero % 2 == 0:
		cantidad_pares += 1

	# punto c
	if (menor_multiplo_3 is None) and (numero % 3 == 0):
		menor_multiplo_3 = numero
	elif (numero % 3 == 0) and (numero < menor_multiplo_3):
		menor_multiplo_3 = numero

	# punto d
	if primer_numero is None:
		primer_numero = numero
		cantidad_primer_numero += 1
	elif numero == primer_numero:
		cantidad_primer_numero += 1

# CALCULOS FINALES Y MOSTRAR RESULTADOS
# punto a
print("La cantidad de números que terminan en 5 es: ", cantidad_termina_5)
# punto b
porcentaje_pares = cantidad_pares * 100 / n
print("El porcentaje de números pares es: ", porcentaje_pares)
# punto c
print("El menor número múltiplo de 3 es : ", menor_multiplo_3)
# punto d
print("El primer número ", primer_numero, "aparecio :", cantidad_primer_numero, "veces")
