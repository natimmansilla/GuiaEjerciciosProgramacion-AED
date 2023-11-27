__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Candidato:
	def __init__(self, codigo, nombre):
		self.codigo = codigo
		self.nombre = nombre

	def __str__(self):
		return f'Candidato Codigo: {self.codigo} - Nombre: {self.nombre}'


class Voto:
	def __init__(self, candidato, provincia, dni):
		self.candidato = candidato
		self.provincia = provincia
		self.votante = dni

	def __str__(self):
		cadena = f'Candidato: {self.candidato} - Provincia: {self.provincia} - Votante: {self.votante}'
		return cadena
