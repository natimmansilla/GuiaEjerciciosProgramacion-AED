__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Calzado:
	def __init__(self, codigo, talle, color):
		self.codigo = codigo
		self.talle = talle
		self.color = color

	def __str__(self):
		cad = 'Cod {} | Color {} | Talle {}'
		return cad.format(self.codigo, self.color, self.talle)
