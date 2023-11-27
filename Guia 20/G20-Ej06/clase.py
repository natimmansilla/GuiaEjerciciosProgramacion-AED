class Alquiler:
    def __init__(self,dni, nombre, monto, tipo):
       self.documento = dni
       self.nombre = nombre
       self.monto = monto
       self.tipo = tipo

    def __str__(self):
        linea = '{:<15}\t{:<40}\t{:>6}\t${:>10.2f}\n'
        return linea.format(self.documento, self.nombre, self.tipo, self.monto)
