__author__ = 'Algoritmos y Estructuras de Datos'


class Reserva:
	def __init__(self, numero, nombre_cumple, edad, tipo_servicio, invitados, monto):
		self.numero = numero
		self.nombre_cumple = nombre_cumple
		self.edad = edad
		self.tipo_servicio = tipo_servicio
		self.invitados = invitados
		self.monto = monto

	def __str__(self):
		cad = '{:<11} | {:<30} | {:^4} | {:<45} | {:^10} | ${:>10.2f}'
		return cad.format(self.numero, self.nombre_cumple, self.edad,
		                  descripcion_servicio(self.tipo_servicio), \
		                  self.invitados, self.monto)

	def to_lineacsv(self):
		cad = '{},{},{},{},{},{}\n'
		return cad.format(self.numero, self.nombre_cumple, self.edad, self.tipo_servicio, \
		                  self.invitados, self.monto)


def descripcion_servicio(tipo_servicio):
	descripcion_servicio = ('Salón', 'Salón y animación', 'Salón, animación y comida niños',
	                        'Salón, animación, comida niños y sorpresitas')
	return descripcion_servicio[tipo_servicio]


def str_toreserva(linea):
	token = linea.split(',')
	numero = token[0]
	nombre = token[1]
	edad = int(token[2])
	tipo_servicio = int(token[3])
	invitados = int(token[4])
	monto = float(token[5])
	reserva = Reserva(numero, nombre, edad, tipo_servicio, invitados, monto)
	return reserva
