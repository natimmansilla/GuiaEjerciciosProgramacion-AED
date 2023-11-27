__author__ = 'Algoritmos y Estructuras de Datos'


def validar_mayor_que(minimo, mensaje='Ingrese un numero'):
    numero = minimo - 1
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print('Error !!!! El valor ingresado de ser mayor a ', minimo)
    return numero


def validar_rango(desde, hasta, mensaje='Ingrese un numero: '):
    numero = desde - 1
    while numero <= desde or numero >= hasta:
        numero = int(input(mensaje))
        if numero <= desde or numero >= hasta:
            print('Error cargue de nuevo, valores de ', desde, 'a', hasta)
    return numero
