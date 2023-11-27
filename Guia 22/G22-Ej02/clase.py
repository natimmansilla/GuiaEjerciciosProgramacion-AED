class Alumno:

    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio

    def __str__(self):
        return 'Alumno: {} - Promedio: {}'.format(self.nombre, round(self.promedio, 2))
