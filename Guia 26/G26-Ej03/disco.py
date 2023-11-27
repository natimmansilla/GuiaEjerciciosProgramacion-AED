class Disco:
    def __init__(self, titulo, artista, anio, genero, reproducciones):
        self.titulo = titulo
        self.artista = artista
        self.anio = anio
        self.genero = genero
        self.reproducciones = reproducciones

    def __str__(self):
        r = "Titulo: {:<25}"
        r += " Artista: {:<20}"
        r += " Año: {:<6}"
        r += " Genero: {:<4}"
        r += " Reproducciones: {:<10}"
        return r.format(self.titulo, self.artista, self.anio, self.genero, self.reproducciones)


def cargar_disco():
    titulo = input("Ingrese titulo: ")
    artista = input("Ingrese artista: ")
    anio = int(input("Ingrese año: "))
    genero = int(input("Ingrese género: "))
    reproducciones = int(input("Ingrese reproducciones: "))
    return Disco(titulo, artista, anio, genero, reproducciones)
