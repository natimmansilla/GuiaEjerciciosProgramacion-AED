class Socio:
    def __init__(self,numero, nombre, plan, monto):
        self.numero = numero
        self.nombre = nombre
        self.plan = plan
        self.monto = monto
        self.activo = True

    def __str__(self):
        txt = 'Numero: {:<10}'.format(self.numero)
        txt += 'Nombre: {:<25}'.format(self.nombre)
        txt += 'Plan: {:<10}'.format(self.plan)
        txt += 'Monto: ${:<10.2f}'.format(self.monto)
        return txt
