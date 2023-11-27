import random


class Linea:
    def __init__(self, numero, titular, tipo_producto, minutos, provincia):
        self.numero = numero
        self.titular = titular
        self.tipo_producto = tipo_producto
        self.minutos = minutos
        self.provincia = provincia

    def __str__(self):
        cadena = '| {:<15} | {:<30} | {:^10} | {:>10} | {:^10} |\n' \
                 '{:<91}\n'
        return cadena.format(self.numero, self.titular, self.tipo_producto, self.minutos, self.provincia, '-' * 91)


def encabezado_listado():
    cadena = '{:<91}\n' \
             '| {:<15} | {:<30} | {:^10} | {:>10} | {:^10} |\n' \
             '{:<91}\n'
    return cadena.format('=' * 91, 'Numero', 'Titular', 'Tpo. Prod.', 'Minutos', 'Provincia', '=' * 91)


def crear_numero_linea():
    numero = '{}{}{}'
    return numero.format(random.randint(350, 373), random.randint(1, 9), random.randint(111111, 999999))


def crear_nombre_titular():
    nombres = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
               'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')

    apellidos = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                 'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    nombre = '{} {}'
    return nombre.format(random.choice(nombres), random.choice(apellidos))