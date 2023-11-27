__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import random

from clase import Equipo
from generales import *


def cargar_manual(n):
    v = [None] * n
    for i in range(n):
        nombre = input('Ingrese nombre del equipo: ')
        puntos = validar_entre(0, 20, 'Ingrese puntos: ')
        goles = validar_mayor_igual_que(0, 'Ingrese goles: ')
        v[i] = Equipo(nombre, puntos, goles)
    return v


def cargar_automatico(n):
    v = [None] * n
    for i in range(n):
        nombre = 'Equipo' + str(i)
        puntos = random.randint(0, 20)
        goles = random.randint(0, 100)
        v[i] = Equipo(nombre, puntos, goles)
    return v


def mostrar(v, mensaje):
    print(mensaje)
    for i in range(len(v)):
        print(v[i])


def generar_tabla(v):
    tabla = [[0] * 21 for f in range(len(v))]
    for i in range(len(v)):
        tabla[i][v[i].puntos] = v[i].goles
    return tabla


def ordenar_seleccion_directa(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].puntos < v[j].puntos:
                v[i], v[j] = v[j], v[i]


def buscar_mayores(v):
    punteros = [v[0]]
    for i in range(1, len(v)):
        if v[i].puntos == punteros[0].puntos:
            punteros.append(v[i])
        else:
            break
    return punteros


def buscar_ultimos(v, cantidad):
    desde = len(v) - cantidad
    hasta = len(v)
    return v[desde:hasta]


def buscar_desde_goles(v, minimo):
    buenos = list()
    for i in range(len(v)):
        if v[i].goles > minimo:
            buenos.append(v[i])
    return buenos


def ordenar_insercion_directa(v):
    n = len(v)
    for j in range(1, n):
        y = v[j]
        k = j - 1
        while k >= 0 and y.nombre < v[k].nombre:
            v[k + 1] = v[k]
            k -= 1
        v[k + 1] = y


def mostrar_matriz(m):
    for c in range(len(m[0])):
        if c == 0:
            print('Puntos', end='\t')
        print(c, end='\t')

    for f in range(len(m)):
        print('\nEq{0:03d}: '.format(f), end='\t')
        for c in range(len(m[f])):
            print(m[f][c], end='\t')

    print()


def sumar_columna(tabla, col):
    suma = 0
    for f in range(len(tabla)):
        suma += tabla[f][col]
    return suma


def contar_ceros(tabla, col):
    cant = 0
    for f in range(len(tabla)):
        if tabla[f][col] == 0:
            cant += 1
    return cant


def principal():
    print('TORNEO DE FUTBOL')
    print('=' * 80)
    v = None
    n = validar_mayor_que(5, 'Ingrese cantidad de equipos: ')
    carga = validar_entre(1, 2, 'Elija tipo de carga: 1) Manual - 2) Automatica: ')
    if carga == 1:
        v = cargar_manual(n)
    elif carga == 2:
        v = cargar_automatico(n)

    # Tabla de posiciones
    ordenar_seleccion_directa(v)
    mostrar(v, '\nTABLA DE POSICIONES')

    # Punteros
    punteros = buscar_mayores(v)
    mostrar(punteros, '\nPUNTEROS')

    # Descenso
    ultimos = buscar_ultimos(v, 5)
    mostrar(ultimos, '\nDESCENSO')

    # Equipos que superan la cantidad de goles
    x = int(input('Ingrese cantidad minima de goles: '))
    buenos = buscar_desde_goles(v, x)
    ordenar_insercion_directa(buenos)
    mostrar(buenos, '\nMEJOR DESEMPEÑO')


    print('\nCOMPARATIVO DE GOLES')
    tabla = generar_tabla(v)
    mostrar_matriz(tabla)

    print()
    print('Total de goles para equipos de máximo puntaje: ', sumar_columna(tabla, 20))
    print('Equipos sin puntos ni goles: ', contar_ceros(tabla, 0))


if __name__ == '__main__':
    principal()
