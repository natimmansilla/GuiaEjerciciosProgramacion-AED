__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random


class Figurita:
	def __init__(self, nombre, pais, numero_jugador, posicion, valor_canje):
		self.nombre = nombre
		self.pais = pais
		self.numero_jugador = numero_jugador
		self.posicion = posicion
		self.valor_canje = valor_canje

	def __str__(self):
		descripcion = descripcion_posicion(self.posicion)
		cad = f'| {self.nombre:<30} | {self.pais:<4} | {self.numero_jugador:<4} | {descripcion:<15} | ' \
		      f'{self.valor_canje:<5} |\n{"-" * 74:<74}'
		return cad

	def figurita_tostr(self):
		return f'{self.nombre},{self.pais},{self.numero_jugador},{self.posicion},{self.valor_canje}\n'

def descripcion_posicion(posicion):
	posiciones = ('arquero', 'defensor', 'volante', 'delantero')
	return posiciones[posicion]


def generar_nombre():
	nombres = 'Vladimir Kinney', 'Odysseus Rice', 'Christen Carter', 'Basil Blake', 'Madonna Wells', 'Emerson Garner', \
		'HadassahEngland', 'Carissa Rivers', 'Doris Justice', 'Seth Tanner', 'Kelly Buckner', 'Galvin Pruitt', \
		'Julian Norton', 'Yvonne Roth', 'McKenzie Morton', 'Jordan Gilliam'
	return random.choice(nombres)


def obtener_tokens(linea, sep=','):
	tokens = []
	pos_inicial = 0
	pos_final = 0
	for pos in range(len(linea)):
		if linea[pos] == sep:
			pos_final = pos
			token = linea[pos_inicial:pos_final]
			tokens.append(token)
			pos_inicial = pos + 1

	if pos_inicial < len(linea):
		token = linea[pos_inicial:]
		tokens.append(token)

	return tokens


def str_tofigurita(linea):
	tokens = obtener_tokens(linea[:-1])
	nombre = tokens[0]
	pais = int(tokens[1])
	numero_jugador = int(tokens[2])
	posicion = int(tokens[3])
	valor_canje = int(tokens[4])
	return Figurita(nombre, pais, numero_jugador, posicion, valor_canje)
