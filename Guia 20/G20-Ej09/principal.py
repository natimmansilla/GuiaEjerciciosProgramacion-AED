import random

from clases import *


def mostrar_menu():
    print('=' * 80)
    print('1. Cargar vector')
    print('2. Mostrar vector')
    print('3. Buscar ticket')
    print('4. Contar apuestas de un caballo')
    print('5. Mostrar ticket con mayor monto')
    print('0. Salir')
    print('=' * 80)
    opcion = int(input('Ingrese opción: '))
    return opcion


def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        num = int(input('Error! ' + mensaje))
    return num


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input('Error! ' + mensaje))
    return num


def cargar_vector_manual(v):
    for i in range(len(v)):
        num = int(input('Ingrese número de ticket: '))
        cab = validar_entre(0, 9, 'Ingrese número de caballo (0-9): ')
        monto = float(input('Ingrese monto a apostar: '))
        v[i] = Apuesta(num, cab, monto)


def cargar_vector_aleatorio(v):
    for i in range(len(v)):
        num = random.randint(100, 999)
        cab = random.randint(0, 9)
        monto = round(random.uniform(1000, 5000),2)
        v[i] = Apuesta(num, cab, monto)


def ordenar_ascendente(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].numero > v[j].numero:
                v[i], v[j] = v[j], v[i]


def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])


def buscar_secuencial(v, num):
    for i in range(len(v)):
        if v[i].numero == num:
            return i
    return -1


def contar_apuestas(v, cab):
    cant = 0
    for i in range(len(v)):
        if v[i].caballo == cab:
            cant += 1
    return cant


def buscar_mayor_monto(v):
    mayor = v[0]
    for i in range(1, len(v)):
        if v[i].monto > mayor.monto:
            mayor = v[i]
    return mayor


def principal():
    v = []
    print('HIPÓDROMO')
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese cantidad de apuestas: ')
            v = [None] * n
            cargar_vector_aleatorio(v)
        elif opcion == 2:
            ordenar_ascendente(v)
            mostrar_vector(v)
        elif opcion == 3:
            num = int(input('Ingrese el ticket a buscar: '))
            pos = buscar_secuencial(v, num)
            if pos == -1:
                print('El ticket ingresado no existe')
            else:
                v[pos].monto *= 10
                print(v[pos])
        elif opcion == 4:
            cab = validar_entre(0, 9, 'Ingrese caballo (0-9): ')
            cant = contar_apuestas(v, cab)
            print('Apuestas para el caballo', cab, ':', cant)
        elif opcion == 5:
            may = buscar_mayor_monto(v)
            print('Ticket con mayor monto:', may)
        elif opcion == 0:
            print('Hasta luego!')


if __name__ == '__main__':
    principal()
