__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import os.path
import pickle
import random

from clases import *


def mostrar_menu():
	print('=' * 80)
	print('ZAPATERÍA')
	print('1. Generar vector')
	print('2. Mostrar vector')
	print('3. Generar archivo')
	print('4. Mostrar archivo')
	print('0. Salir')
	op = int(input('\nIngrese opcion: '))
	return op
	print('=' * 80)


def validar_mayor_que(inf, mensaje):
	num = int(input(mensaje))
	while num <= inf:
		num = int(input('Error! ' + mensaje))
	return num


def generar_vector(n):
	v = []
	colores = ('rojo', 'naranja', 'amarillo', 'verde', 'azul', 'violeta', 'blanco', 'negro', 'dorado', 'plateado')
	for i in range(n):
		codigo = random.randint(1000, 5000)
		color = random.choice(colores)
		talle = random.randint(20, 45)
		v.append(Calzado(codigo, talle, color))
	return v


def mostrar_vector(v):
	for i in range(len(v)):
		print(v[i])


def generar_archivo(v, fd):
	m = open(fd, 'wb')
	for i in range(len(v)):
		pickle.dump(v[i], m)
	m.close()


def ordenar_por_codigo(v):
	n = len(v)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if v[i].codigo > v[j].codigo:
				v[i], v[j] = v[j], v[i]


def mostrar_archivo(fd):
	if not os.path.exists(fd):
		print('El archivo', fd, 'no existe')
	else:
		n = os.path.getsize(fd)
		m = open(fd, 'rb')
		while m.tell() < n:
			x = pickle.load(m)
			print(x)
		m.close()


def principal():
	v = []
	fd = 'catalogo.dat'
	opcion = -1
	while opcion != 0:
		opcion = mostrar_menu()
		if opcion == 1:
			n = validar_mayor_que(0, 'Ingrese cantidad de artículos: ')
			v = generar_vector(n)
		elif opcion == 2:
			if len(v) == 0:
				print('El vector no se ha cargado')
			else:
				mostrar_vector(v)
		elif opcion == 3:
			if len(v) == 0:
				print('El vector no se ha cargado')
			else:
				ordenar_por_codigo(v)
				generar_archivo(v, fd)
		elif opcion == 4:
			mostrar_archivo(fd)


if __name__ == '__main__':
	principal()
