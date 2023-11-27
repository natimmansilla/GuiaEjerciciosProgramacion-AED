__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os.path
import pickle

from gasto import crear_gasto


def mostrar_menu():
	print("\nMenu de opciones:")
	print("1.Cargar gastos (en vector)")
	print("2.Mostrar gastos (vector)")
	print("3.Generar archivo de gastos (a partir del vector)")
	print("4.Mostrar archivo de gastos")
	print("5.Gasto total por mes y sucursal(generacion de matriz a partir del archivo)")
	print("6.Gasto total por mes (a partir de la matriz generada)")
	print("0.SALIR")


def validar_mayor_que(min, mensaje='Ingrese un numero: '):
	n = min
	while n <= min:
		n = int(input(mensaje))
		if n <= min:
			print(f'Error!!! El valor ingresado debe ser mayor a {min}')
	return n


def add_in_order(vec, reg):
	izq, der = 0, len(vec) - 1
	pos = -1
	while izq <= der:
		med = (izq + der) // 2
		if vec[med].codigo == reg.codigo:
			pos = med
			break

		if reg.codigo < vec[med].codigo:
			der = med - 1
		else:
			izq = med + 1

	if izq > der:
		pos = izq

	vec[pos:pos] = [reg]


def generar_gastos(gastos_csv):
	if not os.path.exists(gastos_csv):
		print('No se puede generar los gastos en un vector porque el archivo no existe')
		return

	vec = []
	lineas = open(gastos_csv, "rt")
	encabezado = True
	for linea in lineas:
		if encabezado:
			encabezado = False
			continue
		reg = crear_gasto(linea)
		add_in_order(vec, reg)

	return vec


def mostrar_listado_gastos(v):
	print("Codigo Descripcion Mes Sucursal Importe")
	print("-" * 50)
	for gasto in v:
		print(gasto)
	print("-" * 50)


def grabar_archivo(v, fd, ref):
	m = open(fd, 'wb')
	for i in range(0, len(v)):
		if v[i].importe > ref:
			pickle.dump(v[i], m)
	m.close()


def mostrar_archivo(fd):
	tam_arch = os.path.getsize(fd)
	arch = open(fd, 'rb')
	while arch.tell() < tam_arch:
		gasto = pickle.load(arch)
		print(gasto)
	arch.close()


def importe_total_por_mes_sucursal(fd):
	mat = 12 * [0]
	for i in range(0, 12):
		mat[i] = 3 * [0]
	tam_arch = os.path.getsize(fd)
	arch = open(fd, 'rb')
	while arch.tell() < tam_arch:
		gasto = pickle.load(arch)
		mes = gasto.mes - 1
		suc = gasto.sucursal
		mat[mes][suc] += gasto.importe
	arch.close()
	return mat


def mostrar_matriz(mat):
	for i in range(0, len(mat)):
		print("")
		for j in range(0, len(mat[i])):
			print("Mes: ", (i + 1), "Sucursal: ", (j), "- Gasto total: $", '{:.2f}'.format(mat[i][j]))


def totalizar_costos_mes(mat, mes):
	total = 0
	for i in range(len(mat[mes - 1])):
		total += mat[mes - 1][i]
	return total


def main():
	arreglo_generado = False
	nombre_archivo = "gastos.dat"

	opc = -1
	while opc != 0:
		mostrar_menu()
		opc = int(input("Ingrese su eleccion:"))
		if opc == 1:
			vec = generar_gastos('gastos.csv')
			arreglo_generado = True
			print("Gastos generados.")
		elif opc == 2:
			if arreglo_generado:
				mostrar_listado_gastos(vec)
			else:
				print("\nPrimero debe cargar los gastos!")
		elif opc == 3:
			if arreglo_generado:
				ref = float(input("Ingrese el importe de referencia para generar el archivo de gastos: "))
				grabar_archivo(vec, nombre_archivo, ref)
				print("\nArchivo generado!")
			else:
				print("\nPrimero debe cargar los gastos!")
		elif opc == 4:
			if os.path.exists(nombre_archivo):
				mostrar_archivo(nombre_archivo)
			else:
				print("\nPrimero debe generar el archivo!")
		elif opc == 5:
			if os.path.exists(nombre_archivo):
				mat = importe_total_por_mes_sucursal(nombre_archivo)
				mostrar_matriz(mat)
			else:
				print("\nPrimero debe generar el archivo!")
		elif opc == 6:
			if os.path.exists(nombre_archivo):
				mes = 0
				while mes < 1 or mes > 12:
					mes = int(input("Ingrese el mes sobre el que quiere totalizar los gastos:"))
				mat = importe_total_por_mes_sucursal(nombre_archivo)
				total = totalizar_costos_mes(mat, mes)
				print("El gasto total durante el mes ", mes, " es de: $", total)
			else:
				print("\nPrimero debe generar el archivo!")
		elif opc == 0:
			print("--- Programa finalizado ---")


if __name__ == "__main__":
	main()
