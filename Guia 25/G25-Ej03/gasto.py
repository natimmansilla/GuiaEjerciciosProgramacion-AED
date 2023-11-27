__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Gasto:
	# constructor que genera los datos aleatorios
	def __init__(self, codigo, descripcion, mes, sucursal, importe):
		self.codigo = codigo
		self.descripcion = descripcion
		self.mes = mes
		self.sucursal = sucursal
		self.importe = importe

	def __str__(self):
		renglon =  f'{self.codigo:>5} {self.descripcion:<80} {self.mes:>5} {self.sucursal:>10} {self.importe:>15.2f}'
		return renglon


def crear_gasto(linea):
	tokens = linea.split(',')
	codigo = tokens[0]
	descripcion = tokens[1]
	mes = int(tokens[2])
	sucursal = int(tokens[3])
	importe = float(tokens[4])
	return Gasto(codigo, descripcion, mes, sucursal, importe)
