import os
import pickle
import random

import linea
from linea import Linea


def menu():
    cadena = 'Menu de Opciones \n' \
             '==================================================\n' \
             '1 --- Cargar Vector de Lineas\n' \
             '2 --- Mostrar Vector de Lineas\n' \
             '3 --- Generar Archivo de Lineas con filtro\n' \
             '4 --- Generar Matriz con minutos consumidos por tipo y provincia\n' \
             '5 --- Buscar lines con la menor cantidad de minutos consumidos\n' \
             '6 --- Buscar linea en el Vector\n' \
             '0 --- Salir\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def validar_mayor_que(minimo, mensaje='Ingrese un numero: '):
    numero = minimo
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!!! El valor ingresado debe ser mayor a {}'.format(minimo))
    return numero


def validar_rango(minimo, maximo, mensaje='Ingrese un numero: '):
    numero = minimo - 1
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!!! El valor ingresado debe esta comprendido entre {} y {}'.format(minimo, maximo))
    return numero


def add_in_order(vector, registro):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].numero == registro.numero:
            pos = med
            break

        if registro.numero < vector[med].numero:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [registro]


def cargar_vector(vector, n):
    for i in range(n):
        numero = linea.crear_numero_linea()
        titular = linea.crear_nombre_titular()
        tipo_producto = random.randrange(20)
        minutos = random.randint(150, 1500)
        provincia = random.randint(1, 23)
        lin = Linea(numero, titular, tipo_producto, minutos, provincia)
        add_in_order(vector, lin)


def mostrar_vector(vector):
    listado = linea.encabezado_listado()
    for lin in vector:
        listado += str(lin)
    print(listado)


def generar_archivo(vector, minutos_consumidos, nombre_archivo):
    m = open(nombre_archivo, 'wb')
    for lin in vector:
        if lin.minutos >= minutos_consumidos:
            pickle.dump(lin, m)
    m.close()


def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return round(porcentaje, 2)


def mostrar_archivo(nombre_archivo, plan):
    if not os.path.exists(nombre_archivo):
        print('El archivo {} no existe y no puede ser leido'.format(nombre_archivo))

    listado = linea.encabezado_listado()
    listado_porc = 'Los clientes con el tipo de producto {} tienen {} lineas y representan un {:<10.2}% sobre el ' \
                   'total de lineas'
    total_plan = total_general = 0
    m = open(nombre_archivo, 'rb')
    size = os.path.getsize(nombre_archivo)
    while m.tell() < size:
        lin = pickle.load(m)
        total_general += 1
        if lin.tipo_producto == plan:
            total_plan += 1
        listado += str(lin)
    m.close()

    porcentaje = calcular_porcentaje(total_plan, total_general)
    listado += listado_porc.format(plan, total_plan, porcentaje)
    print(listado)


def generar_matriz(vector):
    mat = [[0] * 23 for i in range(20)]
    for lin in vector:
        f = lin.tipo_producto
        c = lin.provincia - 1
        mat[f][c] += lin.minutos
    return mat


def mostrar_matriz(matriz):
    cad = 'Para el plan {} en la provincia {} se consumieron {} minutos'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print(cad.format(f, c, matriz[f][c]))


def lineas_menor_cantidad_minutos(vector):
    v = []
    primero = True
    for lin in vector:
        if primero:
            v.append(lin)
            primero = False
        elif v[0].minutos == lin.minutos:
            v.append(lin)
        elif lin.minutos < v[0].minutos:
            v = [lin]
    return v


def buscar_linea(vector, numero):
    izq, der = 0, len(vector) - 1
    pos = -1
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].numero == numero:
            pos = med
            break

        if numero < vector[med].numero:
            der = med - 1
        else:
            izq = med + 1

    return pos


def principal():
    lineas = []
    nombre_archivo = 'lineas.dat'
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de lineas que desea cargar: ')
            cargar_vector(lineas, n)

        if len(lineas) > 0:
            if opcion == 2:
                mostrar_vector(lineas)

            elif opcion == 3:
                minutos_consumidos = validar_mayor_que(0, 'Ingrese la cantidad minima de minutos consumidos: ')
                plan = validar_rango(0, 19, 'Ingrese el tipo de producto a filtrar: ')
                generar_archivo(lineas, minutos_consumidos, nombre_archivo)
                mostrar_archivo(nombre_archivo, plan)

            elif opcion == 4:
                matriz = generar_matriz(lineas)
                mostrar_matriz(matriz)

            elif opcion == 5:
                vec = lineas_menor_cantidad_minutos(lineas)
                mostrar_vector(vec)
            elif opcion == 6:
                x = input('Ingrese el numero de linea a buscar: ')
                pos = buscar_linea(lineas, x)
                if pos != -1:
                    lineas[pos].minutos *= 1.20
                    print(lineas[pos])
                else:
                    print('No existe una linea con el numero ingresado')


if __name__ == '__main__':
    principal()
