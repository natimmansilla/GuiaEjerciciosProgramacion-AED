__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

import random


def validar_mayor_que(desde, mensaje):
    valor = int(input(mensaje))
    while valor <= desde:
        print('Valor inválido')
        valor = int(input(mensaje))
    return valor


def cargar(n):
    dado1 = list()
    dado2 = list()
    for i in range(n):
        dado1.append(random.randint(1, 6))
        dado2.append(random.randint(1, 6))
    return dado1, dado2


def generar_tabla(dado1, dado2):
    tabla = [[0] * 7 for f in range(2)]
    for i in range(len(dado1)):
        tabla[0][dado1[i]] += 1
        tabla[1][dado2[i]] += 1
    return tabla


def mostrar_tabla(tabla):
    print('Valores', end=' ')
    for i in range(1, 7):
        print(i, end='\t')
    for fila in range(len(tabla)):
        print('\nDado', fila, ':', end=' ')
        for col in range(1, len(tabla[fila])):
            print(tabla[fila][col], end='\t')
    print()


def buscar_mayor(tabla, fila):
    mayor = 0
    for col in range(1, len(tabla[fila])):
        if tabla[fila][col] > tabla[fila][mayor]:
            mayor = col
    return mayor


def buscar_iguales(tabla):
    iguales = list()
    for col in range(1, len(tabla[0])):
        if tabla[0][col] == tabla[1][col]:
            iguales.append(col)
    return iguales


def main():
    print('ESTADÍSTICAS CON DADOS')
    n = validar_mayor_que(0, 'Ingrese cantidad de lanzamientos: ')
    dado1, dado2 = cargar(n)
    print('Dado 1:', dado1)
    print('Dado 2:', dado2)
    print('-' * 80)
    print('Repeticiones')
    tabla = generar_tabla(dado1, dado2)
    mostrar_tabla(tabla)
    print('-' * 80)
    iguales = buscar_iguales(tabla)
    print('Valores que aparecieron la misma cantidad de veces:', iguales)
    mayor1 = buscar_mayor(tabla, 0)
    mayor2 = buscar_mayor(tabla, 1)
    print('\nEl valor más repetido en el dado 1 fue:', mayor1)
    print('El valor más repetido en el dado 2 fue:', mayor2)


if __name__ == '__main__':
    main()
