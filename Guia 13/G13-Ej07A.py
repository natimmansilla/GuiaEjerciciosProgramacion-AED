__author__ = 'Algoritmos y Estructuras de Datos'


def es_vocal(letra):
    vocales = 'aeiouAEIOU'
    if letra in vocales:
        return True
    else:
        return False


def es_letra(letra):
    if (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
        return True
    else:
        return False


def es_consonante(letra):
    if es_letra(letra) and es_vocal(letra) == False:
        return True
    else:
        return False


def calcular_porcentaje(cantidad, total):
    if total != 0:
        porcentaje = cantidad * 100 / total
    else:
        porcentaje = 0
    return porcentaje


def principal():
    print('PROCESAMIENTO DE TEXTO')
    print('=' * 80)
    letras_pal = vocales_pal = 0
    segunda_consonante = empieza_vp = expresion_ga = False
    palabras_3voc4let = palabras_cons2 = menor_cons2 = palabras_vpna = palabras_ga = palabras = 0
    texto = input('Ingrese el texto, debe finalizar con punto: ')
    for letra in texto:
        if letra == ' ' or letra == '.':
            # Final de la palabra
            palabras += 1
            if vocales_pal >= 3 and letras_pal > 4:
                palabras_3voc4let += 1
            if segunda_consonante:
                palabras_cons2 += 1
                if palabras_cons2 == 1:
                    menor_cons2 = letras_pal
                elif letras_pal < menor_cons2:
                    menor_cons2 = letras_pal
            if empieza_vp and (anterior == 'n' or anterior == 'a'):
                palabras_vpna += 1
            if expresion_ga:
                palabras_ga += 1
            # Reiniciar variables de palabra
            segunda_consonante = empieza_vp = expresion_ga = False
            letras_pal = vocales_pal = 0
        else:
            # Dentro de la palabra
            letras_pal += 1
            if es_vocal(letra):
                vocales_pal += 1
            if letras_pal == 2 and es_consonante(letra):
                segunda_consonante = True
            if letras_pal == 1 and (letra == 'v' or letra == 'p'):
                empieza_vp = True
            if letra == 'a' and anterior == 'g':
                expresion_ga = True
        anterior = letra
    # Resultados
    print('=' * 80)
    print('Palabras que tenían por lo menos tres vocales y más de cuatro letras:', palabras_3voc4let)
    if palabras_cons2 > 0:
        print('Longitud de la palabra más corta de entre las que contenían una consonante en la segunda posición:',
              menor_cons2)
    else:
        print('No había palabras con una consonante en la segunda posición')
    print('Palabras que empiezan con "v" o con "p" y terminan con "n" o con "a":', palabras_vpna)
    porcentaje = calcular_porcentaje(palabras_ga, palabras)
    print('Porcentaje de palabras que contenían la expresión "ga":', round(porcentaje, 2), '%')


if __name__ == '__main__':
    principal()
