class Concursante:
    def __init__(self, dni, nombre, cargo, puntaje):
        self.documento = dni
        self.nombre = nombre
        self.cargo = cargo
        self.puntaje = puntaje

    def __str__(self):
        linea = '{:<15}\t{:<40}\t{:>6}\t{:>10.2f}'
        return linea.format(self.documento, self.nombre, self.cargo, self.puntaje)


def columns():
    linea = '{:<15}\t{:<40}\t{:>6}\t{:>10}'
    return linea.format('Documento', 'Nombre', 'Cargo', 'Puntaje')

