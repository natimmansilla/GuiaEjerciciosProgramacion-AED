__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
import random


def mayor_cero():
    numero = 0
    while numero <= 0:
        numero = int(input('Ingrese un numero: '))
        if numero <= 0:
            print('Valor Incorrecto!! Debe ser superior a cero')
    return numero

def generar_lote_numero(cantidad):
    lote = []

    for i in range(cantidad):
        lote.append(random.randint(1, 150))
    return lote


def calcular_promedio(lote, inferior, superior):
    acumulador = 0
    contador = 0
    for pos in range(len(lote)):
        if inferior <= lote[pos] <= superior:
            contador += 1
            acumulador += lote[pos]

    if contador > 0:
        return acumulador / contador
    else:
        return 0


def listar_multiplos(lote, multiplo):
    res = ''
    for pos in range(len(lote)):
        if lote[pos] % multiplo == 0:
            res += str(lote[pos]) + ', '
    return res


def menor_numero_impar(lote):
    menor = 0
    primero = True
    for pos in range(len(lote)):
        if lote[pos] % 2 != 0:
            if primero:
                menor = lote[pos]
                primero = False
            elif menor > lote[pos]:
                menor = lote[pos]
    return menor


def test():
    menu = 'Menu de opciones \n' \
           '=================================\n' \
           '1 \t Promedio ente dos valores \n' \
           '2 \t Menor numero impar \n' \
           '3 \t Imprimir múltiplos \n' \
           '4 \t Salir \n' \
           'Ingrese su opcion: '
    cantidad = mayor_cero()
    lote = generar_lote_numero(cantidad)
    opcion = 0
    while opcion != 4:
        opcion = int(input(menu))
        if opcion == 1:
            valor1 = mayor_cero()
            valor2 = mayor_cero()

            if valor1 > valor2:
                inferior, superior = valor2, valor1
            else:
                inferior, superior = valor1, valor2

            promedio = calcular_promedio(lote, inferior, superior)
            print('El promedio de numeros es ', promedio)

        elif opcion == 2:
            print("El menor numero impar es ", menor_numero_impar(lote))
        elif opcion == 3:
            multiplo = mayor_cero()
            print(listar_multiplos(lote, multiplo))


test()