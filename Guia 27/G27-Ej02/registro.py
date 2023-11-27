import random


class Factura:
    def __init__(self, numero, nombre, tipo_cliente, tipo_producto, monto_mensual):
        self.numero = numero
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.tipo_producto = tipo_producto
        self.monto_mensual = monto_mensual

    def __str__(self):
        cad = '| {:<8} | {:<30} | {:^10} | {:^10} | {:>10.2f} | {:<91}\n'
        return cad.format(self.numero, self.nombre, self.tipo_cliente, self.tipo_producto, self.monto_mensual, '=' * 91)


def encabezado():
    cad = '{:<91}\n' \
          '| {:<8} | {:<30} | {:^10} | {:^10} | {:>10} |\n' \
          '{:<91}\n'
    return cad.format('=' * 91, 'Numero', 'Titual', 'Tpo. Cte.', 'Tpo. Prod.', 'Monto', '=' * 91)


def crear_nombre_titular():
    nombres = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
               'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')
    apellidos = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                 'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return '{} {}'.format(random.choice(nombres), random.choice(apellidos))
