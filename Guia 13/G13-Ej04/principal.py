from general import *

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def principal():
    # Inicialización
    anterior = ''
    pal_fin_vocal = letras = consonantes = vocales = palabras = cons_pal = letras_pal = pal_comienza_st = 0
    mayor = None
    comienza = tiene_st = False

    # Carga de datos y proceso
    texto = input('Ingrese el texto a analizar, separando las palabras con un espacio y terminando con punto: ')
    texto = texto.lower()
    for letra in texto:
        if letra != ' ' and letra != '.':
            # Dentro de la palabra
            letras_pal += 1
            if es_vocal(letra):
                vocales += 1
            elif es_consonante(letra):
                cons_pal += 1
            if palabras >= 1 and letras_pal == 1 and letra == texto[0]:
                comienza = True
            if letra == 't' and anterior == 's':
                tiene_st = True
        else:
            # Final de la palabra
            palabras += 1
            letras += letras_pal
            consonantes += cons_pal
            if es_vocal(anterior):
                pal_fin_vocal += 1
            if palabras == 1 or cons_pal > mayor[0]:
                mayor = cons_pal, palabras
            if comienza and tiene_st:
                pal_comienza_st += 1
            # Reiniciar
            cons_pal = 0
            letras_pal = 0
            comienza = False
            tiene_st = False
        anterior = letra

    # Resultados
    print('Palabras terminadas en vocal:', pal_fin_vocal)
    porc_voc = calcular_porcentaje(vocales, letras)
    porc_cons = calcular_porcentaje(consonantes, letras)
    print('Hay', round(porc_voc, 2), '% de vocales y', round(porc_cons, 2), '% de consonantes')
    print('La palabra con más consonantes tiene', mayor[0], 'consonantes, y aparece en el orden', mayor[1])
    print('Palabras que comienzan con la primera letra del texto y contienen st:', pal_comienza_st)


if __name__ == '__main__':
    principal()
