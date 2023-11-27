__author__ = 'Algoritmos y Estructuras de Datos'

import random
import string


class Pago:
	def __init__(self, numero, nombre, tipo_empleo, tipo_producto, monto_pagar, gastos):
		self.numero = numero
		self.nombre = nombre
		self.tipo_empleo = tipo_empleo
		self.tipo_producto = tipo_producto
		self.monto_pagar = monto_pagar
		self.gastos = gastos

	def __str__(self):
		cad = '{:<24} | {:<30} | {:<15} | {:<15} | {:>10.2f} | {:>10.2f}'
		tipo_prod = descripcion_tipo_producto(self.tipo_producto)
		tipo_emp = descripcion_tipo_empleo(self.tipo_empleo)
		return cad.format(self.numero, self.nombre, tipo_emp, tipo_prod, self.monto_pagar, self.gastos)

	def to_lineacsv(self):
		cad = '{},{},{},{},{},{}'
		return cad.format(self.numero, self.nombre, self.tipo_empleo, self.tipo_producto,
		                  self.monto_pagar, self.gastos)


def descripcion_tipo_empleo(tipo):
	tipos = ('Director', 'Productor', 'Maquillador', 'Actor', 'Asistentes', 'Especalista CGI', 'Vestuarista')
	return tipos[tipo]


def descripcion_tipo_producto(tipo):
	tipos = ('Pelicula', 'Serie', 'Documental', 'Videojuego', 'Corto Anmacion')
	return tipos[tipo - 1]


def separar_tokens(linea, separador=','):
	t = []
	# 614894fefc13ae6e0e01931f,Albert Meharg,5,1,8725.57,4471.68
	pos_separador = 0
	for i in range(len(linea)):
		if linea[i] == separador:
			pos_separador = i
			valor = linea[initial_pos: pos_separador]
			t.append(valor)
			initial_pos = pos_separador + 1

	if initial_pos < len(linea):
		valor = linea[initial_pos:]
		t.append(valor)

	return t


def str_topago(linea):
	token = separar_tokens(linea)  # linea.split(',')
	numero = token[0]
	nombre = token[1]
	tipo_empleo = int(token[2])
	tipo_producto = int(token[3])
	monto_pagar = float(token[4])
	gastos = float(token[5])
	return Pago(numero, nombre, tipo_empleo, tipo_producto, monto_pagar, gastos)


def crear_numero_pago():
	numero = ''
	for i in range(24):
		numero += random.choice(string.ascii_lowercase + string.digits)
	return numero
