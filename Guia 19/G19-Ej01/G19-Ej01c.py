""" Solución c.) Una clase que incluye un atributo para el promedio, y el método __str__() en lugar de write().
"""
import random


class Atleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.natacion = random.randint(10, 20)
        self.ciclismo = random.randint(10, 40)
        self.pedestre = random.randint(10, 25)
        self.promedio = (self.natacion + self.ciclismo + self.pedestre) / 3

    def __str__(self):
        r = 'Atleta ' + self.nombre
        r += ' | Natacion: ' + str(self.natacion) + 'min.'
        r += ' | Ciclismo: ' + str( self.ciclismo) + 'min.'
        r += ' | Pedestre: ' + str(self.pedestre) + 'min.'
        r += ' | Tiempo promedio: ' + str(round(self.promedio, 2)) + 'min.'
        return r

    def determinar_promedio(self):
        suma = self.ciclismo + self.natacion + self.pedestre
        return suma / 3

    def definir_podio(self, atleta2, atleta3):
        if self.promedio < atleta2.promedio and self.promedio < atleta3.promedio:
            primero = self
            if atleta2.promedio < atleta3.promedio:
                segundo = atleta2
                tercero = atleta3
            else:
                segundo = atleta3
                tercero = atleta2
        elif atleta2.promedio < atleta3.promedio:
            primero = atleta2
            if self.promedio < atleta3.promedio:
                segundo = self
                tercero = atleta3
            else:
                segundo = atleta3
                tercero = self
        else:
            primero = atleta3
            if self.promedio < atleta2.promedio:
                segundo = self
                tercero = atleta2
            else:
                segundo = atleta2
                tercero = self
        return primero, segundo, tercero


def test():
    nombre = input('Ingrese el nombre del atleta 1: ')
    atleta1 = Atleta(nombre)
    print(atleta1)

    nombre = input('Ingrese el nombre del atleta 2: ')
    atleta2 = Atleta(nombre)
    print(atleta2)

    nombre = input('Ingrese el nombre del atleta 3: ')
    atleta3 = Atleta(nombre)
    print(atleta3)

    # Determinar el podio, indicando el nombre del primer,segundo y tercer mejor promedio
    podio = atleta1.definir_podio(atleta2, atleta3)
    print('*PODIO*')
    print('1ro)', podio[0].nombre)
    print('2do)', podio[1].nombre)
    print('3ro)', podio[2].nombre)


if __name__ == '__main__':
    test()
