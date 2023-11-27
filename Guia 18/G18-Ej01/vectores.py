__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'


def sumar_vector(v):
    suma = 0
    for i in range(len(v)):
        suma += v[i]
    return suma


def buscar_mayor(v):
    may = 0
    for i in range(1, len(v)):
        if v[i] > v[may]:
            may = i
    return may


def contar_valores(v, x):
    cant = 0
    for i in range(len(v)):
        if v[i] == x:
            cant += 1
    return cant

