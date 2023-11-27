__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_promedio(suma, total):
    if total != 0:
        promedio = round(suma / total, 2)
    else:
        promedio = 0
    return promedio


def es_mayuscula(letra):
    if letra >= 'A' and letra <= 'Z':
        return True
    else:
        return False


def es_numero(letra):
    numeros = '0123456789'
    if letra in numeros:
        return True
    else:
        return False


def test():
    print('Análisis de Texto')
    print('*' * 80)

    # Inicialización
    letras_pal = 0
    palabras_mayusc = 0
    cant_numeros = 0
    cant_e = 0
    palabras_e = 0
    palabras_impar = 0
    letras_impar = 0

    # Carga de datos y proceso
    texto = input('Ingrese el texto a analizar, separando las palabras con un espacio y terminando con punto: ')

    for letra in texto:
        if letra == ' ' or letra == '.':
            # Tiene más de una e?
            if cant_e > 1:
                palabras_e += 1
            # Longitud impar? Acumular letras y contar
            if letras_pal % 2 != 0:
                palabras_impar += 1
                letras_impar += letras_pal
            # Reiniciar los indicadores de palabra
            letras_pal = 0
            cant_e = 0
        else:
            # Contar letras de la palabra
            letras_pal += 1
            # Empieza con mayúscula?
            if letras_pal == 1 and es_mayuscula(letra):
                palabras_mayusc += 1
            # Contar si es un número
            if es_numero(letra):
                cant_numeros += 1
            # Contar letras e
            if letra == 'e' or letra == 'E':
                cant_e += 1
    # Resultados
    print('*' * 80)
    print('Palabras que empiezan con mayúscula:', palabras_mayusc)
    print('Numeros del 0 al 9 en todo el texto:', cant_numeros)
    print('Palabras que tienen más de una e:', palabras_e)
    promedio = calcular_promedio(letras_impar, palabras_impar)
    print('Promedio de letras por palabra, para las palabras de longitud impar:', promedio)


# Script principal
test()
