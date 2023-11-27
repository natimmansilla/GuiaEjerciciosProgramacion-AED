__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_porcentaje(valor, total):
    porc = 0
    if total > 0:
        porc = round(valor * 100 / total, 2)
    return porc


def es_vocal(letra):
    vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    return letra in vocales


def main():
    print('Analizar texto con letras pe')
    print('-' * 80)

    texto = input('Ingrese el texto a analizar, finaliza con punto: ')
    cont_letras = cont_palabras = cont_pal3letras = pal_vocales_tercer_letra = cant_vocales = pal_2vocales = 0
    cant_pe = palabras_mas2_pe = 0
    anterior = ''
    tiene_vocal = False

    for letra in texto:
        if letra == ' ' or letra == '.':
            if cont_letras > 0:
                cont_palabras += 1
                if cont_letras == 3 or cont_letras == 5 or cont_letras == 7:
                    cont_pal3letras += 1

                if cont_letras > 3 and tiene_vocal:
                    pal_vocales_tercer_letra += 1

                if 0 < cant_vocales <= 2:
                    pal_2vocales += 1

                if cant_pe >= 2:
                    palabras_mas2_pe += 1

            cant_pe = 0
            cant_vocales = 0
            tiene_vocal = False
            cont_letras = 0
        else:
            cont_letras += 1
            if es_vocal(letra):
                cant_vocales += 1
                if cont_letras == 3:
                    tiene_vocal = True

            if letra == 'e' and anterior == 'p':
                cant_pe += 1

        anterior = letra

    porc = calcular_porcentaje(pal_2vocales, cont_palabras)
    print('La cantidad de palabras con 3, 5 o 7 letras de longitud son:', cont_pal3letras)
    print('La cantidad de palabras con mas de 3 letras y una vocal en la tercer letra son:', pal_vocales_tercer_letra)
    print('El porcentaje de palabras con 2 vocales sobre el total del texto es: ', porc, '%', sep='')
    print('La cantidad de palabras con mas de una sílaba \'pe\' es:', palabras_mas2_pe)


main()
