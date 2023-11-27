""" Solución b.) Una clase que incluye un método para el cálculo del podio.
"""
import random


class Atleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.natacion = random.randint(10, 20)
        self.ciclismo = random.randint(10, 40)
        self.pedestre = random.randint(10, 25)

    def write(self):
        print('Atleta', self.nombre, end="")
        print(' | Natacion:', self.natacion, 'min.', end= "")
        print(' | Ciclismo:', self.ciclismo, 'min.', end="")
        print(' | Pedestre:', self.pedestre, 'min.')

    def determinar_promedio(self):
        suma = self.ciclismo + self.natacion + self.pedestre
        return suma / 3

    def definir_podio (self, prom1, atleta2, prom2, atleta3, prom3):
        if prom1 < prom2 and prom1 < prom3:
            primero = self
            if prom2 < prom3:
                segundo = atleta2
                tercero = atleta3
            else:
                segundo = atleta3
                tercero = atleta2
        elif prom2 < prom3:
            primero = atleta2
            if prom1 < prom3:
                segundo = self
                tercero = atleta3
            else:
                segundo = atleta3
                tercero = self
        else:
            primero = atleta3
            if prom1 < prom2:
                segundo = self
                tercero = atleta2
            else:
                segundo = atleta2
                tercero = self
        return primero, segundo, tercero


def test():
    nombre = input('Ingrese el nombre del atleta 1: ')
    atleta1 = Atleta(nombre)
    atleta1.write()

    nombre = input('Ingrese el nombre del atleta 2: ')
    atleta2 = Atleta(nombre)
    atleta2.write()

    nombre = input('Ingrese el nombre del atleta 3: ')
    atleta3 = Atleta(nombre)
    atleta3.write()

    # Informar Tiempo promedio de cada competidor
    print('PROMEDIOS')
    prom1 = atleta1.determinar_promedio()
    prom2 = atleta2.determinar_promedio()
    prom3 = atleta3.determinar_promedio()
    print('El Atleta ', atleta1.nombre, ' hizo ', prom1, ' minutos')
    print('El Atleta ', atleta2.nombre, ' hizo ', prom2, ' minutos')
    print('El Atleta ', atleta3.nombre, ' hizo ', prom3, ' minutos')

    # Determinar el podio, indicando el nombre del primer,segundo y tercer mejor promedio
    podio = atleta1.definir_podio(prom1, atleta2, prom2, atleta3, prom3)
    print('*PODIO*')
    print('1ro)', podio[0].nombre)
    print('2do)', podio[1].nombre)
    print('3ro)', podio[2].nombre)


if __name__ == "__main__":
    test()
