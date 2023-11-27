__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


def es_digito(letra):
    digitos = '1234567890'
    return  letra in digitos


def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad / total
    return round(porcentaje, 2)


def test():
    print('Analisis de Texto - vocales y digitos')
    print('=' * 80)

    texto = input('Ingrese el texto a analizar, temina con punto: ')
    cant_vocales = pal_3vocales = cant_palabras = pal_con_digitos = cant_letras = posicion = pal_men_pri_mitad = 0
    orden = 0
    tiene_digito = tiene_m = tiene_me = tiene_men = False
    menor = None
    for letra in texto:
        if letra == ' ' or letra == '.':
            cant_palabras += 1
            if cant_vocales == 3:
                pal_3vocales += 1

            if tiene_digito and cant_letras > 4:
                pal_con_digitos += 1

            mitad = cant_letras // 2
            if tiene_men and posicion <= mitad:
                pal_men_pri_mitad += 1
            
            if menor is None or cant_letras < menor:
                menor = cant_letras
                orden = cant_palabras
            
            cant_letras = 0
            tiene_men = tiene_m = tiene_me = False
        else:

            cant_letras += 1
            if es_vocal(letra):
                cant_vocales += 1

            if es_digito(letra):
                tiene_digito = True

            if letra == 'm' and not tiene_men:
                tiene_m = True
            else:
                if letra == 'e' and tiene_m:
                    tiene_me = True
                else:
                    if letra == 'n' and tiene_me:
                        tiene_men = True
                        posicion = cant_letras
                    tiene_me = False
                tiene_m = False

    porcentaje = calcular_porcentaje(pal_con_digitos, cant_palabras)
    print('La cantidad de palabras con exactamente 3 vocales es:', pal_3vocales)
    print('El porcentaje de palabras con digitos y mas de cuatro letras es: ', porcentaje, '%', sep='')
    print('La cantidad de palabras que tienen \"men\" en la primera mitad de la palabra es:', pal_men_pri_mitad)
    print('El orden de la menor palabra del texto es:', orden)


test()