import random


def cargar(alumnos):
    for i in range(len(alumnos)):
        alumnos[i] = int(input("Ingrese el legajo del alumno " + str(i) + ": "))


def cargar_random(alumnos):
    for i in range(len(alumnos)):
        alumnos[i] = random.randint(70000, 75000)


def mostrar(alumnos):
    for i in range(len(alumnos)):
        print("Legajo del alumno", i, ":", alumnos[i])


def validar():
    n = -1
    while n <= 0:
        n = int(input("Ingrese la cantidad de alumnos: "))
        if n <= 0:
            print("Valor incorrecto!")
    return n


def ordenar(alumnos):
    n = len(alumnos)
    for i in range(n-1):
        for j in range(i+1, n):
            if alumnos[j] < alumnos [i]:
                alumnos[i], alumnos[j] = alumnos[j], alumnos[i]


def buscar(alumnos, x):
    pos = -1
    izq = 0
    der = len(alumnos)-1
    while izq <= der:
        c = (izq+der)//2
        if alumnos[c] == x:
            return c
        elif x > alumnos[c]:
            izq = c + 1
        else:
            der = c - 1
    return pos


def test():
    n = validar()
    alumnos = [0] * n
    cargar_random(alumnos)
    mostrar(alumnos)

    ordenar(alumnos)
    print()
    print("Listado de Alumnos ordenado")
    mostrar(alumnos)

    print()
    x = int(input("Ingrese el legajo del alumno a buscar: "))
    pos = buscar(alumnos, x)

    if pos == -1:
        print("El legajo NO se encuentra!")
    else:
        print("El alumno estaba en la posición:", pos)


if __name__ == "__main__":
    test()
