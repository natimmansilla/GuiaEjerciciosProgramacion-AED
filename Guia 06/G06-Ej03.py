__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print("Seleccione la opción del menú que prefiera:")
print("1- Calcular promedio de 1.000 números aleatorios.")
print("2- Buscar el mayor de 10.000 números aleatorios.")
print("3- Buscar el menor de 100.000 números aleatorios.")
print("Cualquier numero- Salir.")
op = int(input("Opción:"))

while op > 0 and op < 4:
    if op == 1:
        acumulador = 0
        i = 0
        while i < 1000:
            n = random.randint(0, 100000)
            acumulador += n
            i += 1
        promedio = acumulador / i
        print("El promedio es", promedio)
    elif op == 2:
        mayor = 0
        i = 0
        while i < 10000:
            n = random.randint(0, 100000)
            if mayor < n:
                mayor = n
            i += 1
        print("El mayor es", mayor)
    else:
        menor = 100000
        i = 0
        suma = 0
        cont = 0
        while i < 5000:
            n = random.randint(0, 100000)
            if menor > n:
                menor = n
            if n < 10000:
                suma += n
                cont += 1
            i += 1
        if cont != 0:
            p = suma / cont
        else:
            p = 0
        print("El menor es", menor, "y el promedio de los menores a 10000 es:", p)

    print("Seleccione la opción del menú que prefiera:")
    print("1- Calcular promedio de 1.000 números aleatorios.")
    print("2- Buscar el mayor de 10.000 números aleatorios.")
    print("3- Buscar el menor de 100.000 números aleatorios.")
    print("Cualquier numero- Salir.")
    op = int(input("Opción:"))

print("Fin del programa :)")
