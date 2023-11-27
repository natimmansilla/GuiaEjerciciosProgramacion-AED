__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import pickle
import random

import registro


def generar_cuotas_dat(archivo):
	m = open(archivo, 'wb')
	n = random.randint(1000, 6000)
	for i in range(n):
		socio = random.randint(1000, 9999999)
		deporte = random.randint(1, 4)
		dia = random.randrange(32)
		valor_cuota = random.uniform(2700, 8000)
		cobro = registro.Cuota(socio, deporte, dia, valor_cuota)
		pickle.dump(cobro, m)
	m.close()


if __name__ == '__main__':
	archivo = 'cuotas.dat'
	generar_cuotas_dat(archivo)
