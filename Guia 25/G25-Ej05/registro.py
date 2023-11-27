__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Aspirante:
	def __init__(self, dni, nombre, apellido, nota):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.nota = nota

	def __str__(self):
		return 'Aspirante DNI: {:<10} Nombre: {:<20} Nota: {:>3}'.format(self.dni, self.nombre + ' ' + self.apellido.upper(), self.nota)

	def to_csv(self):
		linea = '{},{},{},{}\n'.format(self.dni, self.nombre, self.apellido, self.nota)
		return linea


def csv_to_aspirante(linea):
	if linea[-1] == '\n':
		linea = linea[:-1]
	campos = linea.split(',')
	return Aspirante(campos[0], campos[1], campos[2], int(campos[3]))
