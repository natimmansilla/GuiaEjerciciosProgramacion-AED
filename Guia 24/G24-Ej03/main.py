__author__ = 'Algoritmos y Estructuras de Datos'

import random

import manejo_archivo
import manejo_vector
import registro
from registro import Pago


def menu():
	cad = 'Menu de Opciones \n' \
	      '=====================================================\n' \
	      '1 - Mostrar el vector\n' \
	      '2 - Buscar pago por numero\n' \
	      '3 - Calcular neto a pagar por tipo de empleo y producto\n' \
	      '4 - Determinar el total por tipo de producto\n' \
	      '5 - Generar Archivo de Pelicula o Serie\n' \
	      '6 - Buscar pago por nombre de cliente\n' \
	      '0 - Salir\n' \
	      'Ingrese su opcion: '
	return int(input(cad))


def generar_matriz(pagos):
	mat = [[0] * 5 for i in range(7)]
	for pago in pagos:
		f = pago.tipo_empleo
		c = pago.tipo_producto - 1
		neto = pago.monto_pagar - pago.gastos
		mat[f][c] += neto
	return mat


def mostrar_matriz(matriz):
	cad = 'El monto neto a pagar para el tipo de empleo {} en {} fue de ${:<10.2f}'
	listado = 'Listado de Montos Netos a pagar\n'
	for f in range(4):
		for c in range(3):
			te = registro.descripcion_tipo_empleo(f)
			tp = registro.descripcion_tipo_producto(c + 1)
			listado += cad.format(te, tp, matriz[f][c]) + '\n'
	print(listado)


def totalizar_por_tipo_producto(matriz, tp):
	total = 0
	for f in range(len(matriz)):
		total += matriz[f][tp - 1]
	return total


def crear_nuevo_pago(vector, nombre):
	numero = registro.crear_numero_pago()
	tipo_empleo = random.randrange(7)
	tipo_producto = random.randint(1, 5)
	monto_pagar = random.uniform(1000, 10000)
	gastos = random.uniform(1000, 10000)
	pago = Pago(numero, nombre, tipo_empleo, tipo_producto, monto_pagar, gastos)
	manejo_vector.add_in_order(vector, pago)


def principal():
	opcion = -1
	pagos = manejo_archivo.generar_vector_pagos()
	matriz = None
	matriz_generada = False

	while opcion != 0:
		opcion = menu()
		if opcion == 1:
			manejo_vector.mostrar_vector(pagos)

		elif opcion == 2:
			x = input('Ingrese el numero a buscar: ')
			pos = manejo_vector.buscar_por_numero(pagos, x)
			if pos != -1:
				pagos[pos].monto_pagar *= 1.25
				print(pagos[pos])
			else:
				print('El registro con el numero {} no existe'.format(x))

		elif opcion == 3:
			matriz_generada = False
			matriz = generar_matriz(pagos)
			mostrar_matriz(matriz)

		elif opcion == 4:
			if matriz_generada:
				tp = random.randint(1, 5)
				total = totalizar_por_tipo_producto(matriz, tp)
				cad = 'El monto neto a pagar para el tipo de producto {} fue de ${:<10.2f}' \
					.format(registro.descripcion_tipo_producto(tp), total)
				print(cad)
			else:
				print('Debe primero ejecutar la opcion que genera la matriz')

		elif opcion == 5:
			promedio = manejo_vector.promediar_netos_pagar(pagos)
			manejo_archivo.generar_archivo_binario(pagos, promedio, 'pagos_peliculas_series.dat')
			manejo_archivo.mostrar_archivo_binario('pagos_peliculas_series.dat')

		elif opcion == 6:
			nombre = input('Ingrese el nombre: ')
			pos = manejo_vector.buscar_por_nombre(pagos, nombre)
			if pos != -1:
				print(pagos[pos])
			else:
				crear_nuevo_pago(pagos, nombre)
				print('Se agrego un pago con el nombre', nombre)

		elif opcion == 0:
			manejo_archivo.grabar_archivo_texto(pagos)


if __name__ == '__main__':
	principal()
