__author__ = 'Algoritmos y Estructuras de Datos'


def es_digito(car):
    if car >= '0' and car <= '9':
        return True
    else:
        return False


def calcular_promedio(suma, cant):
    if cant == 0:
        return 0
    else:
        return suma / cant


def es_letra(car):
    if (car >= 'a' and car <= 'z') or (car >= 'A' and car <= 'Z'):
        return True
    else:
        return False


def principal():
    print('Parcial 2 [1k15 T2] 2020')
    texto = input('Ingrese texto: ')
    # Variables de palabra (reiniciar)
    solo_digitos = True
    long_pal = 0
    tiene_letras = False
    tiene_ch = False
    ultimo = ''
    # Variables de texto (NO reiniciar)
    suma_solo_digitos = 0
    palabras_solo_digitos = 0
    palabras_digito_letra = 0
    palabras = 0
    palabras_ch = 0
    for car in texto:
        if car == ' ' or car == '.':
            palabras += 1
            if solo_digitos:
                suma_solo_digitos += long_pal
                palabras_solo_digitos += 1
            if es_digito(ultimo) and tiene_letras:
                palabras_digito_letra += 1
            if palabras == 1:
                men_long, men_pos = long_pal, palabras
            elif long_pal < men_long:
                men_long, men_pos = long_pal, palabras
            if tiene_ch:
                palabras_ch += 1
            # Reiniciar datos de palabra
            solo_digitos = True
            long_pal = 0
            tiene_letras = False
            tiene_ch = False
        else:
            # Dentro de la palabra
            long_pal += 1
            if not es_digito(car):
                solo_digitos = False
            if es_letra(car):
                tiene_letras = True
            if long_pal > 4 and car == 'h' and ultimo == 'c':
                tiene_ch = True
            ultimo = car
    # Resultados
    promedio = calcular_promedio(suma_solo_digitos, palabras_solo_digitos)
    print('Promedio de dígitos por palabra, entre las formadas sólo por dígitos:', promedio)
    print('Cantidad de palabras que finalizan con un dígito y tienen al menos una letra:', palabras_digito_letra)
    print('La palabra más corta tiene', men_long, 'caracteres y ocupó la posición', men_pos)
    print('Palabras con "ch" a partir de la cuarta letra:', palabras_ch)


if __name__ == '__main__':
    principal()
