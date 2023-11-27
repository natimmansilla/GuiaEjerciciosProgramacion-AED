class Apuesta:
    def __init__(self, numero, caballo, monto):
        self.numero = numero
        self.caballo = caballo
        self.monto = monto

    def __str__(self):
        cad = 'Ticket N° ' + str(self.numero)
        cad += ' - Caballo ' + str(self.caballo)
        cad += ' - Monto $' + str(self.monto)
        return cad
