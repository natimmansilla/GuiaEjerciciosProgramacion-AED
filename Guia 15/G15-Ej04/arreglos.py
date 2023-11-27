def validar_tamanio():
    n = int(input('Ingrese el tamaño del vector: '))
    while n <= 0:
        n = int(input('El tamaño debe ser positivo. Ingrese otro: '))
    return n


def cargar(tam):
    v = []
    for i in range(tam):
        dato = int(input('Ingrese v[' + str(i) + ']: '))
        v.append(dato)
    return v


def elegir_mayores(a,b):
    c = [0] * len(a)
    for i in range(len(a)):
        if a[i] > b[i]:
            c[i] = a[i]
        else:
            c[i] = b[i]
    return c
