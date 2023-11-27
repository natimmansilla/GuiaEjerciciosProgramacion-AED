import random


def validar_mayor_que(minimo, mensaje):
    n = int(input(mensaje))
    while n <= minimo:
        print('INVALIDO! INGRESE OTRO')
        n = int(input(mensaje))
    return n


def binary_search(v, x):
    # busqueda binaria... asume arreglo ordenado...
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


def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def contar_impares(v):
    print('Vector recortado:', v)
    cant = 0
    for i in range(len(v)):
        if v[i] % 2 != 0:
            cant += 1
    return cant


def contar_impares_no_tan_buena(v, x):
    # Recorre todos los elementos, cuando por estar ordenado el vector
    # se sabe que los mayores a x estan despues de ella
    cant = 0
    for i in range(len(v)):
        if v[i] % 2 != 0 and v[i] > x:
            cant += 1
    return cant


def contar_impares_tambien_buena(v, pos):
    # El recorrido empieza en la posicion de  + 1
    cant = 0
    for i in range(pos + 1, len(v)):
        if v[i] % 2 != 0:
            cant += 1
    return cant


def principal():
    n = validar_mayor_que(0, 'Ingrese cantidad de elementos del vector: ')
    v = [0] * n
    for i in range(n):
        v[i] = random.randint(1, 100)
    selection_sort(v)
    print(v)
    x = int(input('Ingrese elemento a buscar: '))
    pos = binary_search(v, x)
    if pos == -1:
        print('El elemento no existe')
    else:
        cant = contar_impares_no_tan_buena(v, x)
        print('Hay', cant, 'elementos impares mayores que', x)
        cant = contar_impares(v[pos + 1:])
        print('Hay', cant, 'elementos impares mayores que', x)
        cant = contar_impares_tambien_buena(v, pos)
        print('Hay', cant, 'elementos impares mayores que', x)


if __name__ == '__main__':
    principal()