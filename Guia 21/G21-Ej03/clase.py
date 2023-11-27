from random import randint, choice


class Pelotero:
    def __init__(self, nombre, posicion, hits):
        self.nombre = nombre
        self.posicion = posicion
        self.hits = hits

    def __str__(self):
        return 'Jugador ' + self.nombre + \
            ' juega en la posicion ' + str(self.posicion) + \
            ' y ha llegado a primera base ' + str(self.hits) + ' veces'


def crear_registro():
    nombres = ['pra', 'con', 'lis', 'cam', 'man', 'are', 'atro', 'pac', 'ino']
    nombre = choice(nombres) + choice(nombres) + choice(nombres) + ' ' + choice(nombres) + choice(nombres) + \
             choice(nombres)
    posicion = randint(1, 9)
    hits = randint(0, 20)
    return Pelotero(nombre, posicion, hits)
