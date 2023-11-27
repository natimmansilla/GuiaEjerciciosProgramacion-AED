from funciones import *


def principal():

    print("Puntajes del deportista")
    print("Ingrese el puntaje de los 9 jueces")

    puntajes = [0] * 9
    llenar_vector_enteros_random(puntajes, 7, 10)
    mostrar_vector(puntajes)

    ordenar_vector(puntajes)
    print("Luego de ordenar")
    mostrar_vector(puntajes)

    print("Los tres mejores puntajes son:", end="")
    print(puntajes[-1], puntajes[-2], puntajes[-3])

    cantidad = contar_mayores(puntajes, 6)
    print(cantidad, "jueces puntuaron más de 6")

    prom = calcular_promedio(puntajes)
    print("Puntaje promedio:", prom)

    print("La menor nota es", puntajes[0])
    print("Se repitio", contar_menor(puntajes))

    print("Puntajes sin repeticiones")
    sin_repeticiones = buscar_distintos(puntajes)
    mostrar_vector(sin_repeticiones)


if __name__ == '__main__':
    principal()
