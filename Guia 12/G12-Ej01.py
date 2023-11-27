__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def is_digit(letra):
    digitos = '0123456789'
    return letra in digitos


def test():
    print('Analisis de Texto - Silaba \"de\" primera mitad')
    print('SIN UTILIZAR ARCHIVOS')
    print('=' * 80)

    texto = input('Ingrese el texto a analizar, finaliza con punto: ')
    tiene_digito = tiene_d = tiene_de = False
    palabra_digito = pal_3letras = pal_4a6letras = pal_mas6letras = cant_letras = pal_demitad = 0
    mayor_longitud = posicion = 0

    for letra in texto:
        if letra == ' ' or letra == '.':

            if tiene_digito:
                palabra_digito += 1

            if cant_letras <= 3:
                pal_3letras += 1
            elif 4 <= cant_letras <= 6:
                pal_4a6letras += 1
            elif cant_letras > 6:
                pal_mas6letras += 1

            if cant_letras > mayor_longitud:
                mayor_longitud = cant_letras

            mitad = cant_letras // 2
            if tiene_de and 0 < posicion <= mitad:
                pal_demitad += 1

            tiene_de = tiene_d = False
            tiene_digito = False
            cant_letras = 0

        else:
            cant_letras += 1

            if is_digit(letra):
                tiene_digito = True

            if letra == 'd' and not tiene_de:
                tiene_d = True
            else:
                if letra == 'e' and tiene_d:
                    tiene_de = True
                    posicion = cant_letras
                tiene_d = False

    print('Presentacion de Resultados')
    print('-' * 80)
    print('La cantidad de palabras que contienen al menos un digito: ', palabra_digito)
    print('La cantidad de palabras que contienen hasta 3 letras es:', pal_3letras)
    print('La cantidad de palabras que contienen entre 4 y 6 letras es:', pal_4a6letras)
    print('La cantidad de palabras que contienen mas de 6 letras es:', pal_mas6letras)
    print('La cantidad de palabras con la expresion \"de\" en la primera mitad es:', pal_demitad)


test()