__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os.path
import pickle


def menu():
	cadena = 'Menu de Opciones\n' \
	         '========================================================\n' \
	         '1 --- Mostrar el listado completo del archivo de votos.\n' \
	         '2 --- Generar una matriz por provincia y candidato.\n' \
	         '3 --- Mostrar la matriz y el nombre del candidato ganador.\n' \
	         '0 --- Salir\n' \
	         'Ingrese su opcion: '
	return int(input(cadena))


def mostrar_votos(votos):
	if not os.path.exists(votos):
		print('Debe primero generar el archivo usando el generador')
		return

	m = open(votos, 'rb')
	size = os.path.getsize(votos)
	print('Listado de votos en la eleccion')
	print('=' * 70)
	while m.tell() < size:
		voto = pickle.load(m)
		print(voto)
	m.close()


def generar_matriz(votos):
	if not os.path.exists(votos):
		print('Debe primero generar el archivo usando el generador')
		return

	matriz = [[0] * 7 for i in range(23)]
	m = open(votos, 'rb')
	size = os.path.getsize(votos)
	while m.tell() < size:
		voto = pickle.load(m)
		fila = voto.provincia
		columna = voto.candidato
		matriz[fila][columna] += 1
	return matriz


def acumular_por_candidato(matriz):
	va = [0] * 7
	for f in range(len(matriz)):
		for c in range(len(matriz[f])):
			va[c] += matriz[f][c]
	return va


def buscar_ganador(vector):
	mayor = None
	for i in range(len(vector)):
		if mayor is None or mayor[1] > vector[i]:
			mayor = i, vector[i]
	return mayor


def buscar_nombre(codigo, candidatos):
	if not os.path.exists(candidatos):
		print('Debe primero generar el archivo usando el generador')
		return

	candidato = None
	m = open(candidatos, 'rb')
	size = os.path.getsize(candidatos)
	while m.tell() < size:
		candidato = pickle.load(m)
		if candidato.codigo == codigo:
			break
	m.close()
	return candidato


def mostrar(mat, mayor, candidatos):
	celda = '|{:^7}'
	cadena = (f'{"=" * 64:<64}\n'
	          f'| {"Prov.":^6}|{"Candidatos(0-6)":^55}|\n'
	          f'{"=" * 64:<64}|\n')
	for f in range(len(mat)):
		cadena += celda.format(f)
		for c in range(len(mat[f])):
			cadena += celda.format(mat[f][c])
		cadena += '|\n'
	cadena += f'|{"=" * 63:<63}|\n'
	print(cadena)
	ganador = buscar_nombre(mayor[0], candidatos)
	print(f'El ganador de la eleccion fue el {str(ganador)} con {mayor[1]} de los votos')
	print()

def principal():
	votos = 'votos.dat'
	candidatos = 'candidatos.dat'
	mat = None
	opcion = -1
	while opcion != 0:
		opcion = menu()
		if opcion == 1:
			mostrar_votos(votos)
		elif opcion == 2:
			mat = generar_matriz(votos)
		elif opcion == 3:
			if mat is None:
				print('Debe primero generar la matriz ejecutando la opcion 2')
			else:
				va = acumular_por_candidato(mat)
				mayor = buscar_ganador(va)
				mostrar(mat, mayor, candidatos)


if __name__ == '__main__':
	principal()
