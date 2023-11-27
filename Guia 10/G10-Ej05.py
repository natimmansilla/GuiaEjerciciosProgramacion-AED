__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_mayor(valor, mensaje='Ingrese un numero: '):
    numero = 0
    while numero <= valor:
        numero = int(input(mensaje))
        if numero <= valor:
            print('Error!!!! El numero debe ser mayor a ', valor)
    return numero


def porcentaje(total, cantidad):
    por = 0
    if total != 0:
        por = round(cantidad * 100 / total, 2)
    return por


def validar_rango():
    cota_inferior = validar_mayor(0, 'Ingrese la cota inferior de rango: ')
    cota_superior = validar_mayor(0, 'Ingrese la cota superior de rango: ')
    while cota_superior < cota_inferior:
        cota_superior = validar_mayor('Ingrese la cota superior de rango, debe ser mayor a la inferior: ')
    return cota_inferior, cota_superior


def es_multiplo(numero, divisor):
    resto = numero % divisor
    return resto == 0


def es_par(numero):
    return es_multiplo(numero, 2)


def test():
    print('Secuencia de Rangos')
    print('*' * 60)

    primer_numero = 0
    anterior = -1
    primero = True
    cantidad_rango = cant_pares_contig = cant_mult = cant_num = 0

    cota_inferior, cota_superior = validar_rango()

    numero = int(input('Ingresar un numero, la secuencia finaliza cuando ingrese el 0: '))
    while numero != 0:

        cant_num += 1
        if primero:
            primer_numero = numero
            primero = False
        else:
            if es_multiplo(numero, primer_numero):
                cant_mult += 1

        if cota_inferior <= numero <= cota_superior:
            cantidad_rango += 1

        if es_par(anterior) and es_par(numero):
            cant_pares_contig += 1

        anterior = numero
        numero = int(input('Ingrese el siguiente numero de la secuencia (con 0 corta): '))

    print('-' * 60)
    print('Resultados')
    print('-' * 60)

    porc = porcentaje(cant_num, cantidad_rango)
    print('Hay', cantidad_rango, 'números se encuentran en el rango definido entre', cota_inferior, 'y', cota_superior)
    print('Y representa un', porc, '% del total de numeros de la serie')
    print(cant_pares_contig, 'veces que se ingresaron 2 números contiguos pares')
    print(cant_mult, 'números que son múltiplos del primer numero de la secuencia ')


test()
