__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Consulta:
	def __init__(self, nombre_propietario, nombre_mascota, especie, tipo_atencion, costo):
		self.nombre_propietario = nombre_propietario
		self.nombre_mascota = nombre_mascota
		self.especie = especie
		self.tipo_atencion = tipo_atencion
		self.costo = costo

	def __str__(self):
		cadena = f'| {self.nombre_propietario:<30} | {self.nombre_mascota:<30} ' \
		         f'| {self.especie:<5} | {self.tipo_atencion:<5} | ${self.costo:<10.2f} |\n ' \
		         f'{"-" * 95:<95}'
		return cadena

	def tocsv_line(self):
		cadena = f'{self.nombre_propietario},{self.nombre_mascota},{self.especie},' \
		         f'{self.tipo_atencion},{self.costo}\n'
		return cadena


def string_toconsulta(linea, sep=','):
	tokens = linea.split(sep)
	prop = tokens[0]
	mascota = tokens[1]
	especie = int(tokens[2])
	atencion = int(tokens[3])
	costo = float(tokens[4])
	return Consulta(prop, mascota, especie, atencion, costo)
