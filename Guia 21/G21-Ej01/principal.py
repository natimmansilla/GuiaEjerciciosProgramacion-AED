__author__ = 'Algoritmos y Estructuras de Datos'

from ModuloEjercicio1 import *


def main():
    lineas = int(input("Ingrese cantidad de líneas: "))
    paradas = int(input("Ingrese la cantidad de paradas: "))

    # Carga de datos
    matriz = cargar_matriz_pasajeros(lineas, paradas)
    print(matriz)

    # Punto 1
    total_por_linea = pasajeros_por_linea(matriz, lineas, paradas)
    for i in range(len(total_por_linea)):
        print("La cantidad de pasajeros de la linea", i, "fue de: ", total_por_linea[i])

    # Punto 2
    parada = int(input("Ingrese parada a consultar: "))
    promedio = promedio_por_parada(parada, matriz, lineas)
    print("El promedio de la parada es de: ", promedio)

    # Punto 3

    # menor cantidad de pasajeros en una linea dada
    linea_menor = int(input("Ingrese linea a controlar: "))
    parada_menor_pasajeros = parada_menor(linea_menor, matriz)
    print("La parada de la linea ", linea_menor, "con menor cantidad de pasajeros es : ", parada_menor_pasajeros,
          "con :", matriz[linea_menor][parada_menor_pasajeros], "Pasajeros")

    # Punto 4
    total = total_pasajeros(matriz)
    print("La recaudación fue de: $", (total * 8.5))


if __name__ == "__main__":
    main()
