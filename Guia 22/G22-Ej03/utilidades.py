import random

__author__ = 'Algoritmos y Estructuras de Datos'


def validar_mayor(minimo, mensaje="Ingrese un numero: "):
    numero = 0
    while numero <= minimo:
        numero = int(input(mensaje))
        if numero <= minimo:
            print("El numero ingresado no es valido!!! Debe ser mayor a ", minimo)
    return numero


def generar_numero_telefonico():
    caracteristica = str(random.randrange(1, 10))
    numero = "15" + str(random.randrange(1111111, 9999999))
    return caracteristica + "-" + numero


def ordenar(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if vector[i] > vector[j]:
                vector[i], vector[j] = vector[j], vector[i]


def busqueda_binaria(valor, vector):
    izq, der = 0, len(vector) - 1
    while izq <= der:
        med = (izq + der) // 2
        if vector[med] == valor:
            return med

        if valor < vector[med]:
            der = med - 1
        else:
            izq = med + 1
    return -1


def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


if __name__ == '__main__':
    numero_telefono = generar_numero_telefonico()
    print(numero_telefono)
