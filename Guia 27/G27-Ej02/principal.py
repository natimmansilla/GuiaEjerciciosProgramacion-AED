import os
import pickle
import random

import registro
from registro import Factura


def menu():
    cad = 'Menu de Opciones\n' \
          '=======================================\n' \
          '1 --- Cargar un vector con las factuas de los clientes\n' \
          '2 --- Mostar las facturas cargadas\n' \
          '3 --- Buscar un factura del cliente por numero de indentificacion\n' \
          '4 --- Generar matriz de acumulacion\n' \
          '5 --- Generar archivo binario\n' \
          '6 --- Filtrar por tipo de producto\n' \
          '0 --- Salir\n' \
          'Ingrese su opcion: '
    return int(input(cad))


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


def add_in_order(vector, factura):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].numero == factura.numero:
            pos = med
            break

        if factura.numero < vector[med].numero:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [factura]


def cargar_facturas(vector, n):
    for i in range(n):
        numero = random.randint(100, 10000)
        nombre = registro.crear_nombre_titular()
        tipo_cliente = random.randrange(9)
        tipo_producto = random.randint(1, 15)
        monto = random.uniform(1500, 5600)
        factura = Factura(numero, nombre, tipo_cliente, tipo_producto, monto)
        add_in_order(vector, factura)


def mostrar_facturas(vector):
    listado = registro.encabezado()
    for factura in vector:
        listado += str(factura)
    print(listado)


def buscar_factura(vector, numero):
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


def generar_matriz(vector):
    mat = [[0] * 16 for i in range(9)]
    for factura in vector:
        f = factura.tipo_cliente
        c = factura.tipo_producto
        mat[f][c] += 1
    return mat


def mostrar_matriz(matriz):
    cad = 'Para el tipo de cliente {} con el tipo de producto {} existen {} facturas'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(cad.format(f, c, matriz[f][c]))


def generar_archivo(vector, tipo_cliente, nombres_archivo):
    m = open(nombres_archivo, 'wb')
    for factura in vector:
        if factura.tipo_cliente == tipo_cliente and (factura.tipo_producto < 2 or factura.tipo_producto > 4):
            pickle.dump(factura, m)
    m.close()


def mostrar_archivo(nombres_archivo):
    if not os.path.exists(nombres_archivo):
        print('No existe el archivo {}'.format(nombres_archivo))
        return

    m = open(nombres_archivo, 'rb')
    size = os.path.getsize(nombres_archivo)
    listado = registro.encabezado()
    total = 0
    while m.tell() < size:
        factura = pickle.load(m)
        listado += str(factura)
        total += factura.monto_mensual
    m.close()

    listado += 'El total facturado por todos los clientes fue de ${:>10.2f}'.format(total)
    print(listado)


def acumular_por_tipo_producto(vector, tipo_producto):
    total_tipo = total_general = 0
    for factura in vector:
        total_general += factura.monto_mensual
        if factura.tipo_producto == tipo_producto:
            total_tipo += factura.monto_mensual
    return total_tipo, total_general


def calcular_porcentaje(acumulador, total):
    porcentaje = 0
    if total > 0:
        porcentaje = acumulador * 100 / total
    return porcentaje


def principal():
    facturas = []
    nombres_archivo = 'facturas_clientes.dat'
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de facturas que desea cargar: ')
            cargar_facturas(facturas, n)

        elif len(facturas) > 0:
            if opcion == 2:
                mostrar_facturas(facturas)
            elif opcion == 3:
                x = validar_mayor_que(0, 'Ingrese el numero de identificacion a buscar: ')
                pos = buscar_factura(facturas, x)
                if pos != -1:
                    print(facturas[pos])
                else:
                    print('No existe una factura con el numero ingresado')
            elif opcion == 4:
                matriz = generar_matriz(facturas)
                mostrar_matriz(matriz)
            elif opcion == 5:
                tipo_cliente = validar_rango(0, 8, 'Ingrese el tipo de cliente a buscar: ')
                generar_archivo(facturas, tipo_cliente, nombres_archivo)
                mostrar_archivo(nombres_archivo)
            elif opcion == 6:
                tipo_producto = validar_rango(0, 16, 'Ingrese el tipo de producto a buscar: ')
                total_tipo_producto, total = acumular_por_tipo_producto(facturas, tipo_producto)
                porcentaje = calcular_porcentaje(total_tipo_producto, total)
                print('El total acumulado para el tipo de producto {} fue de ${:>10.2f} y '
                      'representa un {:>10.2f}% del total facturado'.format(tipo_producto, total_tipo_producto,
                                                                            porcentaje))
        else:
            print('Primero debe cargar el arreglo de facturas')


if __name__ == '__main__':
    principal()
