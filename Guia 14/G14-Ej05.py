__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_letra(car):
    return 'a' <= car <= 'z' or 'A' <= car <= 'Z'


def es_letra_minuscula(car):
    return 'a' <= car <= 'z'


def es_vocal(car):
    return car in 'aeiouáéíóúAEIOUÁÉÍÓÚ'


def es_consonante(car):
    return es_letra(car) and not es_vocal(car)


def es_digito(letra):
    return '0' <= letra <= '9'


def es_impar(digito):
    return int(digito) % 2 == 1


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

    cl = 0
    r1 = r2 = r3 = r4 = 0
    cant_voc = cant_cons = 0
    clc = cpc = 0
    cant_d = 0
    anterior = ''
    pal_mas_larga = None

    inicia_digito = solo_letras_min = inicia_vocal = tiene_b = tiene_m = tiene_a = False

    for car in texto:
        if car != " " and car != ".":
            cl += 1

            if es_digito(car):
                if es_impar(car) and cl == 1:
                    inicia_digito = True

            elif es_vocal(car):
                cant_voc += 1
                if cl == 1:
                    inicia_vocal = True
                if car == 'a' or car == 'A':
                    tiene_a = True
                if anterior == 'd' or anterior == 'D':
                    cant_d += 1

            elif es_consonante(car):
                cant_cons += 1
                if car == 'b' or car == 'B':
                    tiene_b = True
                elif car == 'm' or car == 'M':
                    tiene_m = True

            if cl == 2 and es_letra_minuscula(car):
               solo_letras_min = True
            elif not es_letra_minuscula(car):
                solo_letras_min = False

            anterior = car

        else:
            if inicia_digito and solo_letras_min:
                r1 += 1

            if inicia_vocal and tiene_b:
                if pal_mas_larga is None:
                    pal_mas_larga = cl
                elif cl > pal_mas_larga:
                    pal_mas_larga = cl

            if cant_cons > cant_voc and not tiene_m and not tiene_a:
                clc += cl
                cpc += 1

            if cant_d >= 2 and es_vocal(anterior):
                r4 += 1

            cl = cant_voc = cant_cons = cant_d = 0
            inicia_digito = solo_letras_min = inicia_vocal = tiene_b = tiene_a = tiene_m = False

    r2 = pal_mas_larga
    r3 = calcular_promedio(clc, cpc)

    print('Primer resultado:', r1)
    print('Segundo resultado:', r2)
    print('Tercer resultado:', r3)
    print('Cuarto resultado:', r4)


if __name__ == '__main__':
    principal()
