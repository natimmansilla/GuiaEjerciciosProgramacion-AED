""" Solución a.) Básica (usando una clase a modo de registro simple).
"""
import random


class Atleta:
    pass


def init(nombre):
    atleta = Atleta()
    atleta.nombre = nombre
    atleta.natacion = random.randint(10, 20)
    atleta.ciclismo = random.randint(10, 40)
    atleta.pedestre = random.randint(10, 25)
    return atleta


def write(atleta):
    print('El Atleta ', atleta.nombre, ' - ',
          'Natacion: ', str(atleta.natacion), ' - ',
          'Ciclismo: ', str(atleta.ciclismo), ' - ' ,
          'Pedestre: ', str(atleta.pedestre))


def determinar_promedio(atleta):
    suma = atleta.ciclismo + atleta.natacion + atleta.pedestre
    return suma / 3


def test():
    nombre = input('Ingrese el nombre del atleta 1: ')
    atleta1 = init(nombre)
    write(atleta1)

    nombre = input('Ingrese el nombre del atleta 2: ')
    atleta2 = init(nombre)
    write(atleta2)

    nombre = input('Ingrese el nombre del atleta 3: ')
    atleta3 = init(nombre)
    write(atleta3)

    # Informar Tiempo promedio de cada competidor
    prom1 = determinar_promedio(atleta1)
    prom2 = determinar_promedio(atleta2)
    prom3 = determinar_promedio(atleta3)
    print('El Atleta ', atleta1.nombre, ' hizo ', prom1, ' minutos')
    print('El Atleta ', atleta2.nombre, ' hizo ', prom2, ' minutos')
    print('El Atleta ', atleta3.nombre, ' hizo ', prom3, ' minutos')

    # Determinar el podio, indicando el nombre del primer,
    # segundo y tercer mejor promedio
    if prom1 < prom2 and prom1 < prom3:
        primero = atleta1
        if prom2 < prom3:
            segundo = atleta2
            tercero = atleta3
        else:
            segundo = atleta3
            tercero = atleta2
    elif prom2 < prom3:
        primero = atleta2
        if prom1 < prom3:
            segundo = atleta1
            tercero = atleta3
        else:
            segundo = atleta3
            tercero = atleta1
    else:
        primero = atleta3
        if prom1 < prom2:
            segundo = atleta1
            tercero = atleta2
        else:
            segundo = atleta2
            tercero = atleta1

    print()
    print('Podio')
    print('Primero ', end='')
    write(primero)
    print('Segundo ', end='')
    write(segundo)
    print('Tercero ', end='')
    write(tercero)


if __name__ == "__main__":
    test()
