__author__ = "Catedra de AED"


def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    if num < inf:
        print('Inválido!', end=' ')
        return validar_mayor_que(inf, mensaje)
    return num


def sumatoria_pares(n):
    if n == 0 or n == 1:
        return 0

    if n % 2 == 1:
        n -= 1

    return n + sumatoria_pares(n-2)


def principal():
    n = validar_mayor_que(0, 'Ingrese un numero entero no negativo: ')
    s = sumatoria_pares(n)
    print('Suma de los números pares del 0 al', n, '\b:', s)


if __name__ == '__main__':
    principal()
