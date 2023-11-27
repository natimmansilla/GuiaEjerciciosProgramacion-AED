__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os.path
import pickle
import random
import registro


def generar_vector(origen_info):
	if not os.path.exists(origen_info):
		print(f'No se puede crear el arreglo porque no existe el archivo {origen_info}')
		return

	vector = []
	alquileres = open(origen_info, 'rt')
	primer_linea = True
	for linea in alquileres:
		if primer_linea:
			primer_linea = False
			continue
		alquiler = registro.crear_alquiler(linea)
		vector.append(alquiler)
	alquileres.close()
	return vector


def generar_archivo(vector, monto, archivo):
	arch = open(archivo, 'wb')
	for cabaña in vector:
		if cabaña.monto > monto:
			pickle.dump(cabaña, arch)
	arch.flush()
	arch.close()


def leer_archivo(archivo):
	size = os.path.getsize(archivo)
	if size < 0:
		return None

	arch = open(archivo, 'rb')
	vc = [0] * 10
	while arch.tell() < size:
		cabaña = pickle.load(arch)
		vc[cabaña.tipo] += cabaña.monto

	arch.close()
	return vc


def principal():
	menu = 'Menu de Opciones \n' \
	       '===================================== \n' \
	       '1 - Cargar Arreglo de Reservas \n' \
	       '2 - Grabar Archivo por Monto \n' \
	       '3 - Mostrar Archivo \n' \
	       '0 - Salir\n' \
	       'Ingrese la opcion: '

	nombre_archivo = 'reservas.dat'
	opcion = -1
	vector = []
	while opcion != 0:
		opcion = int(input(menu))
		if opcion == 1:
			origen_info = 'alquileres.csv'
			vector = generar_vector(origen_info)

		elif opcion == 2:
			monto = float(input('Ingrese el monto minimo para guardar: '))
			generar_archivo(vector, monto, nombre_archivo)

		elif opcion == 3:
			listado = leer_archivo(nombre_archivo)
			if not listado is None:
				for i in range(len(listado)):
					print('Tipo de Cabaña ', i, 'recaudo $', listado[i])
			else:
				print('El Archivo no tiene Registros')


if __name__ == '__main__':
	principal()
