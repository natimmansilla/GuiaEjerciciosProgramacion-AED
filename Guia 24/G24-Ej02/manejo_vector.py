__author__ = 'Algoritmos y Estructuras de Datos'


def buscar_alquiler(numero, vector):
	pos = -1
	for i in range(len(vector)):
		if vector[i].numero == numero:
			pos = i
			break
	return pos


def existe(numero, vector):
	pos = buscar_alquiler(numero, vector)
	return pos >= 0


def ordenar(vector):
	tam = len(vector)
	for i in range(tam - 1):
		for j in range(i + 1, tam):
			if vector[i].numero > vector[j].numero:
				vector[i], vector[j] = vector[j], vector[i]
