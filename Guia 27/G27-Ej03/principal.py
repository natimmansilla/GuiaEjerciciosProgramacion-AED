import os
import pickle
import random

import registro
from registro import Venta


def menu():
    cad = 'Menu de Opciones\n' \
          '=======================================\n' \
          '1 --- Cargar un vector con las ventas de los clientes\n' \
          '2 --- Mostar las ventas cargadas\n' \
          '3 --- Buscar un cliente por nombre\n' \
          '4 --- Generar matriz de acumulacion\n' \
          '5 --- Generar archivo binario\n' \
          '6 --- Filtrar por rango de marca de auto\n' \
          '0 --- Salir\n' \
          'Ingrese su opcion: '
    return int(input(cad))


def validar_mayor_que(minimo, mensaje='Ingrese un numero: '):
    numero = minimo - 1
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error!!!! El valor ingresado debe ser mayor a {}'.format(minimo))
    return numero


def validar_rango(minimo, maximo, mensaje='Ingrese un numero: '):
    numero = minimo - 1
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje))
        if numero < minimo or numero > maximo:
            print('Error!!!! El valor ingresado debe esta comprendido entre {} y {}'.format(minimo, maximo))
    return numero


def add_in_order(vector, venta):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].cliente == venta.cliente:
            pos = med
            break

        if venta.cliente < vector[med].cliente:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [venta]


def cargar_vector(vector, n):
    for i in range(n):
        cliente = registro.crear_nombre_titular()
        tipo_venta = random.randrange(4)
        marca_auto = random.randint(1, 15)
        cantidad_cuotas = random.randint(5, 84)
        monto_plan = random.uniform(1500000, 4500000)
        venta = Venta(cliente, tipo_venta, marca_auto, cantidad_cuotas, monto_plan)
        add_in_order(vector, venta)


def mostrar_vector(vector):
    listado = registro.encabezado()
    for venta in vector:
        listado += str(venta)
    print(listado)


def buscar_cliente(vector, cliente):
    izq, der = 0, len(vector) - 1
    pos = -1
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].cliente == cliente:
            pos = med
            break

        if cliente < vector[med].cliente:
            der = med - 1
        else:
            izq = med + 1

    return pos


def generar_matriz(vector):
    mat = [[0] * 15 for i in range(4)]
    for venta in vector:
        f = venta.tipo_venta
        c = venta.marcar_auto - 1
        mat[f][c] += venta.monto_plan
    return mat


def mostrar_matriz(matriz):
    cad = 'Para el tipo de venta {} de la marca de auto {} se facturo un total de ${:>10.2f}'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(cad.format(f, c + 1, matriz[f][c]))


def generar_archivo(vector, num, nombre_archivo):
    m = open(nombre_archivo, 'wb')
    for venta in vector:
        if venta.tipo_venta != 2 and venta.monto_plan > num:
            pickle.dump(venta, m)
    m.close()


def calcular_promedio(acumulado, cantidad):
    promedio = 0
    if cantidad > 0:
        promedio = acumulado / cantidad
    return promedio


def mostrar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print('No existe un archivo con el nombre {}'.format(nombre_archivo))
        return

    m = open(nombre_archivo, 'rb')
    size = os.path.getsize(nombre_archivo)
    listado = registro.encabezado()
    total = cantidad = 0
    while m.tell() < size:
        venta = pickle.load(m)
        listado += str(venta)
        total += venta.monto_plan
        cantidad += 1
    m.close()
    promedio = calcular_promedio(total, cantidad)
    listado += 'El Monto del Plan promedio de los cliente es de ${:>10.2f}'.format(promedio)
    print(listado)


def acumular_por_marca_auto(vector, marca_inf, marca_sup):
    total_marca = total = 0
    for venta in vector:
        total += venta.cuotas_pagas
        if marca_inf <= venta.marcar_auto <= marca_sup:
            total_marca += venta.cuotas_pagas
    return total_marca, total


def calcular_porcentaje(acumulado, total):
    porcentaje = 0
    if total > 0:
        porcentaje = acumulado * 100 / total
    return porcentaje


def principal():
    ventas = []
    nombre_archivo = 'ventas.dat'
    opcion = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de ventas de planes a cargar: ')
            cargar_vector(ventas, n)

        elif len(ventas) > 0:
            if opcion == 2:
                mostrar_vector(ventas)
            elif opcion == 3:
                nom = input('Ingrese el nombre del cliente a buscar: ')
                pos = buscar_cliente(ventas, nom)
                if pos != -1:
                    x = validar_mayor_que(0, 'Ingrese la cantidad de cuotas a actualizar: ')
                    ventas[pos].cuotas_pagas += x
                    print(ventas[pos])
                else:
                    print('No existe una venta para el cliente {}'.format(nom))

            elif opcion == 4:
                matriz = generar_matriz(ventas)
                mostrar_matriz(matriz)
            elif opcion == 5:
                num = float(input('Ingrese el monto minimo facturado a filtrar: '))
                generar_archivo(ventas, num, nombre_archivo)
                mostrar_archivo(nombre_archivo)
            elif opcion == 6:
                marca_inf = validar_rango(1, 15, 'Ingrese el limite inferior del rango de marcas de auto: ')
                marca_sup = validar_rango(1, 15, 'Ingrese el limite superior del rango de marcas de auto: ')
                total_pago_marca, total_pago = acumular_por_marca_auto(ventas, marca_inf, marca_sup)
                porcentaje = calcular_porcentaje(total_pago_marca, total_pago)
                print('El total de los montos del plan para las marcas comprendidas entre {} y {} fue de '
                      '{:>6} y representan un {:>3.2f}% sobre lo montos totales de planes'.format(marca_inf,
                                                                                                       marca_sup,
                                                                                                       total_pago_marca,
                                                                                                       porcentaje))
        else:
            print('Primero debe cargar el arreglo de ventas de planes')


if __name__ == '__main__':
    principal()
