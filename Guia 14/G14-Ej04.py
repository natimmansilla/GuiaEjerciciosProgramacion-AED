import random


def elegir_camino():
    t_caminos = 1, 2, 3
    camino = int(random.choice(t_caminos))
    return camino


def obtener_tiempo_salida():
    camino = elegir_camino()
    if camino == 1:
        print("Camino 1")
        return 3 + obtener_tiempo_salida()
    elif camino == 2:
        print("Camino 2")
        return 5 + obtener_tiempo_salida()
    else:
        print("Camino 3")
        return 7


def principal():
    print("Tiempo total: ", obtener_tiempo_salida())


if __name__ == '__main__':
    principal()
