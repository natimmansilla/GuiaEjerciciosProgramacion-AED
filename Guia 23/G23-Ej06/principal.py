import os
import pickle

from registro import *


def leer_archivo(fd):
	v = []
	if not os.path.exists(fd):
		print('El archivo', fd, 'no existe')
	else:
		m = open(fd, 'rb')
		size = os.path.getsize(fd)
		while m.tell() < size:
			v.append(pickle.load(m))
		m.close()
	return v


def mostrar_vector(v):
	print(to_string_titulos())
	for cuota in v:
		print(cuota)


def buscar_secuencial(v, socio, deporte):
	for i in range(len(v)):
		if v[i].socio == socio and v[i].deporte == deporte:
			return i
	return -1


def mostrar_menu():
	cadena = '=======================================\n' \
	         'Menu Club Deportivo \n' \
	         '=======================================\n' \
	         '1 - Consultar el contenido del vector\n' \
	         '2 - Realizar un cobro (busqueda)\n' \
	         '3 - Generar csv de Morosos\n' \
	         '4 - Totalizar cobros por deporte\n' \
	         '5 - Grabar contenido en memoria\n' \
	         '0 - Salir\n' \
	         'Ingrese su opcion: '
	return int(input(cadena))


def validar_entre(minimo, maximo, mensaje):
	num = int(input(mensaje))
	while num < minimo or num > maximo:
		print(f'Error!!! El número ingresado debe estar entre {minimo} y {maximo} incluídos')
		num = int(input(mensaje))
	return num


def contar_por_deporte(v):
	cd = [0] * 5
	for cuota in v:
		cd[cuota.deporte] += 1
	return cd


def buscar_mayor(cd):
	may = 0
	for i in range(1, len(cd)):
		if cd[i] > cd[may]:
			may = i
	return may


def generar_archivo_morosos(v):
	m = open('morosos.csv', 'wt')
	for cuota in v:
		if cuota.dia == 0:
			m.write(cuota.to_str_csv() + '\n')
	m.close()


def grabar_vector(v, fd):
	m = open(fd, 'wb')
	for cuota in v:
		pickle.dump(cuota, m)
	m.close()


def principal():
	v = leer_archivo('cuotas.dat')

	if len(v) == 0:
		print('El vector no se pudo cargar')
	else:
		opcion = -1
		while opcion != 0:
			opcion = mostrar_menu()

			if opcion == 1:
				mostrar_vector(v)
			elif opcion == 2:
				socio = int(input('Ingrese socio: '))
				deporte = validar_entre(0, 4, 'Ingrese deporte (0-4): ')
				dia = int(input('Ingrese dia: '))
				valor = int(input('Ingrese monto a cobrar $: '))
				pos = buscar_secuencial(v, socio, deporte)
				if pos == -1:
					v.append(Cuota(socio, deporte, dia, valor))
					print('Se agrego un nuevo registro')
				else:
					v[pos].dia = dia
					v[pos].valor = valor
					print('Se registró el pago')
			elif opcion == 3:
				generar_archivo_morosos(v)
				print('Archivo generado')
			elif opcion == 4:
				cd = contar_por_deporte(v)
				may = buscar_mayor(cd)
				print('El deporte con más socios es', describir_deporte(may))
			elif opcion == 5:
				grabar_vector(v, 'cuotas.dat')



if __name__ == '__main__':
	principal()
