__author__ = "Cátedra de Algoritmos y Estructuras de Datos"

from clase import *


def cargar_alumnos(n):
    v = [None] * n

    for i in range(n):
        print("\nCarga del alumno", i + 1)
        nombre = input("Ingrese nombre: ")
        promedio = float(input("Ingrese el promedio del alumno "))
        v[i] = Alumno(nombre, promedio)

    return v


def mostrar_mejores(v, cantidad):
    print("\n\nLos", cantidad, "mejores promedios son: ")
    for i in range(cantidad):
        print(v[i])


def ordenar_descendente(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].calcular_promedio < v[j].calcular_promedio:
                v[i], v[j] = v[j], v[i]


def calcular_promedio(v):
    prom = 0
    acum = 0
    n = len(v)
    for i in range(n):
        acum += v[i].calcular_promedio

    if n > 0:
        prom = acum / n
    return prom



def principal():
    n = int(input("Ingrese la cantidad de alumnos: "))
    v = cargar_alumnos(n)

    # Buscar los tres meores promedios
    ordenar_descendente(v)
    mostrar_mejores(v, 3)

    # Calcular promedio general
    promedio = calcular_promedio(v)
    print('El promedio general es: ', round(promedio, 2))


if __name__ == "__main__":
    principal()
