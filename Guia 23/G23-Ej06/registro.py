__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

DEPORTES = ['Natacion', 'Basquet', 'Karate', 'Futbol', 'Patin']


class Cuota:
	def __init__(self, socio, deporte, dia, valor_cuota):
		self.socio = socio
		self.deporte = deporte
		self.dia = dia
		self.valor_cuota = valor_cuota

	def __str__(self):
		return f'{self.socio:<6} | {describir_deporte(self.deporte - 1):<10} | {self.dia:>4} | ${self.valor_cuota:>5.2f}'

	def to_str_csv(self):
		return f'{self.socio:<6},{describir_deporte(self.deporte - 1):<10},{self.dia:>4},{self.valor_cuota:>5.2f}'


def describir_deporte(deporte):
	return str(deporte) + '-' + DEPORTES[deporte]


def to_string_titulos():
	return '{:<6} | {:<10} | {:>4} | {:>8}'.format('Socio', 'Deporte', 'Dia', 'Valor')
