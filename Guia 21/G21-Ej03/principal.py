__author__ = 'Algoritmos y Estructuras de Datos'

import generales
import clase


def menu():
    menu = 'Menu de Opciones \n' + \
           '=' * 60 + '\n' + \
           '1  ---------- Cargar Jugadores\n' + \
           '2  ---------- Generar hits por posiciones (matriz)\n' + \
           '3  ---------- Mostrar Hits por posiciones\n' + \
           '4  ---------- Acumular porcentajes de efectividad por posicion\n' + \
           '5  ---------- Nombre del jugador con mejor porcentaje de bateo\n' + \
           '0  ---------- Salir\n' + \
           'Ingrese su opcion: '
    return int(input(menu))


def cargar_vector(vector, n):
    for i in range(n):
        pelotero = clase.crear_registro()
        vector.append(pelotero)


def generar_matriz(vector):
    matriz = [[0] * 21 for i in range(9)]
    for pelotero in vector:
        fila = pelotero.posicion - 1
        columna = pelotero.hits
        matriz[fila][columna] += 1
    return matriz


def mostrar_matriz(matriz):
    print('Resultados de la matriz')
    print('=' * 60)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            print('En la posicion ', fila + 1, 'hubo', matriz[fila][columna], 'jugadores que le pegaron', columna,
                  'hits')


def acumular_por_posicion(matriz, posicion):
    total = 0
    for columna in range(len(matriz[posicion - 1])):
        total += matriz[posicion - 1][columna]
    return total


def acumular_porcentajes(vector):
    va = [0] * 9
    for jugador in vector:
        pos = jugador.posicion - 1
        va[pos] += (jugador.hits / 100) * 100
    return va


def buscar_mayor_porcentaje(vector):
    mayor = vector[0]
    for i in range(1, len(vector)):
        if vector[i].hits > mayor.hits:
            mayor = vector[i]
    return mayor


def principal():
    opcion = -1
    jugadores = []
    matriz = None
    matriz_generada = False

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = generales.validar_mayor_que(0, 'Ingrese la cantidad de jugadores a cargar: ')
            cargar_vector(jugadores, n)
        else:
            if len(jugadores) > 0:
                if opcion == 2:
                    matriz_generada = True
                    matriz = generar_matriz(jugadores)
                    mostrar_matriz(matriz)

                elif opcion == 3:
                    if matriz_generada:
                        posicion = generales.validar_rango(1, 9, 'Ingrese la posicion a totalizar: ')
                        total = acumular_por_posicion(matriz, posicion)
                        print('El total de jugadores que pegaron hits en la posicion ingresada fueron:', total)
                    else:
                        print('Primero debe ejecutar la opcion 2')

                elif opcion == 4:
                    va = acumular_porcentajes(jugadores)
                    for i in range(len(va)):
                        print('Los porcentajes acumulados para la posicion', i + 1, 'fue de', va[i])
                elif opcion == 5:
                    jugador = buscar_mayor_porcentaje(jugadores)
                    print('El nombre con el jugador de mejor porcentaje es', jugador.nombre)
            else:
                print('Debe cargar los jugadores para poder ejecutar las opciones')


if __name__ == '__main__':
    principal()
