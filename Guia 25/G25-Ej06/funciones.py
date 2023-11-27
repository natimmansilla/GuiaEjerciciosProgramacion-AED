__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os
import pickle

from registro import *


def generar_achivo_binario(vector, archivo):
	m = open(archivo, 'wb')

	for consulta in vector:
		if consulta.especie != 3 or consulta.especie != 7:
			pickle.dump(consulta, m)

	m.close()


def leer_archivo(archivo):
	if not os.path.exists(archivo):
		print('Archivo inexistente.....')

	m = open(archivo, 'rb')
	size = os.path.getsize(archivo)
	while m.tell() < size:
		consulta = pickle.load(m)
		print(consulta)

	m.close()


def mostrar_consultas(vector):
	encabezado = '| {:<93} |\n| {:^93} |\n| {:<93} |'
	print(encabezado.format('=' * 93, 'Menu de Opciones', '=' * 93))
	for consulta in vector:
		print(consulta)


def add_in_order(vector, registro):
	n = len(vector)
	izq = 0
	der = n - 1
	pos = 0
	while izq <= der:
		c = (izq + der) // 2
		if vector[c].nombre_propietario == registro.nombre_propietario:
			pos = c
			break

		if registro.nombre_propietario < vector[c].nombre_propietario:
			der = c - 1
		else:
			izq = c + 1

	if izq > der:
		pos = izq

	vector[pos:pos] = [registro]


def cargar_vector(archivo):
	vector = []
	if not os.path.exists(archivo):
		print('No existe el archivo!!')
		return vector

	texto = open(archivo, 'rt')
	num_linea = 0
	for linea in texto:
		if num_linea > 0:
			consulta = string_toconsulta(linea[:-1])
			add_in_order(vector, consulta)
		num_linea += 1
	texto.close()
	return vector


def buscar_binaria(vector, x):
	izq, der = 0, len(vector) - 1
	pos = -1
	while izq <= der:
		med = (izq + der) // 2
		if vector[med].nombre_propietario == x:
			pos = med
			break

		if x < vector[med].nombre_propietario:
			der = med - 1
		else:
			izq = med + 1

	return pos
