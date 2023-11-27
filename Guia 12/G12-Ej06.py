__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_vocal(caracter):
    vocales = 'aeiouáéíóú'
    return caracter in vocales


def leer_numero():
    numero = 0
    while numero <= 0:
        numero = int(input('Ingrese un numero: '))
        if numero <= 0:
            print('Error!!! el numero debe ser mayor a cero')
    return numero


def palabras_superan_promedio(texto, prom):
    cant_palabras = cant_letras = 0
    for caracter in texto:
        if caracter != ' ' and caracter != '.':
            cant_letras += 1
        else:
            if cant_letras > prom:
                cant_palabras += 1
    return cant_palabras


def es_multiplo(numero, divisor):
    resto = numero % divisor
    return resto == 0


def test():
    print('Analizador de Texto las 2 vocales')
    print('*' * 60)

    numero = leer_numero()
    texto = input('Ingrese el texto a analizar, finaliza con punto: ')

    pal_2voc_dif = cant_palabras = cant_letras = cant_let_pal_ant = pal_mult_ant = pal_let_mayor_num = total_letras = 0
    pal_sup_promedio = 0
    es_pri_vocal = True
    hay_2_voc_dif = False
    pri_vocal = ''

    for letra in texto:
        if letra == ' ' or letra == '.':
            if cant_letras > 0:

                cant_palabras += 1

                if hay_2_voc_dif:
                    pal_2voc_dif += 1

                if cant_palabras == 1:
                    cant_let_pal_ant = cant_letras
                else:
                    if es_multiplo(cant_letras, cant_let_pal_ant):
                        pal_mult_ant += 1
                    cant_let_pal_ant = cant_letras

                if cant_letras > numero:
                    pal_let_mayor_num += 1

                total_letras += cant_letras

            es_pri_vocal = True
            hay_2_voc_dif = False
            pri_vocal = ''
            cant_letras = 0

        else:
            cant_letras += 1

            if es_vocal(letra):
                if es_pri_vocal:
                    pri_vocal = letra
                    es_pri_vocal = False
                else:
                    if es_vocal(letra) and letra != pri_vocal:
                        hay_2_voc_dif = True
                        pri_vocal = ''

    if cant_palabras > 0:
        prom = total_letras // cant_palabras
        pal_sup_promedio = palabras_superan_promedio(texto, prom)

    print('La cantidad de palabras con 2 vocales diferentes son:', pal_2voc_dif)
    print('La cantidad de palabras cuya cantidad de letras es multiplo de la anterior son:', pal_mult_ant)
    print('Palabras que tienen mas de ', numero, 'letras son', pal_let_mayor_num)
    print('La cantidad de palabras que superan el promedio de letras de la palabra son', pal_sup_promedio)


test()