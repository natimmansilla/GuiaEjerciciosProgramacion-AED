__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import pickle
import random

from registros import Voto, Candidato


def gererar_arhivo_votos():
	m = open("votos.dat", 'a+b')
	for i in range(5000):
		candidato = random.randrange(7)
		provincia = random.randrange(23)
		votante = random.randint(0, 99999)
		v = Voto(candidato, provincia, votante)
		pickle.dump(v, m)
		m.flush()
	m.close()


def generar_archivo_candidato():
	nombres = ['Antonio Miguel Carmona', 'Ada Colau', 'Alberto Fernández Díaz',
	           'Fernando Giner', 'Juan Espadas', 'Elena Martínez', 'Alicia Morales']
	m = open("candidatos.dat", 'a+b')
	for i in range(len(nombres)):
		candidato = Candidato(i, nombres[i])
		pickle.dump(candidato, m)
	m.close()


if __name__ == '__main__':
	gererar_arhivo_votos()
	generar_archivo_candidato()
