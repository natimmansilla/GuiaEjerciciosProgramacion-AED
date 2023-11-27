import random

from clase import *


def existe(aspirantes, legajo):
    for aprendiz in aspirantes:
        if aprendiz.legajo == legajo:
            return True
    return False


def cargar_aspirante(aspirantes):
    legajo = int(input('Ingrese el legajo del aspirante: '))
    if not existe(aspirantes, legajo):
        nombre = input('Ingrese el nombre del aspirante: ')
        apellido = input('Ingrese el apellido del aspirante: ')
        aspirantes.append(AprendizMago(legajo, nombre, apellido))
        return True
    else:
        return False


def listar(aspirantes):
    listado = '{:<8}\t{:<20}\t{:<20}\n{}\n'.format('Legajo', 'Nombre', 'Apellido', '-' * 60)
    for aprendiz in aspirantes:
        listado += str(aprendiz)
    return listado


def se_puede_asignar(c, casas):
    asignar = True
    cant_casa = casas[c]
    if casas[c] != 0:
        for i in range(len(casas)):
            if i != c and abs((cant_casa + 1) - casas[i]) < 2:
                asignar = False
                break
    return asignar


def seleccionar_aprendices(aspirantes, casas):
    tam = len(aspirantes)
    for i in range(tam):
        aprendiz = aspirantes[i]
        if aprendiz.casa_asignada == -1:
            asignar = False
            c = 0
            while not asignar:
                c = random.randrange(4)
                asignar = se_puede_asignar(c, casas)
            casas[c] += 1
            aprendiz.casa_asignada = c


def listar_por_casa(aspirantes):
    listado = '{:^60}\n'.format('Listado de Aprendices Por Casa')
    listado += '=' * 60 + '\n'

    for i in range(4):
        v = [aprendiz for aprendiz in aspirantes if aprendiz.casa_asignada == i]
        listado += 'Casa de {:<60}\n{}\n'.format(to_string_casa(i), '_' * 60)
        listado += '{:<8}\t{:<20}\t{:<20}\n{}\n'.format('Legajo', 'Nombre', 'Apellido', '-' * 60)

        for aprendiz in v:
            listado += str(aprendiz)

        listado += '\n'
        listado += '_' * 60 + '\n'
    return listado


def cargar_aleatorio():
    nombres = ('Carlos', 'Andres', 'Martin', 'Carla', 'Maria', 'Laura', 'Andrea', 'German')
    apellidos = ('Martinez', 'Fernandez', 'Perez', 'Garcia', 'Lopez', 'Gonzales')
    n = int(input('Ingrese la cantidad a generar: '))
    vec = [None] * n
    for i in range(n):
        legajo = random.randint(1, 1500)
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        vec[i] = AprendizMago(legajo, nombre, apellido)
    return vec


def main():
    menu = 'Menu de Opciones\n' \
           '=================================================\n' \
           '1 \t Agregar Aspirante a Mago\n' \
           '2 \t Listar Todos los Aspirantes a Magos\n' \
           '3 \t Asignar Aspirantes a Casas de Magia\n' \
           '4 \t Cantidad de Aspirantes por Casa\n' \
           '5 \t Listar los Aspirantes Asignados a cada Casa\n' \
           '6 \t Salir\n' \
           'Ingrese su opcion: '

    aspirantes = cargar_aleatorio()
    casas = [0] * 4
    opcion = 0
    while opcion != 6:
        opcion = int(input(menu))
        if opcion == 1:
            if cargar_aspirante(aspirantes):
                print('El nuevo aspirante fue ingresado ocn exito a la escuela')
            else:
                print('No se puede asignar el legajo ingresado, ya esta asignado')

        elif opcion == 2:
            listado = '{:^60}\n'.format('Listado de Aprendices')
            listado += listar(aspirantes)
            print(listado)

        elif opcion == 3:
            seleccionar_aprendices(aspirantes, casas)

        elif opcion == 4:
            print('Cantidad de Aspirantes por Casa')
            print('-' * 60)
            for i in range(len(casas)):
                print(to_string_casa(i), ':', casas[i])

        elif opcion == 5:
            listado = listar_por_casa(aspirantes)
            print(listado)


if __name__ == '__main__':
    main()