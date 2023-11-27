__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from random import randint


def validar_mayor_que(limite, mensaje='Ingerse un numero: '):
	num = limite
	while num <= limite:
		num = int(input(mensaje))
		if num <= limite:
			print(f'Error!!!! El valor debe ser mayor a {limite}')
	return num


def buscar_comprador(vector, nom):
	pos = -1
	for i in range(len(vector)):
		if vector[i].comprador == nom:
			pos = i
			break
	return pos


def add_in_order(vector, operacion):
	izq, der = 0, len(vector) - 1
	pos = -1
	while izq <= der:
		med = (izq + der) // 2
		if vector[med].codigo == operacion.codigo:
			pos = med
			break

		if operacion.codigo > vector[med].codigo:
			izq = med + 1
		else:
			der = med - 1

	if izq > der:
		pos = izq

	vector[pos:pos] = [operacion]


def buscar(vector, num):
	izq, der = 0, len(vector) - 1
	pos = -1
	while izq <= der:
		med = (izq + der) // 2
		if vector[med].codigo == num:
			pos = med
			break

		if num > vector[med].codigo:
			izq = med + 1
		else:
			der = med - 1

	return pos


def existe(vector, num):
	pos = buscar(vector, num)
	return pos >= 0


def cargar_codigo(vector):
	num = randint(1, 100)
	while existe(vector, num):
		print("Error!!!! El numero se encuentra duplicado, se solicitara uno nuevo")
		num = randint(1, 100)
	return num


def calcular_promedio(total, cantidad):
	promedio = 0
	if cantidad > 0:
		promedio = total / cantidad
	return promedio
