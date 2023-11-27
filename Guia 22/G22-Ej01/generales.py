__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_mayor_que(desde, mensaje):
    valor = int(input(mensaje))
    while valor <= desde:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def validar_mayor_igual_que(desde, mensaje):
    valor = int(input(mensaje))
    while valor < desde:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def validar_entre(desde, hasta, mensaje):
    valor = int(input(mensaje))
    while valor < desde or valor > hasta:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor
