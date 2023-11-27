__author__ = 'Algoritmos y Estructuras de Datos'

import random
import string


class Alquiler:
	def __init__(self, numero, nombre, cantidad_personas, tipo_residencia, monto, cantidad_dias):
		self.numero = numero
		self.nombre = nombre
		self.cantidad_personas = cantidad_personas
		self.tipo_residencia = tipo_residencia
		self.monto = monto
		self.cantidad_dias = cantidad_dias

	def __str__(self):
		cad = '{:<8} | {:<30} | {:^10} | {:<20} | ${:>10.2f} | {:>4}'
		return cad.format(self.numero, self.nombre, self.cantidad_personas,
		                  descripcion_tipo_residencia(self.tipo_residencia), self.monto, self.cantidad_dias)

	def to_lineacsv(self):
		cad = '{},{},{},{},{},{}'
		return cad.format(self.numero, self.nombre, self.cantidad_personas,
		                  self.tipo_residencia, self.monto, self.cantidad_dias)


def descripcion_tipo_residencia(tipo):
	nombres = ('Departamento', 'Cabaña', 'Hotel Spa', 'Casa', 'Chalet', 'Hosteria')
	return nombres[tipo]


def generar_numero_alquiler():
	numero = ''
	for i in range(8):
		numero += random.choice(string.ascii_uppercase + string.digits)
	return numero


def str_toalquiler(linea):
	token = linea.split(',')
	numero = token[0]
	nombre = token[1]
	cantidad = int(token[2])
	tipo = int(token[3])
	monto = float(token[4])
	dias = int(token[5])
	return Alquiler(numero, nombre, cantidad, tipo, monto, dias)
