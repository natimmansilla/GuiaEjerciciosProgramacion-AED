import random


def cargar_aleatorio(v):
    for i in range(len(v)):
        v[i] = random.randint(1, 10)


def ordenar_ascendente(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        print('Error! Debe ser un valor entre', inf, 'y', sup)
        num = int(input(mensaje))
    return num


def buscar_binario(v, x):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = izq + 1
    return -1


def buscar_mayores(puntos, pos):
    may = list()
    n = len(puntos)
    for i in range(pos + 1, n):
        if puntos[i] > puntos[pos]:
            may.append(puntos[i])
    return may


def sumar_vector(v):
    tot = 0
    for x in v:
        tot += x
    return tot


def promediar_vector(v):
    tot = 0
    for x in v:
        tot += x
    return tot / len(v)


def principal():
    print('CONCURSO DE BAILE')
    n = 7
    puntos = [0] * n
    cargar_aleatorio(puntos)
    ordenar_ascendente(puntos)
    print('Puntaje:', puntos)
    print('Mejores:', puntos[n - 3:])
    x = validar_entre(-1, 10, 'Ingrese puntaje a buscar: ')
    pos = buscar_binario(puntos, x)
    if pos == -1:
        print('No recibieron ningún', x)
    else:
        may = buscar_mayores(puntos, pos)
        if len(may) == 0:
            print('No hubo puntajes mayores a', x)
        else:
            print('Puntajes mayores a', x, ':', may)
    dif = puntos[-1] - puntos[0]
    print('La diferencia entre el mayor y el menor puntaje es', dif)
    total = sumar_vector(puntos)
    if total < 20:
        print('Quedan descalificados')
    else:
        print('El puntaje es', promediar_vector(puntos[1:n]))


if __name__ == '__main__':
    principal()