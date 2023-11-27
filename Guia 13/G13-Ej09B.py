"""
   Ejercicio 9 - Guia de Ejercicios Semana 12
"""


def es_vocal(car):
    # if car in 'aeiouáéíóú':
    #  return True
    # else:
    #  return False
    return car in 'aeiouáéíóú'
    # return car in ('a', 'e', 'i', 'o', 'u')


def es_consonante(car):
    return car in 'bcdfghjklmnpqrstvwxyz'


def inicio():
    print('Analizador de Texto')
    print('Ingrese el texto a analizar (finaliza con punto): ')
    cadena = input()
    cadena = cadena.lower()

    contador_palabras = 0
    contador_letras_palabra = 0
    # acumulador_letras = 0
    contador_vocales = 0
    contador_consonantes = 0
    contador_pal_punt0_1 = 0
    bandera_letra_s = bandera_letra_s_vocal = False
    contador_pal_punto_3 = 0
    bandera_comienza_ultima_letra = False
    contador_pal_punto_4 = 0
    ultima_letra = None

    for car in cadena:
        if car == '.' or car == ' ':
            # Fin de palabra

            # Control más de un espacio seguido
            if contador_letras_palabra == 0:
                continue

            contador_palabras += 1

            if contador_vocales > contador_consonantes:
                contador_pal_punt0_1 += 1

            if contador_palabras == 1 or contador_letras_palabra < menor:
                menor = contador_letras_palabra

            if bandera_letra_s_vocal:
                contador_pal_punto_3 += 1

            if bandera_comienza_ultima_letra:
                contador_pal_punto_4 += 1

            ultima_letra = anterior

            # Reinicialización de contadores y banderas de la palabra
            contador_letras_palabra = 0
            contador_vocales = contador_consonantes = 0
            bandera_letra_s = bandera_letra_s_vocal = False
            bandera_comienza_ultima_letra = False

            # Fin sector fin palabra
        else:
            # Dentro de Palabra
            contador_letras_palabra += 1
            if es_vocal(car):
                contador_vocales += 1
            else:
                if es_consonante(car):
                    contador_consonantes += 1
            if car == 's':
                bandera_letra_s = True
            else:
                if bandera_letra_s and es_vocal(car):
                    bandera_letra_s_vocal = True
                bandera_letra_s = False
            # Versión de condición sin necesidad de inicializar ultima_letra aportada por alumno.
            # if contador_palabras > 0 and contador_letras_palabra == 1 and car == ultima_letra:
            if contador_letras_palabra == 1 and car == ultima_letra:
                bandera_comienza_ultima_letra = True
        # Fin sector dentro de palabra
        anterior = car

    print('\n\n Resultados')
    print('===========================>')
    if contador_palabras > 0:
        print('Cantidad de palabras:', contador_palabras)
        porcentaje = contador_pal_punt0_1 * 100 / contador_palabras
        print(f'Porcentaje punto 1: {porcentaje}%')
        print(f'La palabra con menos letras tuvo {menor} letras')
        print(f'La cantidad de palabras con s+vocal fue {contador_pal_punto_3}')
        print(
            f'La cantidad de palabras que comenzaron con la última letra de la palabra anterior fue {contador_pal_punto_4}')
    else:
        print('No cargó nada')


# Script Principal
inicio()
