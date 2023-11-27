__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Viaje:
	def __init__(self, numero, chofer, costo, origen, destino, tipo_servicio):
		self.numero = numero
		self.chofer = chofer
		self.costo = costo
		self.origen = origen
		self.destino = destino
		self.tipo_servicio = tipo_servicio

	def __str__(self):
		cadena = 'Viaje Numero {:<10}'.format(self.numero)
		cadena += '- Chofer: {:<20}'.format(self.chofer)
		cadena += ' - Origen: {:<2}'.format(self.origen)
		cadena += ' - Destino: {:<2}'.format(self.destino)
		cadena += ' - Servicio: {:<2}'.format(self.tipo_servicio)
		cadena += ' - Costo: {:<8}'.format(self.costo)
		return cadena
