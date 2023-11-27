__author__ = 'Algoritmos y Estructuras de Datos'
from reserva import str_toreserva, Reserva
import os.path


def generar_arreglo():
	v = []
	if os.path.exists("reservas.csv"):
		m = open('reservas.csv', 'rt')
		for linea in m:
			reserva = str_toreserva(linea)
			v.append(reserva)
		m.close()
	return v


def grabar_arreglo(vector):
	m = open('reservas.csv', "wt")
	for res in vector:
		cad = res.to_lineacsv()
		m.write(cad)
	m.close()
