from soporte import *


def procesar():
    n = validar_mayor_que(0, "Ingrese el tamaño del vector: ")
    vec = n * [0]
    read(vec)

    prom = promedio(vec)
    cont = contar_mayores(vec, prom)

    print("Promedio de valores:", prom)
    print("Cantidad de valores mayores al promedio:", cont)


if __name__ == "__main__":
    procesar()