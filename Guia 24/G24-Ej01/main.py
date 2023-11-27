from manejador_archivo import generar_arreglo, grabar_arreglo
from reserva import *

__author__ = 'Algoritmos y Estructuras de Datos'


def menu():
	cad = 'Menu de Opciones\n' + \
	      '=' * 80 + '\n' + \
	      '1 ----- Mostrar Arreglo de Reservas\n' + \
	      '2 ----- Agregar nuevo reserva\n' + \
	      '3 ----- Determinar total por monto de servicio\n' + \
	      '4 ----- Crear y mostrar nuevo vector de reservas\n' + \
	      '0 ----- Salir\n' + \
	      'Ingrese su opcion: '
	return int(input(cad))


def validar_rango(min, max, mensaje='Ingrese un numero: '):
	valor = min - 1
	while valor < min or valor > max:
		valor = int(input(mensaje))
		if valor < min or valor > max:
			print('Error!!!! El valor esta fuera del rango solicitado [' + str(min) + ',' + str(max) + ']')
	return valor


def validar_mayor(min, mensaje='Ingrese un numero: '):
	valor = min - 1
	while valor < min:
		valor = int(input(mensaje))
		if valor < min:
			print('Error!!!! El valor ser mayor a ' + str(min))
	return valor


def display(vector):
	print('Listado de Reservas')
	print('=' * 126)
	titulo = '{:<11} | {:<30} | {:>4} | {:<45} | {:>10} | {:>11}\n{}'
	print(titulo.format('Numero', "Nombre Cumpleañero", 'Edad', 'T. Scio', 'Cant Inv.', 'Monto', '=' * 126))

	for elem in vector:
		print(elem)


def existe(vector, num_reserva):
	existe = False
	for elem in vector:
		if elem.numero == num_reserva:
			existe = True
			break
	return existe


def agregar_nueva_reserva(vector):
	numero = input('Ingresar el nuevo numero de la reserva: ')
	if not existe(vector, numero):
		nombre = input('Ingrese el nombre del cumpleañero: ')
		edad = validar_rango(0, 13, 'Ingrese la edad del cumpleañero: ')
		tipo_servicio = validar_rango(0, 3, 'Ingrese el tipo de servicio a prestar: ')
		invitados = validar_mayor(0, 'Ingrese la cantidad de invitados: ')
		monto = validar_mayor(0, 'Ingrese el monto a abonar por la fiesta: ')
		reserva = Reserva(numero, nombre, edad, tipo_servicio, invitados, monto)
		vector.append(reserva)


def acumular_por_tipo(vector):
	va = [0] * 4
	for res in vector:
		va[res.tipo_servicio] += res.monto
	return va


def buscar_mayor_tipo_servicio(vector):
	mayor_tipo = 0
	monto_mayor = vector[0]
	for i in range(len(vector)):
		if vector[i] > monto_mayor:
			monto_mayor, mayor_tipo = vector[i], i
	return mayor_tipo


def mostrar_acumulados(vector, may_tipo_servicio):
	print('Acumulados por Tipo de Servicio')
	print('=' * 65)
	print('{:<45} | {:>15}'.format('Descripcion Tipo', 'Acumulado'))
	print('=' * 65)
	for i in range(len(vector)):
		cad = '{:<45} | S{:>15.2f}'.format(descripcion_servicio(i), vector[i])
		print(cad)
	print('El tipo de servicio que mas recaudo fue', descripcion_servicio(may_tipo_servicio))


def generar_nuevo_por_edad_monto(reservas, edad, invitados):
	vector = []
	for res in reservas:
		if res.edad > edad and res.invitados > invitados:
			vector.append(res)
	return vector


def principal():
	opcion = -1
	reservas = generar_arreglo()
	while opcion != 0:
		print()
		opcion = menu()
		if opcion == 1:
			display(reservas)
		elif opcion == 2:
			agregar_nueva_reserva(reservas)
		elif opcion == 3:
			va = acumular_por_tipo(reservas)
			may_tipo_servicio = buscar_mayor_tipo_servicio(va)
			mostrar_acumulados(va, may_tipo_servicio)
		elif opcion == 4:
			edad = validar_rango(0, 13, 'Ingrese la edad del cumpleañero: ')
			invitados = validar_mayor(0, 'Ingrese la cantidad de invitados: ')
			vector = generar_nuevo_por_edad_monto(reservas, edad, invitados)
			display(vector)
		elif opcion == 0:
			print('Fin del Programa')
			grabar_arreglo(reservas)


if __name__ == '__main__':
	principal()
