__author__ = 'Algoritmos y Estructuras de Datos'

import random


def validar_mayor_a(limite, mensaje='Ingrese un numero: '):
    numero = 0
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print('Error!!! El valor a ingresar debe ser mayor a', limite)
    return numero


def validar_rango(inferior, superior, mensaje='Ingrese un numero: '):
    numero = 0
    while numero <= inferior or numero > superior:
        numero = int(input(mensaje))
        if numero < inferior or numero > superior:
            print('Error!!! El valor a ingresar debe ser mayor o igual a', inferior, 'y menor o igual a', superior)
    return numero


def menu():
    cadena = 'Menu de Opciones\n' \
             '1 ---- Cargar Codigos de Productos\n' \
             '2 ---- Costo Total de Produccion de un Producto\n ' \
             '3 ---- Costo Total por Categoria (ordenado) \n' \
             '4 ---- Determinar Categoria que mas fabrico\n' \
             '0 ---- Salir\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def generar_costos_produccion():
    v = []
    for i in range(10):
        v.append(random.uniform(1000, 15000))
    return v


def generar_productos(vector, n):
    for i in range(n):
        # codigo = validar_rango(1, 80, 'Ingrese el codigo para el producto' + \
        #                        str(i + 1) + ': ')
        codigo = random.randint(1, 80)
        vector.append(codigo)


def contar_en_vector(vector, x):
    total = 0
    for prod in vector:
        if prod == x:
            total += 1
    return total


def obtener_costo(costos, codigo):
    pos = codigo % 10
    return costos[pos]


def generar_total_por_categoria(productos, costos):
    v = [0] * len(costos)
    for prod in productos:
        pos = prod % 10
        costo = obtener_costo(costos, prod)
        v[pos] += costo
    return v


def mostar_vector(vector):
    print('Valores cargados en el vector:')
    for i in range(len(vector)):
        print('\t vector[', i, '] = ', vector[i])


def ordenar(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]


def generar_cantidad_por_categoria(productos, tam):
    vc = [0] * tam
    for prod in productos:
        pos = prod % 10
        vc[pos] += 1
    return vc


def buscar_mayor(vector):
    mayor = vector[0]
    categoria = 0
    for i in range(1, len(vector)):
        if vector[i] > mayor:
            mayor = vector[i]
            categoria = i
    return categoria


def principal():
    opcion = -1
    costos = generar_costos_produccion()
    productos = []

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            n = validar_mayor_a(0, 'Ingrese la cantidad de productos a cargar: ')
            generar_productos(productos, n)
            # mostar_vector(productos)

        elif opcion == 2:
            codigo = validar_rango(1, 80, 'Ingrese el codigo a buscar: ')
            total_producido = contar_en_vector(productos, codigo)
            costo_produccion = obtener_costo(costos, codigo)
            print('El total producido por el producto', codigo,
                  'fue de $', total_producido * costo_produccion)

        elif opcion == 3:
            va = generar_total_por_categoria(productos, costos)
            ordenar(va)
            mostar_vector(va)

        elif opcion == 4:
            vc = generar_cantidad_por_categoria(productos, len(costos))
            mayor_categoria = buscar_mayor(vc)
            print('La mayor categoria que se produjo fue:', mayor_categoria)


if __name__ == '__main__':
    principal()
