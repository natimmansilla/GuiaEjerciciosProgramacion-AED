__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_digito(letra):
    return letra in '0123456789'


def es_vocal(letra):
    return letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def es_letra(letra):
    return 'a' <= letra <= 'z' or 'A' <= letra <= 'Z' or letra == 'ñ' or letra == 'Ñ'


def es_consonante(letra):
    return es_letra(letra) and not es_vocal(letra)


def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


def principal():
    # el archivo "entrada.txt" está en la misma carpeta de este programa, en el repositorio GitLab. También está
    # disponible en la Guía 14 junto con el enunciado, para ser descargado.
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # para hacer pruebas cargando el texto por teclado, comentarice las tres líneas anteriores (en las que el
    # texto se carga desde un archivo), y quite el comentario de la línea que sigue (en la que el texto se carga
    # por teclado...
    # texto = input("Ingresar texto (con punto al final): ")

    cl = cl_letrats = 0
    cp_cons35 = cp_digimp = cp_letrats = cp_maprilet = 0
    tiene_cons35 = tiene_digito = tiene_t = tiene_s = tiene_m = tiene_ma = tiene_pri_let = False
    es_primera_letra = True
    anterior = primer_letra = ''

    for letra in texto:
        if letra != ' ' and letra != '.':
            cl += 1

            if es_primera_letra:
                primer_letra = letra
                es_primera_letra = False

            if cl == 3 or cl == 5:
                if es_consonante(letra):
                    tiene_cons35 = True

            if cl >= 4:
                if letra == 'm' or letra == 'M':
                    tiene_m = True
                else:
                    if tiene_m and (letra == 'a' or letra == 'A'):
                        tiene_ma = True
                    tiene_m = False

            if es_digito(letra):
                tiene_digito = True

            if letra == 't' or letra == 'T':
                tiene_t = True
            else:
                if tiene_t and (letra == 's' or letra == 'S'):
                    tiene_s = True

            if letra == primer_letra:
                tiene_pri_let = True

        else:
            if cl > 0:
                if tiene_cons35 and es_vocal(anterior):
                    cp_cons35 += 1

                if tiene_digito and cl % 2 == 1:
                    cp_digimp += 1

                if tiene_t and tiene_s:
                    cp_letrats += 1
                    cl_letrats += cl

                if tiene_ma and tiene_pri_let:
                    cp_maprilet += 1

            cl = 0
            tiene_cons35 = tiene_digito = tiene_s = tiene_t = tiene_ma = tiene_pri_let = False
        anterior = letra

    promedio = calcular_promedio(cl_letrats, cp_letrats)
    print('La cantidad de palabras que contengan una consonante en la 3 o 5 letra de la palabra son:', cp_cons35)
    print('La cantidad de palabras que contienen al menos un dígitos y que son de longitud impar son:', cp_digimp)
    print('El promedio entero de caracteres entre las palabras que contiene al menos una letra "t" y '
          'un letra "s" son:', promedio)
    print('La cantidad de palabras incluyen la expresión "ma" a partir de la cuarta letra de la palabra '
          'y contengan la primera letra del texto son:', cp_maprilet)


if __name__ == '__main__':
    principal()
