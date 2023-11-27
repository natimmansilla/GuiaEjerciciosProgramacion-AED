__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

import manejador_archivo
import registro


def menu():
	cadena = 'Menu de Opciones\n' \
	         '========================================================\n' \
	         '1 ---- Mostrar todos los datos de todas las figuritas\n' \
	         '2 ---- Agregar una figurita al arreglo\n' \
	         '3 ---- Generar conteo por cada posible país y cada posicion de jugador\n' \
	         '4 ---- Generar y mostrar un nuevo archivo binario\n' \
	         '5 ---- Guardar toda la información contenida en el arreglo en el archivo figuritas.csv\n' \
	         '0 ---- Salir\n' \
	         'Ingrese la opcion a ejecutar: '
	return int(input(cadena))


def encabezado():
	cadena = '|{:<72}|\n|{:^72}|\n|{:<72}|\n' \
	         '| {:<30} | {:<4} | {:<4} | {:<15} | {:<5} |\n{:<74}'

	return cadena.format('=' * 72, 'Listado de Figuritas', '=' * 72, 'Nombre', 'Pais', 'Jug.', 'Posicion', 'Canje',
	                     '-' * 74)


def mostrar_arreglo(vector):
	print(encabezado())
	for figurita in vector:
		print(figurita)


def buscar(vector, pais, numero):
	pos = -1
	for i in range(len(vector)):
		if vector[i].pais == pais and vector[i].numero == numero:
			pos = i
			break
	return pos


def existe(vector, pais, numero):
	pos = buscar(vector, pais, numero)
	return pos >= 0


def agregar_figurita(vector):
	pais = random.randint(1, 32)
	numero = random
	while existe(vector, pais, numero):
		numero = random

	nombre = registro.generar_nombre()
	posicion = random.randrange(4)
	valor_canje = random.randint(1, 150)
	figurita = registro.Figurita(nombre, pais, numero, posicion, valor_canje)
	vector.append(figurita)


def contar_por_pais_posicion(vector):
	m = [[0] * 4 for i in range(32)]
	for figurita in vector:
		f = figurita.pais - 1
		c = figurita.posicion
		m[f][c] += 1
	return m


def mostrar_matriz(mc, c):
	print('Cantidad de Jugadores por pais y posicion mayore a {}'.format(c))
	for i in range(len(mc)):
		for j in range(len(mc[i])):
			if mc[i][j] >= c:
				desc_posicion = registro.descripcion_posicion(j)
				print(f'Para el pais {i + 1} y posicion {desc_posicion} hay {mc[i][j]} jugadores')


def principal():
	opcion = -1

	figuritas = manejador_archivo.generar_arreglo('figuritas.csv')

	while opcion != 0:
		opcion = menu()
		if figuritas is not None and len(figuritas) > 0:
			if opcion == 1:
				mostrar_arreglo(figuritas)

			elif opcion == 2:
				agregar_figurita(figuritas)

			elif opcion == 3:
				mc = contar_por_pais_posicion(figuritas)
				c = int(input('Ingrese el valor a comparar: '))
				mostrar_matriz(mc, c)

			elif opcion == 4:
				v = int(input('Ingrese el valor de canje a comparar: '))
				manejador_archivo.generar_binario(figuritas, v, 'valiosos.dat')
				cadena = encabezado()
				manejador_archivo.mostrar_archivo_binario('valiosos.dat', cadena)

			elif opcion == 5:
				manejador_archivo.guardar_arreglo(figuritas, 'figuritas.csv')
		else:
			print('Primero debe cargar ')


if __name__ == '__main__':
	principal()
