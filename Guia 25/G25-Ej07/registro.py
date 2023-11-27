__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from random import choice


class Operacion:
	def __init__(self, codigo, comprador, monto_venta, marca, modelo):
		self.codigo = codigo
		self.comprador = comprador
		self.monto_venta = monto_venta
		self.marca = marca
		self.modelo = modelo

	def __str__(self):
		sep = '-'
		cadena = f'| {self.codigo:<10} | {self.comprador:<30} | ${self.monto_venta:>10.2f} ' \
		         f'| {self.marca:^6} | {self.modelo:^6} |\n{sep * 79:<79}'
		return cadena


def encabezado():
	cadena = '| {:<77} |\n| {:<10} | {:<30} | {:<11} | {:^6} | {:^6} |\n| {:<77} |\n'
	return cadena.format('=' * 77, 'Codigo', 'Comprador', 'Monto Vta.', 'Marca', 'Modelo', '=' * 77)


def generar_nombre_comprador():
	nombre = 'Juan', 'Carlos', 'Ernesto', 'Karina', 'Laura', 'Guada', 'Joaquin', 'German', 'Ignacio'
	apellido = 'Smith', 'Gallego', 'Vazco', 'Tano', 'Turco', 'Zombi', 'Valeryon', 'Stark', 'Baratheon'
	return f'{choice(nombre)} {choice(apellido)}'
