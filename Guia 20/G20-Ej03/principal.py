import random

from clase import *


def validar_mayor_cero(mensaje='Ingrese un valor: '):
    numero = 0
    while numero <= 0:
        numero = int(input(mensaje))
        if numero <= 0:
            print('Incorrecto!!!! El valor debe ser mayor a cero.')
    return numero


def cargar_deuda():
    nombres = ('Josefa Prueba', 'Alberta Prueba', 'Antonia Prueba', 'Carla Pruebo', 'Roberto Prueba', 'Esteban Prueba')
    nombre = random.choice(nombres)
    deuda = random.randint(100, 3500)
    return Deuda(nombre, deuda)


def principal():
    print('Deuda del Almacen')
    print('=' * 80)

    n = validar_mayor_cero('Ingrese la cantidad de deudas a procesar: ')
    monto_maximo = validar_mayor_cero('Ingrese el monto maximo a comparar: ')
    total = 0
    menor = None
    cant_debajo_maximo = 0

    v = n * [None]
    for vuelta in range(n):
        v[vuelta] = cargar_deuda()

    for deuda in v:
        total += deuda.monto

        if menor is None or menor.monto > deuda.monto:
            menor = deuda

        if deuda.monto < monto_maximo:
            cant_debajo_maximo += 1

    promedio = total / n
    porcentaje = round(cant_debajo_maximo * 100 / n, 2)

    print('=' * 80)
    print('Visualizacion de resultados')
    print('_' * 80)
    print('El almacen tiene que cobrar un fiado promedio de', promedio, 'pesos')
    print('Hay un', porcentaje, '% de clientes con una deuda menor a', monto_maximo, 'pesos')
    print('La menor deuda es:', menor)


if __name__ == '__main__':
    principal()