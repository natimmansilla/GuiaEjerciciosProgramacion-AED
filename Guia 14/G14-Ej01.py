__author__ = "Catedra de Algoritmos y Estructuras de Datos"


def factorial01(n):
    """Calcula el factorial de n en forma iterativa.

    :param n: el numero al cual se debe calcular el factorial.
    :return: el factorial de n.
    """
    fact = 1
    for i in range(2, n + 1, 1):
        fact *= i
    return fact


def factorial02(n):
    """Calcula el factorial de n en forma recursiva.

    :param n: el numero al cual se debe calcular el factorial.
    :return: el factorial de n.
    """
    if n == 0:
        return 1
    return n * factorial02(n - 1)


def fibonacci01(n):
    """Calcula el termino n-esimo de Fibonacci en forma iterativa.

    :param n: el indice del termino a calcular.
    :return: el valor de Fibonacci para el termino n-esimo
    """
    ant2 = ant1 = 1
    for i in range(2, n + 1):
        aux = ant1 + ant2
        ant2 = ant1
        ant1 = aux
    return ant1


def fibonacci02(n):
    """Calcula el termino n-esimo de Fibonacci en forma recursiva.

    :param n: el indice del termino a calcular.
    :return: el valor de Fibonacci para el termino n-esimo
    """
    if n <= 1:
        return 1
    return fibonacci02(n - 1) + fibonacci02(n - 2)


def mostrar01(n):
    """Muestra recursivamente una secuencia de n mensajes numerados de mayor a menor.

    :param n: el numero de mensajes a mostrar.
    """
    if n > 0:
        print('Mensaje numero', n)
        mostrar01(n-1)


def mostrar02(n):
    """Muestra recursivamente una secuencia de n mensajes numerados de menor a mayor.

    :param n: el numero de mensajes a mostrar.
    """
    if n > 0:
        mostrar02(n-1)
        print('Mensaje numero', n)


def test():
    n = int(input('Ingrese un numero entero no negativo: '))
    print()

    print('Factorial (iterativo) de', n, ':', factorial01(n))
    print('Factorial (recursivo) de', n, ':', factorial02(n))
    print()

    print('Término', n, '-esimo de Fibonacci (iterativo):', fibonacci01(n))
    print('Término', n, '-esimo de Fibonacci (recursivo):', fibonacci02(n))
    print()

    m = int(input('Cuantos mensajes quiere ver? '))
    print()

    print('Primera version recursiva...')
    mostrar01(m)
    print()

    print('Segunda version recursiva...')
    mostrar02(m)


if __name__ == '__main__':
    test()
