__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import random
from vectores import *


def cargar_estaciones():
    e = ['Maipú', 'Borges', 'Libertador', 'Anchorena', 'Barrancas', 'San Isidro R', 'Punta Chica', 'Marina Nueva',
         'San Fernando R', 'Canal', 'Delta']
    return e


def cargar_pasajeros(estaciones):
    n = len(estaciones)
    ida = [0] * n
    vuelta = [0] * n
    for i in range(n):
        ida[i] = random.randint(0, 5)
        vuelta[i] = random.randint(0, 5)
    return ida, vuelta


def mostrar_datos(estaciones, ida, vuelta):
    print('Estacion', 'Ida', 'Vuelta', sep=' | ')
    for i in range(len(estaciones)):
        print(estaciones[i], ida[i], vuelta[i], sep=' | ')


def comparar_estaciones(ida, vuelta, estaciones):
    rta = list()
    for i in range(len(ida)):
        if ida[i] > vuelta[i]:
            rta.append(estaciones[i])
    return rta


def principal():
    estaciones = cargar_estaciones()
    ida, vuelta = cargar_pasajeros(estaciones)
    opcion = -1
    while (opcion != 0):
        print('=' * 50)
        print('TREN DE LA COSTA')
        print('1. Mostrar los datos')
        print('2. Total de pasajeros')
        print('3. Estacion con mayor cantidad de pasajeros (ida)')
        print('4. Estaciones sin pasajeros')
        print('5. Estaciones con mas pasajeros a la ida')
        print('0. Salir')
        opcion = int(input('Ingrese su opción: '))
        if opcion == 1:
            mostrar_datos(estaciones, ida, vuelta)
        elif opcion == 2:
            tot_ida = sumar_vector(ida)
            tot_vuelta = sumar_vector(vuelta)
            print('Total de pasajeros:', tot_ida, '(ida) y', tot_vuelta, '(vuelta)')
        elif opcion == 3:
            pos = buscar_mayor(ida)
            print('Estacion con mayor cantidad de pasajeros a la ida:', estaciones[pos], '(', ida[pos], 'pasajeros)')
        elif opcion == 4:
            cant = contar_valores(vuelta, 0)
            porc = cant * 100 / len(estaciones)
            print('Estaciones sin pasajeros:', cant, '. Representa un', round(porc, 2), '% del total')
        elif opcion == 5:
            rta = comparar_estaciones(ida, vuelta, estaciones)
            print(rta)
        elif opcion == 0:
            print('Hasta pronto!')
        else:
            print('Opción invalida')
        print('=' * 50)


if __name__ == '__main__':
    principal()
