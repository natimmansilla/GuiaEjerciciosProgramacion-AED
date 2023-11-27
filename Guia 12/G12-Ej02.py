__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_procentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


def es_multiplo(numero, divisor):
    resto = numero % divisor
    return resto == 0


def es_par(numero):
    return es_multiplo(numero, 2)


def test():
    # variables para el punto 1
    cant_pares = 0
    cant_numeros = 0

    # variables para el punto 2
    cant_numeros_punto2 = 0

    # variables para el punto 3
    menor = None

    # variables para el punto 4
    # se inicializa con True, suponiendo que se ingresa una secuencia de numeros menores o iguales a 7
    # si dentro del ciclo se encuentra un numero que no cumple se cambia a false
    secuencia_menor_igual7 = True

    print('Ingrese una secuencia de números, la misma termina con un 0 (cero) : ')
    numero = int(input('Ingrese un número (distinto de 0): '))
    while numero != 0:
        cant_numeros += 1

        # punto 1
        # pregunta si es par
        if es_par(numero):
            cant_pares += 1

        # punto 2
        digito = numero
        if numero > 10:
            digito = numero % 10

        if digito == 4 or digito == 5:
            cant_numeros_punto2 += 1

        # punto 3
        # si el numero leido es divisible por 3 realiza proceso de busqueda de menor o menor no esta inicializado
        if es_multiplo(numero, 3):
            if menor is None or numero < menor:
                menor = numero

        # punto 4
        # si encuentra algun valor mayor a 7 ya no cumple
        if numero > 7:
            secuencia_menor_igual7 = False

        numero = int(input('Ingrese un número (distinto de 0): '))

    # punto 1
    # calcula el porcentaje
    porcentaje = calcular_procentaje(cant_pares, cant_numeros)

    # punto 4
    if secuencia_menor_igual7:
        mensaje = 'La secuencia estaba formada sólo por números menores o iguales que 7'
    else:
        mensaje = 'La secuencia NO estaba formada sólo por números menores o iguales que 7'

    # mostrar resultados
    print('\n El porcentaje de números pares sobre la cantidad total de números ingresados: ', porcentaje)
    print('\n La cantidad de números ingresados que tiene su último dígito igual a 4 o igual a 5: ', cant_numeros_punto2)
    print('\n El menor de los números ingresados que son divisibles por 3: ', menor)
    print('\n ', mensaje)


test()