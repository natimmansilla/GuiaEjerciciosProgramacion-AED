def validar_tamanio():
    n = int(input('Ingrese el tamaño del vector: '))
    while n<= 0:
        n = int(input('El tamaño debe ser positivo. Ingrese otro: '))
    return n


def crear(tam):
    v = []
    for i in range(tam):
        dato = int(input('Ingrese v[' + str(i) + ']: '))
        v.append(dato)
    return v


def contar_repeticiones(v):
    repeticiones = 0
    for elemento in v:
        if elemento == v[-1]:
            repeticiones += 1
    return repeticiones


def buscar_menores(v):
    menores = list()
    for elemento in v:
        if elemento < v[0]:
            menores.append(elemento)
    return menores
