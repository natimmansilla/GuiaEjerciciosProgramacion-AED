import random
from clase import *


def validar_mayor_cero(mensage='Ingrese un valor: '):
    numero = 0
    while numero <= 0:
        numero = int(input(mensage))
        if numero <= 0:
            print('Valor Incorrecto!!! El valor debe ser mayor a cero.')
    return numero


def cargar_datos():
    regiones = ('Centro', 'Patagonia', 'Noroeste', 'Mesopotamia', 'Cuyo')
    region = random.choice(regiones)
    mes = random.randint(1, 12)
    maxima = random.uniform(0, 60)
    minima = random.uniform(-35, 10)
    return AnalisisTermico(region, mes, maxima, minima)


def buscar_temperatura_promedio(temperaturas):
    suma = 0
    for registro in temperaturas:
        if registro.mes <= 6:
            suma += registro.temperatura_maxima
    return suma / 6


def menor_minima(temperaturas):
    menor = None
    for pos in range(len(temperaturas)):
        if pos == 0:
            menor = temperaturas[pos]
        elif menor.temperatura_minima > temperaturas[pos].temperatura_minima:
            menor = temperaturas[pos]
    return menor


def test():
    temperaturas = []
    menu = 'Menu de Opciones\n ' \
           '============================================== \n' \
           '1 \t Cargar datos termicos \n' \
           '2 \t Informar temperatura maxima promedio \n' \
           '3 \t Menor minima del año \n' \
           '4 \t Salir \n' \
           '---------------------------------------------- \n' \
           'Ingrese su opcion: '

    opcion = 0
    while opcion != 4:
        opcion = int(input(menu))
        if opcion == 1:
            print('Carga de datos')
            n = validar_mayor_cero('Ingrese la cantidad de registros a generar: ')
            for vuelta in range(n):
                analizador = cargar_datos()
                temperaturas.append(analizador)
            print('Arreglo generado')
            print()

        elif opcion == 2:
            if temperaturas != []:
                promedio = buscar_temperatura_promedio(temperaturas)
                print('Promedio de temperaturas maximas en el primer semestre:', round(promedio, 2), 'ºC')
            else:
                print('No hay temperaturas registradas')
            print()

        elif opcion == 3:
            menor = menor_minima(temperaturas)
            if menor is not None:
                print('Menor registro termico:', menor.mes)
                print('\tRegion:', menor.region)
                print('\tFue en el mes:', menor.mes)
            else:
                print('No hay temperaturas registradas.')
            print()


if __name__ == '__main__':
    test()