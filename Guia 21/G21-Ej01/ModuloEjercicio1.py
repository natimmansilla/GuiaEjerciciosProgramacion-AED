__author__ = 'Algoritmos y Estructuras de Datos'

# Modulo ModuloEjercicio1

import random


def cargar_matriz_pasajeros(lineas, paradas):
    pasajeros = [[0] * paradas for i in range(lineas)]

    for i in range(lineas):
        print("Linea", i)
        for j in range(paradas):
            cantidad = random.randint(0, 20)
            # cantidad = int(input("Cantidad de pasajeros en la parada " + str(j) + ": "))
            pasajeros[i][j] = cantidad

    return pasajeros


def pasajeros_por_linea(matriz, lineas, paradas):
    cont = [0] * lineas
    for i in range(lineas):
        for j in range(paradas):
            cont[i] += matriz[i][j]
    return cont


def promedio_por_parada(parada, matriz, lineas):
    suma = 0
    for i in range(lineas):
        suma += matriz[i][parada]
    return suma / lineas


def total_pasajeros(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]

    return suma


def parada_menor(linea_menor, matriz):
    par_menor = 0
    men = matriz[linea_menor][0]
    for j in range(1, len(matriz[linea_menor])):  # j toma cada valor parada de la linea_menor
        if matriz[linea_menor][j] < men:
            par_menor = j
            men = matriz[linea_menor][j]

    return par_menor
