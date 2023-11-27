import random


class Venta:
    def __init__(self, cliente, tipo_venta, marca_auto, cuotas_pagas, monto_plan):
        self.cliente = cliente
        self.tipo_venta = tipo_venta
        self.marcar_auto = marca_auto
        self.cuotas_pagas = cuotas_pagas
        self.monto_plan = monto_plan

    def __str__(self):
        cad = '| {:<30} | {:^10} | {:^10} | {:>6} | {:>10.2f} | {:<86}\n'
        return cad.format(self.cliente, self.tipo_venta, self.marcar_auto, self.cuotas_pagas, self.monto_plan, '=' * 91)


def encabezado():
    cad = '{:<86}\n' \
          '| {:<30} | {:^10} | {:^10} | {:>6} | {:>10} |\n' \
          '{:<86}\n'
    return cad.format('=' * 91, 'Cliente', 'Tpo. Venta', 'Marca', 'Cuotas', 'Monto', '=' * 91)


def crear_nombre_titular():
    nombres = ('Melvin', 'Marny', 'Vielka', 'Connor', 'Yvette', 'Beard', 'Hahn', 'Beau', 'Spencer', 'Crawford',
               'Duncan', 'Barron', 'Michelle', 'Walton', 'Kirsten', 'Reece', 'Robinson', 'Dylan', 'West')
    apellidos = ('Chandler', 'Maxwell', 'Gregory', 'Brooks', 'Burke', 'Meyers', 'Beard', 'Xanthus', 'Crawford',
                 'Barron', 'Walton', 'Jenkins', 'Robinson', 'West')
    return '{} {}'.format(random.choice(nombres), random.choice(apellidos))
