__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Alquiler:
	def __init__(self, documento, monto, tipo):
		self.documento = documento
		self.monto = monto
		self.tipo = tipo

	def __str__(self):
		cadena = 'Reseva por Documento: {:<10}'.format(self.documento)
		cadena += ' Moto a pagar: ${:<10.2f}'.format(self.monto)
		cadena += ' Tipo Cabaña: ${:<5}'.format(self.tipo)
		return cadena


def crear_alquiler(linea):
	tokens = linea.split(',')
	documento = tokens[0]
	monto = float(tokens[1])
	tipo = int(tokens[2])
	return Alquiler(documento, monto, tipo)
