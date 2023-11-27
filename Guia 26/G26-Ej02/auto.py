class Auto:
    def __init__(self, patente, modelo):
        self.patente = patente
        self.modelo = modelo
        self.estado = 1

    def __str__(self):
        txt = 'Patente: {:<10}'.format(self.patente)
        txt += 'Modelo: {:<25}'.format(self.modelo)
        txt += 'Estado: {:<5}'.format(self.estado)
        return txt
