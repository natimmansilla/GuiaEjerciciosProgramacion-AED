__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

IDIOMAS = ('0-Español', '1-Ingles', '2-Frances', '3-Portugues', '4-Otros')
GENEROS = ('0-Infantil', '1-Comedia', '2-Romantico', '3-Drama', '4-Ciencia Ficcion', '5-Otros')


class Serie:
    def __init__(self, titulo, genero, idioma, temporadas, duracion):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.temporadas = temporadas
        self.duracion = duracion

    def __str__(self):
        cad = '{:<30}{:<20}{:<12}{:>4}{:>6}'
        return cad.format(self.titulo, GENEROS[self.genero], IDIOMAS[self.idioma], self.temporadas,
                          self.duracion)


def csv_to_Serie(linea):
    linea = linea[:-1]
    token = linea.split(',')
    return Serie(token[0], int(token[1]), int(token[2]), int(token[3]), int(token[4]))


def mostrar_titulos():
    cad = '{:<30}{:<20}{:<12}{:<4}{:>6}'.format('Titulo', 'Genero', 'Idioma', 'Temp', 'Durac')
    print(cad)
