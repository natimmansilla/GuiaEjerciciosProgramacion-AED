import math


def validar_mayor_cero(mensage='Ingrese un numero: '):
    numero = 0
    while numero <= 0:
        numero = int(input(mensage))
        if numero <= 0:
            print('Numero incorrecto!!! El numero debe ser mayor a cero')
    return numero


def es_primo(numero):
    primo = True
    if numero % 2 == 0:
        primo = False

    else:
        tope = math.ceil(math.sqrt(numero))
        for i in range(3, tope):
            if numero % i == 0:
                primo = False
                break
    return primo
