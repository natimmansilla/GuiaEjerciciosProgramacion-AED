__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import pickle
import random

from viaje import *


def validar_mayor_a(minimo, mensaje):
	numero = int(input(mensaje))
	while numero <= minimo:
		print('Error!! Debe ser mayor a', minimo)
		numero = int(input(mensaje))
	return numero


def add_in_order(viaje, vector):
	tam = len(vector)

	izq, der = 0, tam - 1
	pos = der
	while izq <= der:
		med = (izq + der) // 2
		if vector[med].numero == viaje.numero:
			pos = med
			break

		if viaje.numero < vector[med].numero:
			der = med - 1
		else:
			izq = med + 1

	if izq > der:
		pos = izq

	vector[pos:pos] = [viaje]


def generar_arreglo(n, vector):
	for i in range(n):
		numero = random.randint(1, 10000)
		chofer = "Chofercito N°" + str(random.randint(1, 10000))
		origen = random.randrange(10)
		destino = random.randrange(10)
		servicio = random.randrange(5)
		costo = random.randint(100, 350)
		viaje = Viaje(numero, chofer, costo, origen, destino, servicio)
		add_in_order(viaje, vector)


def mostar(vector):
	print('Listado de Viajes')

	for viaje in vector:
		print('\n' + str(viaje))


def generar_por_servicio(vector, servicio):
	v = []
	for viaje in vector:
		if viaje.tipo_servicio == servicio:
			v.append(viaje)
	return v


def validar_rango(minimo, maximo, mensaje):
	numero = int(input(mensaje))
	while numero < minimo or numero > maximo:
		print('Error!!! El valor debe estar entre', minimo, 'y', maximo)
		numero = int(input(mensaje))
	return numero


def totalizar_por_chofer(chofer, vector):
	total = 0
	for viaje in vector:
		if viaje.chofer == chofer:
			total += viaje.costo

	return total


def genera_archivo(vservicios):
	arch = 'viajes_servicio.dat'
	f = open(arch, 'wb')

	for viaje in vservicios:
		pickle._dump(viaje, f)

	f.flush()
	f.close()


def generar_matriz(vector):
	mat = [[0] * 10 for i in range(10)]
	for viaje in vector:
		f = viaje.origen
		c = viaje.destino
		mat[f][c] += 1
	return mat


def main():
	menu = 'Menu de Opciones\n' \
	       '============================================\n' \
	       '1 - Generar Arreglo de viajes\n' \
	       '2 - Totalizar por Chofer\n' \
	       '3 - Generar y Mostrar Vector de Servicion\n' \
	       '4 - Generar Archivo\n' \
	       '0 - Salir\n' \
	       'Ingrese su opcion: '

	vector = []
	vservicios = []
	opcion = -1
	while opcion != 0:
		opcion = int(input(menu))
		if opcion == 1:
			n = validar_mayor_a(0, 'Ingrese la cantidad de viajes: ')
			generar_arreglo(n, vector)

		if len(vector) != 0:
			if opcion == 2:
				chofer = input('Ingrese el nombre del chofer a buscar: ')
				total = totalizar_por_chofer(chofer, vector)
				print('El total de viajes cobrados en viajes del chofer', chofer, 'fueron', total)

			elif opcion == 3:
				servicio = validar_rango(0, 4, 'Ingrese el tipo de servicio a buscar: ')
				vservicios = generar_por_servicio(vector, servicio)
				mostar(vservicios)

			elif opcion == 4:
				if len(vservicios) == 0:
					print('Se debe generar el vector con el punto 3')
				else:
					genera_archivo(vservicios)

			elif opcion == 5:
				matriz = generar_matriz(vector)
				for i in range(matriz):
					for j in random(matriz[i]):
						print('La Cantidad de viajes del origen', i, 'al destino', j, 'fueron:', matriz[i][j])

		else:
			print('Debe primero ejecutar la opcion 1')


if __name__ == '__main__':
	main()
