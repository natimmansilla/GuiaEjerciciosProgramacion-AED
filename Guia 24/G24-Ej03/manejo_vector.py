__author__ = 'Algoritmos y Estructuras de Datos'

import registro


def add_in_order(vector, registro):
	tam = len(vector)
	izq, der = 0, tam - 1
	pos = tam
	while izq <= der:
		med = (izq + der) // 2
		if vector[med].numero == registro.numero:
			pos = med
			break

		if registro.numero < vector[med].numero:
			der = med - 1
		else:
			izq = med + 1

	if izq > der:
		pos = izq

	vector[pos:pos] = [registro]


def mostrar_vector(pagos):
	cad = '|{:<24} | {:<30} | {:<15} | {:<15} | {:>11} | {:>11} |\n'
	titulo = '_' * 120 + '\n'
	titulo += cad.format('Numero', 'Nombre', 'Tipo Empleo', 'Tipo Producto', 'Mto Pagar', 'Gastos')
	titulo += '_' * 120 + '\n'
	for pago in pagos:
		titulo += '|' + str(pago) + ' |\n'
	titulo += '_' * 120 + '\n'
	print(titulo)


def buscar_pago(pagos, x):
	tam = len(pagos)
	izq, der = 0, tam - 1

	while izq <= der:
		med = (izq + der) // 2
		if pagos[med].numero == x:
			return med

		if x < pagos[med].numero:
			der = med - 1
		else:
			izq = med + 1
	return -1


def promediar_netos_pagar(vector):
	total = 0
	tam = len(vector)
	for pago in vector:
		total += pago.monto_pagar - pago.gastos

	return total / tam


def buscar_pago_por_nombre(vector, nombre):
	pos = -1
	for i in range(len(vector)):
		if vector[i].nombre == nombre:
			pos = i
			break
	return pos
