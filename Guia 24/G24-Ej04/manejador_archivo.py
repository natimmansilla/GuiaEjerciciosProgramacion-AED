__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os.path
import pickle

import registro


def generar_arreglo(archivo):
	vec = []

	if not os.path.exists(archivo):
		print('El archivo que desea cargar no existe')
		return

	archivo_texto = open(archivo, 'rt')
	num_linea = 0
	for linea in archivo_texto:
		if num_linea > 0:
			figurita = registro.str_tofigurita(linea)
			vec.append(figurita)
		num_linea += 1
	archivo_texto.close()

	return vec


def guardar_arreglo(vector, archivo, sep=','):
	primera_linea = 'Nombre,Pais,Numero,Posicion,ValorCanje'

	archivo_texto = open(archivo, 'wt')
	archivo_texto.write(primera_linea)
	for figurita in vector:
		linea = figurita.figurita_tostr()
		archivo_texto.write(linea)
	archivo_texto.close()


def generar_binario(vector, valor, archivo):
	m = open(archivo, 'wb')
	for figurita in vector:
		if figurita.valor_canje >= valor:
			pickle.dump(figurita, m)
	m.close()


def mostrar_archivo_binario(archivo, encabezado='Listado de Registros'):
	if not os.path.exists(archivo):
		print('El archivo que desea mostrar no existe')
		return

	m = open(archivo, 'rb')
	print(encabezado)
	size = os.path.getsize(archivo)
	while m.tell() < size:
		figurita = pickle.load(m)
		print(figurita)
	m.close()
