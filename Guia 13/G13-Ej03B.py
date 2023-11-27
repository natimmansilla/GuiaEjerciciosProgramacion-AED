__author__ = 'Felipe'

"""
    Programa que soluciona el enunciado tipo parcial 1 publicado como Ejercicio 3 en la Guía 11
"""


def es_vocal(letra):
    vocales = ('a', 'e', 'i', 'o', 'u')
    return letra in vocales


def leer_texto():
    texto = input('Ingrese el texto (termina con "." y las plabras se separan por espacio)\n')
    while texto[-1] != '.':
        print('Error: el texto debe terminar con "."')
        texto = input('Ingrese el texto (termina con "." y las plabras se separan por espacio)\n')
    texto = texto.lower()
    return texto


def pausa():
    input('\n\nPresione enter para continuar...\n')


def test():
    # Inicialización de contadores y acumuladores Generales
    acumulador_letras = 0
    contador_palabras = 0
    cont_pal_term_vocal = 0
    cont_pal_l_vocal = 0
    orden_mas_larga = 0
    letras_mas_larga = 0
    contador_letras = 0
    ultima_letra = ' '
    vino_l = False
    vino_l_vocal = False

    texto = leer_texto()

    for car in texto:
        if car != ' ' and car != '.':  # Por verdadero estoy procesando las letras dentro de una palabra
            # Cuento las letras de la palabra
            contador_letras += 1

            # Detecto si vino l + vocal
            if car == 'l':
                vino_l = True
            else:
                if vino_l and es_vocal(car):
                    vino_l_vocal = True
                vino_l = False

            # Me guardo cada letra para tener la última cuando la palabra termine
            ultima_letra = car

        else:  # Por el falso esto al final de una palabra (o entre 2 palabras, parado en el espacio)
            # Cuento las palabras
            contador_palabras += 1

            # Acumulo las letras para tener el total de letras para el promedio
            acumulador_letras += contador_letras

            # Cuentos las palabras con la última letra vocal
            if es_vocal(ultima_letra):
                cont_pal_term_vocal += 1

            # Chequeo si la palabra anterior fue más larga y guardo los datos si asi fuera
            if contador_palabras == 1 or contador_letras > letras_mas_larga:
                letras_mas_larga = contador_letras
                orden_mas_larga = contador_palabras

            # Cuento las palabras con l + vocal
            if vino_l_vocal:
                cont_pal_l_vocal += 1

            # Vuelvo al inicio los contadores y banderas para la próxima palabra
            contador_letras = 0
            vino_l = False
            vino_l_vocal = False

    print('\n\nTexto procesado correctamente...\n\n')
    texto_cargado = True
    pausa()

    # Mostrar promedio
    if contador_palabras > 0:
        promedio = acumulador_letras / contador_palabras
    else:
        promedio = 0
    print('El promedio de letras por palabra fue:', promedio)
    pausa()
    # Mostrar terminadas en vocal
    print('La cantidad de palabras terminadas en vocal fue:', cont_pal_term_vocal)
    pausa()
    # Mostrar terminadas en vocal
    print('La ', orden_mas_larga, '° fue la palabra más larga, y tuvo ', letras_mas_larga, ' letras', sep='')
    pausa()
    # Mostrar terminadas en vocal
    print('La cantidad de palabras que incluyeron "l + <vocal>" fue:', cont_pal_l_vocal)
    pausa()


test()
