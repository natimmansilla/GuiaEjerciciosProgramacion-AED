__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os
import pickle
import random

import funciones

import registro


def menu():
	cadena = 'Menu de Opciones:\n' + \
	         '===========================================\n' + \
	         '1 - Cargar un arreglo ordenado de operaciones\n' \
	         '2 - Mostrar todos los datos del arreglo\n' \
	         '3 - Determinar la cantidad de operaciones que se realizaron por modelo y año\n' \
	         '4 - Buscar en el arreglo una operación con el nombre del comprador\n' \
	         '5 - Generar un archivo binario con operaciones mayores al promedio de ventas \n' \
	         '6 - Mostrar el archivo generado\n' \
	         '0 - Salir\n' \
	         'Ingrese su opcion: '
	return int(input(cadena))


def cargar_codigo(vector):
	codigo = random.randint(100, 15000)
	while funciones.existe(vector, codigo):
		print('El codigo existe, se generara uno nuevo')
		codigo = random.randint(100, 15000)
	return codigo


def generar_operaciones(vector, n):
	for i in range(n):
		codigo = cargar_codigo(vector)
		nombre = registro.generar_nombre_comprador()
		monto = random.uniform(150000, 12000000)
		marca = random.randint(1, 15)
		modelo = random.randint(2000, 2022)
		operacion = registro.Operacion(codigo, nombre, monto, marca, modelo)
		funciones.add_in_order(vector, operacion)


def mostrar(vector, ver_promedio=True):
	print('Listado de Operacion')
	print(registro.encabezado())
	total = 0
	for operacion in vector:
		total += operacion.monto_venta
		print(operacion)

	if ver_promedio:
		promedio = funciones.calcular_promedio(total, len(vector))
		print(f'El promedio total de montos de ventas fue de ${promedio:<10.2f}')


def generar_matriz(vector):
	m = [[0] * 23 for i in range(15)]
	for operacion in vector:
		f = operacion.marca - 1
		c = operacion.modelo - 2000
		m[f][c] += 1
	return m


def obtener_promedio_ventas(vector):
	total = 0
	for operacion in vector:
		total += operacion.monto_venta
	return funciones.calcular_promedio(total, len(vector))


def generar_archivo_operaciones(vector, archivo):
	promedio = obtener_promedio_ventas(vector)
	m = open(archivo, 'wb')
	for operacion in vector:
		if operacion.monto_venta > promedio:
			pickle.dump(operacion, m)
	m.close()


def mostrar_archivo_operaciones(archivo):
	if not os.path.exists(archivo):
		print('No existe el archivo')
		return

	m = open(archivo, 'rb')
	size = os.path.getsize(archivo)
	cantidad = 0
	print(registro.encabezado())
	while m.tell() < size:
		operacion = pickle.load(m)
		cantidad += 1
		print(operacion)

	m.close()
	print(f'Se leyeron {cantidad} de operaciones')


def mostrar_matriz(matriz, ver_table=False):
	if not ver_table:
		for f in range(len(matriz)):
			for c in range(len(matriz[f])):
				if matriz[f][c] > 0:
					print(f'Hay {matriz[f][c]} operaciones de la marca {f + 1} y el modelo'
					      f'{2000 + c}')
	else:

		titulos = '| {:^5} |'.format('Marca')
		for i in range(len(matriz[0])):
			titulos += ' {:^4} |'.format(2000 + i)
		encabezado = '{:<170}\n{:<170}\n{:<170}'.format('-' * 170, titulos, '-' * 170)
		print(encabezado)

		for f in range(len(matriz)):
			linea = f'| {f + 1:^5} |'
			for c in range(len(matriz[f])):
				linea += f' {matriz[f][c]:^4} |'
			linea += f'\n{"-" * 170:<170}'
			print(linea)


def principal():
	opcion = -1
	vector = []

	while opcion != 0:
		opcion = menu()

		if opcion == 1:
			n = funciones.validar_mayor_que(0, 'Ingrese la cantidad de operaciones: ')
			generar_operaciones(vector, n)

		elif len(vector) > 0:
			if opcion == 2:
				mostrar(vector)

			elif opcion == 3:
				mat = generar_matriz(vector)
				mostrar_matriz(mat, True)

			elif opcion == 4:
				nom = input('Ingrese el nombre del comprador')
				pos = funciones.buscar_comprador(vector, nom)
				if pos != -1:
					x = funciones.validar_mayor_que(0, 'Ingrese el porcentaje a incrementar: ')
					vector[pos].monto_venta *= 1 + (x / 100)
					# vector[pos].monto_venta += (vector[pos].monto_venta * 20 / 100)
					print(vector[pos])
				else:
					print('No Existe')
			elif opcion == 5:
				generar_archivo_operaciones(vector, 'operaciones.dat')

			elif opcion == 6:
				mostrar_archivo_operaciones('operaciones.dat')
		else:
			print('Primero debe ejecutar la opcion 1')


if __name__ == '__main__':
	principal()
