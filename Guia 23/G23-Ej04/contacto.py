__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Contacto:
	def __init__(self, nombre, apellido, mail, telefono):
		self.nombre = nombre
		self.apellido = apellido
		self.mail = mail
		self.telefono = telefono

	def __str__(self):
		linea = '{:<30} {:<30} {:<15} {:<30}'
		return linea.format(self.nombre, self.apellido, self.telefono, self.mail)
