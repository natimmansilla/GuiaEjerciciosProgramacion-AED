__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os
import pickle
import random

import registro


def add_in_order(v, reg):
	izq, der = 0, len(v) - 1
	while izq <= der:
		c = (izq + der) // 2
		if v[c].dni == reg.dni:
			pos = c
			break
		if reg.dni < v[c].dni:
			der = c - 1
		else:
			izq = c + 1
	if izq > der:
		pos = izq
	v[pos:pos] = [reg]


def cargar_vector(fd):
	v = list()
	if not os.path.exists(fd):
		print('El archivo', fd, 'no existe')
		return v

	m = open(fd, 'rt')
	for linea in m:
		reg = registro.csv_to_aspirante(linea)
		add_in_order(v, reg)
	return v


def mostrar_vector(v):
	for i in range(len(v)):
		print(v[i])


def mostrar_menu():
	print('\nMENÚ DE OPCIONES')
	print('1. Mostrar')
	print('2. Contar')
	print('3. Asignar vacantes')
	print('4. Buscar por DNI')
	print('0. Salir')


def contar_por_nota(v):
	conteo = [0] * 7
	for reg in v:
		conteo[reg.nota - 4] += 1
	return conteo


def mostrar_conteo(conteo):
	for i in range(len(conteo)):
		print('Nota', i + 4, ':', conteo[i], 'Aspirantes')


def validar_entre(inf, sup, mensaje):
	num = int(input(mensaje))
	while num < inf or num > sup:
		print('Error! Debe se un valor entre', inf, 'y', sup)
		num = int(input(mensaje))
	return num


def filtrar_por_nota(v):
	mejores, otros = [], []
	for reg in v:
		if reg.nota >= 9:
			mejores.append(reg)
		else:
			otros.append(reg)
	return mejores, otros


def sortear(v, cant, ingresantes):
	for i in range(cant):
		pos = random.randrange(0, len(v))
		ingresantes.append(v[pos])
		del (v[pos])


def asignar_vacantes(v, vacantes):
	ingresantes = []
	mejores, otros = filtrar_por_nota(v)
	if len(mejores) <= vacantes:
		ingresantes[:] = mejores[:]
		sortear(otros, vacantes - len(mejores), ingresantes)
	else:
		sortear(mejores, vacantes, ingresantes)
	return ingresantes


def buscar_binario(v, dni):
	izq, der = 0, len(v) - 1
	while izq <= der:
		c = (izq + der) // 2
		if v[c].dni == dni:
			return c
		if dni < v[c].dni:
			der = c - 1
		else:
			izq = c + 1
	return -1


def buscar_secuencial(v, dni):
	for i in range(len(v)):
		if v[i].dni == dni:
			return i
	return -1


def guardar_archivo(v, fd):
	f = open(fd, 'wb')
	for reg in v:
		pickle.dump(reg, f)
	f.close()


def principal():
	print('SISTEMA DE INSCRIPCIONES')
	fd = 'aspirantes.csv'
	aspirantes = cargar_vector(fd)
	ingresantes = []
	if len(aspirantes) == 0:
		return
	opcion = -1
	while opcion != 0:
		mostrar_menu()
		opcion = int(input('Ingrese su opcion: '))
		if opcion == 1:
			mostrar_vector(aspirantes)
		elif opcion == 2:
			conteo = contar_por_nota(aspirantes)
			mostrar_conteo(conteo)
		elif opcion == 3:
			vacantes = validar_entre(1, len(aspirantes), 'Ingrese cantidad de vacantes: ')
			ingresantes = asignar_vacantes(aspirantes, vacantes)
			print('Felicitaciones ingresantes!')
			mostrar_vector(ingresantes)
		elif opcion == 4:
			dni = input('Ingrese DNI a buscar: ')
			pos = buscar_binario(aspirantes, dni)
			if pos == -1:
				print('No existe un aspirante con ese DNI')
			else:
				print('Aspirante encontrado:', aspirantes[pos])
				if len(ingresantes) == 0:
					print('Aún no se han sorteado las vacantes')
				else:
					pos = buscar_secuencial(ingresantes, dni)
					if pos == -1:
						print('No se encuentra entre los ingresantes')
					else:
						print('Es un nuevo ingresante. Felicitaciones!')
		elif opcion == 0:
			if len(ingresantes) > 0:
				guardar_archivo(ingresantes, 'ingresantes.dat')
				print('Se guardó la lista de ingresantes')
			print('Hasta luego')


if __name__ == '__main__':
	principal()
