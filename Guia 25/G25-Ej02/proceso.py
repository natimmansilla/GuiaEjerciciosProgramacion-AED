__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from clases import *
import pickle
import os.path


def menu():
    print('=' * 80)
    print('GALA DE BENEFICENCIA')
    print('1 - Mostrar el listado completo de invitados')
    print('2 - Informar cantidad de invitados por ONG y por mesa')
    print('3 - Mostrar el nombre del invitado que realizó la mayor donación')
    print('4 - Guardar en un archivo todas las donaciones que correspondan a una ONG')
    print('5 - Buscar el archivo de la ONG ')
    print('0 - Salir')
    print('=' * 80)
    return int(input('Ingrese su opcion: '))


def add_in_order(v, x):
    n = len(v)
    izq, der, pos = 0, n - 1, n
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == x.nombre:
            pos = c
            break
        if x.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [x]


def leer_csv(fd):
    v = []
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, 'rt')
        for linea in m:
            campos = linea.split(',')
            x = Invitado(campos[0], int(campos[1]), int(campos[2]), int(campos[3]))
            add_in_order(v, x)
        m.close()
    return v


def mostrar_vector(vector):
    print('Listado de Invitados')
    for i in range(len(vector)):
        print(vector[i])


def generar_conteo(vector):
    m = [[0] * 13 for fila in range(10)]

    for i in range(len(vector)):
        f = vector[i].ong
        c = vector[i].mesa
        m[f][c] += 1

    return m


def mostrar_conteo(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > 1:
                print('Mesa {} ONG {}: {} invitados'.format(f, c, m[f][c]))


def buscar_mayor(v, mesa):
    mayor = None
    for i in range(len(v)):
        if v[i].mesa == mesa:
            if mayor is None or v[i].monto > mayor.monto:
                mayor = v[i]
    return mayor


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input('Error! ' + mensaje))
    return num


def crear_archivo_ong(v, ong):
    fd = 'donaciones{}.dat'.format(ong)
    m = open(fd, 'wb')
    for i in range(len(v)):
        if v[i].ong == ong:
            pickle.dump(v[i], m)
    m.close()
    print('Archivo', fd, 'generado')


def calcular_promedio(suma, cant):
    if cant == 0:
        return 0
    else:
        return suma / cant


def mostrar_archivo(ong):
    suma, cant = 0, 0
    fd = 'donaciones{}.dat'.format(ong)
    if not os.path.exists(fd):
        print('En archivo no existe')
    else:
        m = open(fd, 'rb')
        size = os.path.getsize(fd)
        while m.tell() < size:
            x = pickle.load(m)
            print(x)
            suma += x.monto
            cant += 1
        m.close()
    print('Recaudación promedio $', calcular_promedio(suma, cant))


def principal():
    # Leer el archivo csv
    v = leer_csv('invitados.csv')
    if len(v) == 0:
        print('No se pudo leer el archivo. El programa finalizará')
        return
    # Continuar con el menú si se pudo leer el archivo
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            mostrar_vector(v)
        elif opcion == 2:
            cont = generar_conteo(v)
            mostrar_conteo(cont)
        elif opcion == 3:
            x = validar_entre(0, 12, 'Ingrese mesa a buscar (0-12): ')
            may = buscar_mayor(v, x)
            if may is None:
                print('No hay invitados para la mesa seleccionada')
            else:
                print('El invitado con mayor monto fue', may.nombre)
        elif opcion == 4:
            ong = validar_entre(0, 9, 'Ingrese ONG a buscar (0-9): ')
            crear_archivo_ong(v, ong)
        elif opcion == 5:
            ong = validar_entre(0, 9, 'Ingrese ONG a buscar (0-9): ')
            mostrar_archivo(ong)


if __name__ == '__main__':
    principal()
