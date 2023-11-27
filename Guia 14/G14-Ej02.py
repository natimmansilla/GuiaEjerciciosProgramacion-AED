__author__ = "Catedra de AED"


def sumar_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumar_digitos(n // 10)


def principal():
    n = int(input('Ingrese un numero entero no negativo: '))
    s = sumar_digitos(n)
    print('Suma de los dígitos del número', n, '\b:', s)


if __name__ == '__main__':
    principal()
