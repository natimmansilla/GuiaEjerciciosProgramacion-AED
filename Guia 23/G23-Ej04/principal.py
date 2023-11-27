import os.path
import pickle
import random

from contacto import *

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def menu():
	print('Menu de Opciones')
	print('=' * 60)
	print('1 \t Cargar Archivo por Teclado')
	print('2 \t Mostrar Archivo')
	print('3 \t Generar Vector de contactos')
	print('4 \t Salir')
	return int(input('Ingrese su opcion: '))


def generar_archivo(archivo, n):
	m = open(archivo, 'wb')
	for i in range(n):
		nombre = input('Ingrese el nombre del contacto: ')
		apellido = input('Ingrese el apellido del contacto: ')
		telefono = input('Ingrese el telefono del contacto: ')
		mail = input('Ingrese el mail del contacto: ')
		entrada_agenda = Contacto(nombre, apellido, mail, telefono)
		pickle.dump(entrada_agenda)
	m.flush()
	m.close()


def generar_archivo_random(archivo, n):
	nombres = ('Carlos', 'Juan', 'Esteban', 'Jazmin', 'Serio', 'Luis', 'German')
	apellidos = ('Garcia', 'Perez', 'Lopez', 'Martinez', 'Prueba', 'Pruebon', 'Pruebita')
	m = open(archivo, 'wb')
	for i in range(n):
		nombre = random.choice(nombres)
		apellido = random.choice(apellidos)
		telefono = '035' + str(random.randint(0, 9)) + str(random.randint(100000, 999999))
		mail = nombre + '.' + apellido + '@test.com'
		entrada_agenda = Contacto(nombre, apellido, mail, telefono)
		pickle.dump(entrada_agenda, m)
	m.flush()
	m.close()


def validar_mayor(minimo, mensage):
	valor = int(input(mensage))
	while valor <= minimo:
		print('El valor es incorrecto!!! Debe ser mayor a', minimo)
		valor = int(input(mensage))
	return valor


def mostrar_archivo(archivo):
	size = os.path.getsize(archivo)
	if size <= 0:
		return 'No hay registrool para mostrar'

	listado = 'Listado de Contactos de la Agenda. \n{}'.format('=' * 110)
	listado += '\n{:<30} {:<30} {:<15} {:<30}'.format('Nombre', 'Apellido', 'Telefono', 'Email')
	listado += '\n{}'.format('-' * 110)
	m = open(archivo, 'rb')
	while m.tell() < size:
		contacto = pickle.load(m)
		listado += '\n' + str(contacto)
	m.close()
	return listado


def generar_vector(archivo):
	vector = []
	size = os.path.getsize(archivo)
	if size <= 0:
		return vector

	m = open(archivo, 'rb')
	while m.tell() < size:
		contacto = pickle.load(m)
		vector.append(contacto)
	m.close()
	return vector


def mostrar_vector(vector):
	listado = 'Listado de Contactos de la Agenda. \n{}'.format('=' * 110)
	listado += '\n{:<30} {:<30} {:<15} {:<30}'.format('Nombre', 'Apellido', 'Telefono', 'Email')
	listado += '\n{}'.format('-' * 110)
	for contacto in vector:
		listado += '\n' + str(contacto)
	return listado


def principal():
	print('Generacion de Agenda')
	archivo = 'contactos.dat'

	opcion = -1
	while opcion != 4:
		opcion = menu()
		print()
		if opcion == 1:
			tam = validar_mayor(0, 'Ingrese la cantidad de contactos: ')
			rand = input('Desea agregar contactos en forma aleatoria (S/N): ')
			if rand == 'S':
				generar_archivo_random(archivo, tam)
			else:
				generar_archivo(archivo, tam)

		elif opcion == 2:
			listado = mostrar_archivo(archivo)
			print(listado)

		elif opcion == 3:
			vector = generar_vector(archivo)
			print(mostrar_vector(vector))
		print('\n\n')


if __name__ == '__main__':
	principal()
