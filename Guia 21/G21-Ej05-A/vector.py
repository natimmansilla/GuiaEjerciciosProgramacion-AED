__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def buscar_mayor(v):
    mayor = v[0]
    for i in range(1, len(v)):
        if v[i] > mayor:
            mayor = v[i]
    return mayor


def sumar_vector(v):
    total = 0
    for valor in v:
        total += valor
    return total
