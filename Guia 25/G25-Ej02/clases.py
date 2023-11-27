__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Invitado:

	def __init__(self, nombre, mesa, ong, monto):
		self.nombre = nombre
		self.mesa = mesa
		self.ong = ong
		self.monto = monto

	def __str__(self):
		cad = '{:<20} Mesa:{:<5} ONG:{}-{:<30} ${:<8.2f}'
		return cad.format(self.nombre, self.mesa, self.ong, describir_ong(self.ong), self.monto)


def describir_ong(codigo):
	ongs = ('Missing Children', 'Caritas', 'PUPI', 'Médicos Sin Fronteras', 'Vida Silvestre',
	        'Aldeas', 'Fundaleu', 'Cimientos', 'Uniendo Caminos', 'Adoptare')
	return ongs[codigo]


if __name__ == '__main__':
	x = Invitado('Luis Miguel', 1, 2, 5000)
	print(x)
