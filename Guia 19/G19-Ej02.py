import random


class Carta:
    def __init__(self):
        self.palo = random.choice(('Oro', 'Copa', 'Espada', 'Basto'))
        self.numero = random.randint(1,12)

    def __str__(self):
        return str(self.numero) + ' de ' + self.palo


def definir_resultado(puntos1, puntos2):
    if puntos1 > puntos2:
        resultado = '¡Ganó el Jugador 1!'
    elif puntos2 > puntos1:
        resultado = '¡Ganó el Jugador 2!'
    else:
        resultado = '¡Empate!'
    return resultado


def play():
    print('GUERRA DE CARTAS')
    puntos1, puntos2 = 0, 0
    print('-' * 80)
    for ronda in range(3):
        print('Jugador 1: ',end='')
        carta1 = Carta()
        print(carta1)
        print('Jugador 2: ',end='')
        carta2 = Carta()
        print(carta2)
        puntos = carta1.numero + carta2.numero
        if carta1.numero > carta2.numero:
            puntos1 += puntos
        elif carta2.numero > carta1.numero:
            puntos2 += puntos
        else:
            if carta1.palo == 'Oro':
                puntos1 += puntos
            elif carta2.palo == 'Oro':
                puntos2 += puntos
            else:
                puntos1 += carta1.numero
                puntos2 += carta2.numero
        print('Puntaje Jugador 1:', puntos1)
        print('Puntaje Jugador 2:', puntos2)
        print('-' * 80)
    resultado = definir_resultado(puntos1, puntos2)
    print('RESULTADO FINAL:', resultado)


if __name__ == '__main__':
    play()
