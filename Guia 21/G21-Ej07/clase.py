__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Ticket:
    def __init__(self, num, tipo, desc, estado):
        self.numero = num
        self.tipo = tipo
        self.descripcion = desc
        self.estado = estado

    def __str__(self):
        return f"Número de identificación: {self.numero} - Tipo de ticket: {self.tipo} - " \
               f"Descripción: {self.descripcion} - Estado: {self.estado}"
