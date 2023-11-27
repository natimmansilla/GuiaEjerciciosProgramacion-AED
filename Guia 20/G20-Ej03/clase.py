class Deuda:
    def __init__(self, nombre, deuda):
        self.nombre = nombre
        self.monto = deuda

    def __str__(self):
        return 'El cliente ' + self.nombre + ' adeuda ' + str(self.monto) + ' pesos.'
