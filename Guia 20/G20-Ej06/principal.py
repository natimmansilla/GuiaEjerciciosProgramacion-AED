import random
from clase import *


def validar_mayor(referencia, mensage='Ingrese un valor: '):
    numero = referencia
    while numero <= referencia:
        numero = int(input(mensage))
        if numero <= referencia:
            print('Valor incorrecto!!! Debe ser mayor a ', referencia)
    return numero


def validar_rango(minimo, maximo, mensage='Ingrese un valor'):
    numero = minimo - 1
    while numero <= minimo or numero < maximo:
        numero = int(input(mensage))
        if numero <= minimo or numero < maximo:
            print('Error el valor debe estar comprendido entre ', minimo, ' y ', maximo)
    return numero


def cargar_aleatorio(cantidad):
    v = cantidad * [None]
    for pos in range(cantidad):
        dni = random.randint(145, 4600)
        nombre = 'Locatario ' + str(random.randint(145, 4600))
        monto = random.randint(1500, 1510)
        tipo = random.randrange(10)
        v[pos] = Alquiler(dni, nombre, monto, tipo)
    return v


def cargar_vector(cantidad):
    v = cantidad * [None]
    for pos in range(cantidad):
        dni = input('Ingrese el dni del cliente: ')
        nombre = input('Ingrese el nombre del cliente: ')
        monto = float(input('Ingrese el monto del alquiler: '))
        tipo = validar_rango(0, 9, 'Ingrese el tipo de cabana: ')
        v[pos] = Alquiler(dni, nombre, monto, tipo)
    return v


def cantidad_alquileres_mayor_a(vector, monto):
    cantidad = 0
    for alquiler in vector:
        if alquiler.monto > monto:
            cantidad += 1
    return cantidad


def total_recaudado_por_tipo(vector):
    va = [0] * 10
    linea = '{:<6}\t${:<12.2f}\n'
    lista = '{:<6}\t{:<12}\n'.format('Tipo', 'Monto Total') + ('-' * 20) + '\n'

    for alquiler in vector:
        va[alquiler.tipo] += alquiler.monto

    for i in range(len(va)):
        lista += linea.format(i, va[i])

    return lista


def ordenar(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if vector[i].documento < vector[j].documento:
                vector[i], vector[j] = vector[j], vector[i]


def listar_alquileres(vector):
    lista = '{:<15}\t{:<40}\t{:<6}\t{:<10}\n'.format('Documento', 'Nombre', 'Tipo', 'Monto')
    lista += ('-' * 80) + '\n'
    tam = len(vector)
    for pos in range(tam):
        conc = str(vector[pos])
        lista += conc
    return lista


def buscar_menor_monto(vector):
    menores = [vector[0]]
    for i in range(1, len(vector)):
        if vector[i].monto < menores[0].monto:
            menores = [vector[i]]
        elif vector[i].monto == menores[0].monto:
            menores.append(vector[i])
    return menores


def main():
    menu = 'Menu de Opciones\n' \
           '==================================================== \n' \
           '1 \t Cargar vector de alquileres \n' \
           '2 \t Cantidad de alquileres mayor a un valor \n' \
           '3 \t Monto total recaudado por tipo\n' \
           '4 \t Listado Ordenado por dni \n' \
           '5 \t Listado de Alquileres con el menor monto \n' \
           '6 \t Salir\n' \
           'Ingrese su opcion: '

    alquileres = None
    opcion = 0
    while opcion != 6:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = validar_mayor(0, 'Ingrese la cantidad de alquileres a cargar: ')
            # alquileres = cargar_vector(cantidad)
            alquileres = cargar_aleatorio(cantidad)

        if alquileres is not None:
            if opcion == 2:
                monto = validar_mayor(0, 'Ingrese el monto a comparar: ')
                total = cantidad_alquileres_mayor_a(alquileres, monto)
                print('La cantidad de alquileres mayor a ', monto, 'son ', total)

            elif opcion == 3:
                lista = total_recaudado_por_tipo(alquileres)
                print(lista)

            elif opcion == 4:
                ordenar(alquileres)
                print(listar_alquileres(alquileres))

            elif opcion == 5:
                menores = buscar_menor_monto(alquileres)
                print(listar_alquileres(menores))

        else:
            print('No hay alquileres cargados!!!')


if __name__ == '__main__':
    main()
