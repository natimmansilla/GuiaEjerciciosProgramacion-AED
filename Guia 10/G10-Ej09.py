__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random


def validar_mayor_que(minimo, mensaje):
    num = int(input(mensaje))
    while num <= minimo:
        num = int(input('INVALIDO! ' + mensaje))
    return num


def generar_carta():
    palos = ('Copa', 'Basto', 'Espada', 'Oro')
    num = random.randint(1, 12)
    palo = random.choice(palos)
    return num, palo


def jugar(n):
    puntos1 = puntos2 = 0
    for ronda in range(n):
        print('\nRONDA', ronda)

        carta1 = generar_carta()
        print('Jugador 1 obtiene', carta1)

        carta2 = generar_carta()
        print('Jugador 2 obtiene', carta2)

        suma = carta1[0] + carta2[0]
        if carta1[0] > carta2[0]:
            puntos1 += suma
        elif carta2[0] > carta1[0]:
            puntos2 += suma
        else:
            if carta1[1] == 'Oro' and carta2[1] != 'Oro':
                puntos1 += suma
            elif carta1[1] != 'Oro' and carta2[1] == 'Oro':
                puntos2 += suma
            else:
                puntos1 += carta1[0]
                puntos2 += carta2[0]
        print('Puntajes: ', puntos1, 'a', puntos2)

    return puntos1, puntos2


def mostrar_resultado(puntos1, puntos2):
    if puntos1 > puntos2:
        print('¡El Jugador 1 es el ganador!')
    elif puntos2 > puntos1:
        print('¡El Jugador 2 es el ganador!')
    else:
        print('¡Los jugadores empataron!')


def principal():
    print('JUEGO DE CARTAS')
    print('*' * 80)
    n = validar_mayor_que(0, 'Ingrese rondas a jugar: ')
    puntos1, puntos2 = jugar(n)
    print('*' * 80)
    mostrar_resultado(puntos1, puntos2)


if __name__ == '__main__':
    principal()
