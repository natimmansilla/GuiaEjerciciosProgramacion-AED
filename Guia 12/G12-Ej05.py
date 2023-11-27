__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


def test():
    print('Análisis de Texto')
    print('*' * 80)

    # Inicialización
    letras_pal = palabras_bym = palabras_pvocal = palabras_iniciofin = 0
    tiene_b = tiene_m = tiene_p = tiene_pvocal = False
    primera = None
    ultima = None

    # Carga de datos y proceso
    texto = input('Ingrese el texto a analizar, separando las palabras con un espacio y terminando con punto: ')

    for letra in texto:
        if letra == ' ' or letra == '.':
            # Tiene m y b a partir de la tercer letra?
            if tiene_b and tiene_m:
                palabras_bym += 1

            # Empieza con p seguida de vocal?
            if tiene_pvocal:
                palabras_pvocal += 1

            # Empieza y termina con la misma letra?
            if primera == ultima:
                palabras_iniciofin += 1

            # Reiniciar los indicadores de palabra
            letras_pal = 0
            tiene_b = False
            tiene_m = False
            tiene_p = False
            tiene_pvocal = False
            primera = None
            ultima = None
            
        else:
            # Contar letras de la palabra
            letras_pal += 1
            # Identificar m y b a partir de la tercer letra
            if letras_pal >= 3:
                if letra == 'b':
                    tiene_b = True
                elif letra == 'm':
                    tiene_m = True

            # Detectar si comienza con p seguida de vocal
            if letras_pal == 1 and letra == 'p':
                tiene_p = True

            if letras_pal == 2 and es_vocal(letra) and tiene_p:
                tiene_pvocal = True

            # Guardar primera letra
            if letras_pal == 1:
                primera = letra
            ultima = letra

    # Resultados
    print('*' * 80)
    print('Palabras tienen una m y una b a partir de la tercer letra:', palabras_bym)
    print('Palabras que comienzan con la letra p seguida de cualquier vocal:', palabras_pvocal)
    print('Palabras que comienzan y terminan con el mismo carácter:', palabras_iniciofin)


# Script principal
test()