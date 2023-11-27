__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_vocal(letra):
    vocales = 'aeiouáéíóú'
    return letra in vocales


def calcular_porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round(muestra * 100 / total, 2)
    return porc


def main():
    print('Analisis de Texto - Silabas \"pa\"')
    print('-' * 80)

    cont_letras = cant_pal_pa = cant_vocales = cant_pal_dosvocales = 0
    cant_palabras = cant_pal_5letras = 0

    tiene_p = tiene_pa = tiene_n = False
    texto = input('Ingrese el texto a analizar, debe finalizar con punto: ')
    for letra in texto:
        if letra == ' ' or letra == '.':
            if cont_letras > 0:
                cant_palabras += 1
                if tiene_pa and tiene_n:
                    cant_pal_pa += 1

                if cant_vocales > 2:
                    cant_pal_dosvocales += 1

                if cont_letras > 5:
                    cant_pal_5letras += 1

            tiene_p = False
            tiene_pa = False
            cant_vocales = 0
            cont_letras = 0
        else:
            cont_letras += 1
            if cont_letras == 1 and letra == 'p':
                tiene_p = True
            else:
                if tiene_p and letra == 'a':
                    tiene_pa = True
                tiene_p = False

            if cont_letras > 3:
                if es_vocal(letra):
                    cant_vocales += 1

            tiene_n = False
            if letra == 'n':
                tiene_n = True

    porcentaje = calcular_porcentaje(cant_pal_pa, cant_palabras)
    print('La cantidad de palabras que empiezan con \"pa\" y terminan con \"s\" es:', cant_pal_pa)
    print('El porcentaje de la cantidad anterior sobre el total del texto es: ', porcentaje, '%', sep='')
    print('La cantidad de palabras con mas de 2 vocales a partir  de la tercera letra es:', cant_pal_dosvocales)
    print('La cantidad de palabras con mas de cinco letras es:', cant_pal_5letras)


main()
