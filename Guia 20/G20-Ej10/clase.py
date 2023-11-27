import random

nombres = ['Felipe', 'Nico', 'Andy', 'Romi', 'Norma', 'Aldo', 'Rapaz']
apellidos = ['Steffo', 'Parola', 'Bianchi', 'Alesso', 'Perez', 'Gonzalez']
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Pasaje:
	def __init__(self, pas, nom, dest, clase, monto):
		self.pasaporte = pas
		self.nombre = nom
		self.destino = dest
		self.clase = clase
		self.monto = monto

	def __str__(self):
		return f'{self.pasaporte:9} {self.nombre:<30} {self.destino:^7} {self.clase:^5} {self.monto:>10}'


def crear_pasaje_aleatorio():
	pas = random.choice(letras) + str(random.randint(10000000, 99999999))
	nom = random.choice(nombres) + ' ' + random.choice(apellidos)
	destino = random.randint(100, 103)
	clase = random.randint(1, 10)
	importe = float(random.randint(100000, 500000))
	return Pasaje(pas ,nom, destino, clase, importe)
