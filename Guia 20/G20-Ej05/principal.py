import random

from clase import *


def validar_mayor_que(men, mensaje):
    num = int(input(mensaje))
    while num <= men:
        print('INVALIDO!')
        num = int(input(mensaje))
    return num


def cargar_automatico(v, n):
    for i in range(n):
        dni = random.randint(15000000, 40000000)
        nombre = 'Concursante ' + str(i)
        cargo = random.randrange(20)
        puntaje = random.uniform(0, 100)
        v[i] = Concursante(dni, nombre, cargo, puntaje)


def ordenar_descendente(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].puntaje < v[j].puntaje:
                v[i], v[j] = v[j], v[i]


def mostrar_vector(v):
    print(columns())
    for i in range(len(v)):
        print(v[i])


def mostrar_aprobados(v):
    print(columns())
    for i in range(len(v)):
        if v[i].puntaje >= 70:
            print(v[i])


def mostrar_menu():
    print('\nCONCURSO ADMINISTRACION PUBLICA')
    print('=' * 40)
    print('1. Cargar los concursantes')
    print('2. Mostrar concursantes aprobados')
    print('3. Cantidad de concursantes por cargo')
    print('4. Listar el arreglo ordenado por puntaje')
    print('5. Buscar postulante')
    print('0. Salir')
    opcion = int(input('Ingrese la opcion: '))
    return opcion


def contar_por_cargo(v):
    conteo = [0] * 20
    for concursante in v:
        conteo[concursante.cargo] += 1
    return conteo


def mostrar_conteo(conteo):
    for i in range(len(conteo)):
        if conteo[i] > 0:
            print('Cargo', i, ':', conteo[i], 'concursantes')


def buscar_por_nombre(v, nombre):
    for i in range(len(v)):
        if v[i].nombre == nombre:
            return i
    return -1


def principal():
    v = list()
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese tamaño del vector: ')
            v = [None] * n
            cargar_automatico(v, n)
        else:
            if len(v) == 0:
                print('El vector aun no fue cargado')
            else:
                if opcion == 2:
                    mostrar_aprobados(v)
                elif opcion == 3:
                    conteo = contar_por_cargo(v)
                    mostrar_conteo(conteo)
                elif opcion == 4:
                    ordenar_descendente(v)
                    mostrar_vector(v)
                elif opcion == 5:
                    nombre = input('Ingrese nombre del postulante buscado: ')
                    pos = buscar_por_nombre(v, nombre)
                    if pos == -1:
                        print('No se encontró el postulante')
                    else:
                        print(columns())
                        print(v[pos])
                        if v[pos].puntaje >= 70:
                            print('¡El postulante aprobó el concurso!')


if __name__ == '__main__':
    principal()