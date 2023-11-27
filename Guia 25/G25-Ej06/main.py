__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import registro
from funciones import *


def menu():
	cadena = 'Menu de Opciones\n' \
	         '========================================\n' \
	         '1 --- Buscar y mostrar la consulta con el mayor costo\n' \
	         '2 --- Buscar las consultas hechas por un propietario\n' \
	         '3 --- Obtener el total por especie de mascota y tipo de atención\n' \
	         '4 --- Generar un archivo binario especie.dat con todas las consultas hechas a mascotas\n' \
	         '0 --- Salir\n' \
	         'Ingrese su opcion: '
	return int(input(cadena))


def buscar_mayor_costo(vector):
	lista = []
	primero = True
	for consulta in vector:
		if primero or consulta.costo > lista[0].costo:
			lista = [consulta]
			primero = False
		elif lista[0].costo == consulta.costo:
			lista.append(registro)
	return lista


def buscar_propietario(vector, nom):
	lista = []
	pos = buscar_binaria(vector, nom)
	if pos != -1:
		for i in range(pos, len(vector)):
			if vector[i].nombre_propietario != nom:
				break
			lista.append(vector[i])
	return lista


def acumular_por_especie_tipo(vector):
	mat = [[0] * 20 for i in range(10)]

	for consulta in vector:
		f = consulta.especie - 1
		c = consulta.tipo_atencion
		mat[f][c] += consulta.costo

	return mat


def principal():
	opcion = -1
	consultas = cargar_vector('mascotas.csv')
	mostrar_consultas(consultas)

	while opcion != 0:
		opcion = menu()
		if opcion == 1:
			lista = buscar_mayor_costo(consultas)
			mostrar_consultas(lista)

		elif opcion == 2:
			nom = input('Ingrese el nombre del propietario: ')
			lista = buscar_propietario(consultas, nom)
			mostrar_consultas(lista)

		elif opcion == 3:
			matriz = acumular_por_especie_tipo(consultas)
			for f in range(len(matriz)):
				for c in range(len(matriz[f])):
					if matriz[f][c] > 0:
						print(f'Matriz[{f}][{c}] = {matriz[f][c]}')

		elif opcion == 4:
			generar_achivo_binario(consultas, 'especie.dat')
			leer_archivo('especie.dat')


if __name__ == '__main__':
	principal()
