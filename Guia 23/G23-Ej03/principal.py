import os.path
import pickle
import registro

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_rango(minimo, maximo, mensaje):
	error = 'Error!!! El valor debe ser entre {} y {}. {}'.format(minimo, maximo, mensaje)
	numero = int(input(mensaje))
	while numero < minimo or numero > maximo:
		numero = int(input(error))
	return numero


def generar_cobro():
	cuenta = input('Ingrese la cuenta del servicio a cobrar: ')
	tipo = validar_rango(1, 15, 'Ingresar el tipo de Servicio: ')
	dia = validar_rango(1, 31, 'Ingresar el dia en que se Cobro el Servicio: ')
	monto = float(input('Ingrese el monto cobrado: '))
	return registro.Cobro(cuenta, dia, tipo, monto)


def grabar_cobro(cobro, archivo):
	file = open(archivo, 'ab')
	pickle.dump(cobro, file)
	file.flush()
	file.close()


def calcular_total_cuenta(cuenta, fd):
	total = 0
	size = os.path.getsize(fd)
	if size == 0:
		return False, total

	m = open(fd, 'rb')
	while m.tell() < size:
		cobro = pickle.load(m)
		if cobro.cuenta == cuenta:
			total += cobro.monto

	m.close()
	return True, total


def generar_matriz(fd):
	if not os.path.exists(fd):
		return []

	matriz = [[0] * 31 for i in range(15)]
	m = open(fd, 'rb')
	size = os.path.getsize(fd)
	while m.tell() < size:
		cobro = pickle.load(m)
		matriz[cobro.tipo - 1][cobro.dia - 1] += cobro.monto
	m.close()
	return matriz


def mostrar_matriz(matriz):
	tc = len(matriz[0])
	tf = len(matriz)
	celda = '|{:^8}'
	listado = celda.format('')
	for i in range(1, tc + 1):
		listado += celda.format('Dia ' + str(i + 1))

	for i in range(tf):
		listado += '\n' + celda.format('Tipo ' + str(i + 1))
		for j in range(tc):
			listado += celda.format(matriz[i][j])

	return listado


def totalizar_dia(columna, matriz):
	total = 0
	for f in range(len(matriz)):
		total += matriz[f][columna]
	return total


def mayor_dia_con_cobros(matriz):
	tc = len(matriz[0])
	mayor = totalizar_dia(0, matriz)
	dia = 0
	for c in range(1, tc):
		total = totalizar_dia(c, matriz)
		if mayor < total:
			mayor = total
			dia = c
	return dia


def totalizar_por_servicio(tipo, matriz):
	total = 0
	for c in range(len(matriz[tipo])):
		total += matriz[tipo][c]
	return total / len(matriz[tipo])


def principal():
	fd = 'cobros.dat'
	menu = 'Menu de Opciones\n' \
	       '====================================================\n' \
	       '1 - Cargar un Cobro en el Archivo\n' \
	       '2 - Determinar Total Cobrado a Cuenta\n' \
	       '3 - Determinar el Monto por Tipo Servicio y Dia\n' \
	       '4 - Determinar dia con mayor monto\n' \
	       '5 - Determinar Promedio Cobrado por Tipo de Servicio\n' \
	       '6 - Salir\n' \
	       'Ingrese su opcion: '

	matriz = []
	opcion = 0
	while opcion != 6:
		opcion = int(input(menu))
		if opcion == 1:
			cobro = generar_cobro()
			grabar_cobro(cobro, fd)

		elif opcion == 2:
			cuenta = input('Ingrese el numero de cuenta a totalizar: ')
			res, total = calcular_total_cuenta(cuenta, fd)
			if res:
				print('El total cobrado a la cuenta ingresada fue de $', total)
			else:
				print('El Archivo no existe o no tiene registros de cobros')

		elif opcion == 3:
			matriz = generar_matriz(fd)
			if len(matriz) > 0:
				print(mostrar_matriz(matriz))
			else:
				print('No se ha generado la matriz')

		elif opcion == 4:
			dia = mayor_dia_con_cobros(matriz)
			print('El dia con mayor monto cobrado fue', dia + 1)

		elif opcion == 5:
			tipo = validar_rango(1, 15, 'Ingrese el tipo de servicio a promediar: ')
			promedio = totalizar_por_servicio(tipo, matriz)
			print('El promedio cobrado para el tipo', tipo, 'fue de $', round(promedio, 2))


if __name__ == '__main__':
	principal()
