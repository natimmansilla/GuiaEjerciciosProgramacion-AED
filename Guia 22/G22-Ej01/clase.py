class Equipo:

    def __init__(self, nombre, puntos, goles):
        self.nombre = nombre
        self.puntos = puntos
        self.goles = goles

    def __str__(self):
        return 'Nombre: {} - Puntos: {} - Goles: {}'.format(self.nombre, self.puntos, self.goles)
