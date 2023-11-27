import random


def cargar_vector_cadenas(v):
    n = len(v)
    for i in range(n):
        v[i] = input()


def cargar_vector_enteros(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input())


def crear_vector_enteros(n):
    v = [0] * n
    for i in range(n):
        v[i] = int(input())

    # Acá sí es obligatorio el return
    return v


def llenar_vector_enteros_random(v, desde, hasta):
    n = len(v)
    for i in range(n):
        v[i] = random.randint(desde, hasta)


def mostrar_vector(v):
    n = len(v)
    for i in range(n):
        print(v[i], end=" ")
    print()


def ordenar_vector(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def buscar(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1


def contar_mayores(v, minimo):
    pos = buscar(v, minimo)
    if pos == -1:
        pos = 0

    n = len(v)
    c = 0
    for i in range(pos, n):
        if v[i] > minimo:
            c += 1

    return c


def calcular_promedio(v):
    suma = 0
    n = len(v)
    for i in range(n):
        suma += v[i]

    promedio = 0
    if n > 0:
        promedio = suma / n

    return promedio


def contar_menor(v):
    menor = v[0]
    n = len(v)
    c = 1
    for i in range(1, n):
        if v[i] == menor:
            c += 1
        else:
            break

    return c


def contar_menor_while(v):
    menor = v[0]
    n = len(v)
    c = i = 1
    while v[i] == menor and i < n:
        c += 1

    return c


def buscar_distintos(v):
    salida = []
    n = len(v)
    for i in range(n):
        if i == 0 or v[i] != v[i - 1]:
            salida.append(v[i])

    return salida
