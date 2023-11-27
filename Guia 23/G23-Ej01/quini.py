__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import pickle


def validar_entre(mensaje, desde, hasta):
	num = int(input(mensaje))
	while num < desde or num > hasta:
		print('Debe ser un valor entre', desde, 'y', hasta)
		num = int(input(mensaje))
	return num


def ordenar_ascendente(v):
	for i in range(len(v) - 1):
		for j in range(i + 1, len(v)):
			if v[i] > v[j]:
				v[i], v[j] = v[j], v[i]


def cargar_sorteo():
	v = [0] * 6
	for i in range(len(v)):
		v[i] = validar_entre('Ingrese el ' + str(i + 1) + '° número: ', 0, 36)
	ordenar_ascendente(v)
	m = open("extracto.dat", "wb")
	pickle.dump(v, m)
	m.close()


def mostrar_extracto():
	archivo = 'extracto.dat'
	m = open(archivo, 'rb')
	v = pickle.load(m)
	print(v)
	m.close()


def principal():
	opcion = -1
	while opcion != 0:
		print('*' * 80)
		print('Sorteo Quini 6')
		print('====================')
		print('1 - Cargar sorteo')
		print('2 - Consultar')
		print('0 - Salir')
		opcion = int(input('Ingrese opción: '))

		if opcion == 1:
			cargar_sorteo()
			print('Sorteo cargado!')
		elif opcion == 2:
			mostrar_extracto()

		print('*' * 80)


if __name__ == '__main__':
	principal()
