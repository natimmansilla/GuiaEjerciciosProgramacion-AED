__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

# Definir semilla e intervalos
random.seed(11)
n = 1000
inicio = 1
fin = 2500
# Inicializar contadores y acumuladores
divisibles4, divisibles48 = 0, 0
suma_mayores, cant_mayores = 0, 0
menores = 0
hay_extremos = False
# Datos y procesos
for i in range(n):
	num = random.randint(inicio, fin)
	# Controlar si son divisibles por 4
	if num % 4 == 0:
		# Diferenciar los que son divisibles por 8 y los que no
		if num % 8 != 0:
			divisibles4 += 1
		else:
			divisibles48 += 1

	# Contar y sumar valores mayores a 2000
	if num > 2000:
		suma_mayores += num
		cant_mayores += 1

	# Diferenciar el primer valor y comparar a los restantes
	if i == 0:
		primero = num
	elif num < primero:
		menores += 1

	# Controlar si aparecen los extremos
	if num == inicio or num == fin:
		hay_extremos = True

# Resultados
print('Números divisibles por 4 pero no por 8 son:', divisibles4)
print('Números divisibles por 4 y por 8 son:', divisibles48)
# Calcular promedio (evitar división por 0)
if cant_mayores == 0:
	promedio = 0
else:
	promedio = suma_mayores / cant_mayores
print('Promedio de los valores mayores a 2000:', round(promedio, 2))
# Calcular porcentaje
porcentaje = menores * 100 / n
print('Números menores al primer valor generado:', menores, 'y representan', round(porcentaje, 2), '% del total')
# Informar si aparecieron los extremos
if hay_extremos:
	print('Aparecieron en la secuencia los valores extremos del intervalo')
else:
	print('NO aparecieron en la secuencia los valores extremos del intervalo')
