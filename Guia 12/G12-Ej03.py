__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_porcentaje(cantidad, total):
    if total == 0:
        porcentaje = 0
    else:
        porcentaje = round(cantidad * 100 / total)
    return porcentaje


def es_vocal(letra):
    vocales = 'aeiou'
    return letra in vocales


def test():
    print('Análisis de Texto')
    print('*' * 80)

    # Inicialización
    letras_pal = 0
    palabras = 0
    tiene_a = False

    tiene_eiou = False
    palabras_soloa = 0

    # Carga de datos y proceso
    texto = input('Ingrese el texto a analizar, separando las palabras con un espacio y terminando con punto: ')

    for letra in texto:
        if letra == ' ' or letra == '.':
            # Contar palabras
            if letras_pal > 0:
                palabras += 1

            # Buscar mayor
            if palabras == 1:
                mayor = letras_pal
            elif letras_pal > mayor:
                mayor = letras_pal
            # Tiene sólo a?

            if tiene_a and not tiene_eiou:
                palabras_soloa += 1

            # Reiniciar los indicadores de palabra
            letras_pal = 0
            tiene_a = False
            tiene_eiou = False
        else:
            # Determinar longitud
            letras_pal += 1

            # Detectar sólo a
            if es_vocal(letra):
                if letra == 'a':
                    tiene_a = True
                else:
                    tiene_eiou = True

    # Resultados
    print('*' * 80)
    print('La longitud de la palabra más larga es', mayor, 'letras')
    print('Las palabras cuya única vocal es la a son:', palabras_soloa)
    porcentaje = calcular_porcentaje(palabras_soloa, palabras)
    print('El porcentaje de estas palabras sobre el total es', porcentaje, '%')


# Script principal
test()