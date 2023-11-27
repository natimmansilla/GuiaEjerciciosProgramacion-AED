__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_letra(car):
    return 'a' <= car <= 'z' or 'A' <= car <= 'Z'


def es_vocal(car):
    return car in 'aeiouáéíóúAEIOUÁÉÍÓÚ'


def es_consonante(car):
    return es_letra(car) and not es_vocal(car)


def es_digito(letra):
    return '0' <= letra <= '9'


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
    r1 = r4 = 0
    cant_voc = cant_cons = 0
    clss = cpss = 0
    anterior = ''
    pal_mas_larga = None
    tiene_digito = tiene_p = tiene_s = tiene_ra = tiene_voc = False

    for car in texto:
        if car != " " and car != ".":
            cl += 1

            if es_consonante(car):
                cant_cons += 1

                if car == 'p' or car == 'P':
                    tiene_p = True
                elif car == 's' or car == 'S':
                    tiene_s = True

            elif es_vocal(car):
                cant_voc += 1
                if cl <= 2:
                    tiene_voc = True
                if (anterior == 'r' or anterior == 'R') and (car == 'a' or car == 'A'):
                    tiene_ra = True

            elif es_digito(car):
                tiene_digito = True

            anterior = car
        else:
            if cl % 2 == 0 and cant_cons == cant_voc:
                r1 += 1

            if tiene_digito and not tiene_p:
                if pal_mas_larga is None:
                    pal_mas_larga = cl
                elif cl >= pal_mas_larga:
                    pal_mas_larga = cl

            if tiene_s and cl > 2:
                clss += cl
                cpss += 1

            if tiene_ra and tiene_voc:
                r4 += 1

            cl = 0
            cant_voc = cant_cons = 0
            tiene_digito = tiene_p = tiene_s = tiene_voc = tiene_ra = False

    r2 = pal_mas_larga
    r3 = calcular_promedio(clss, cpss)

    print('Primer resultado:', r1)
    print('Segundo resultado:', r2)
    print('Tercer resultado:', r3)
    print('Cuarto resultado:', r4)


if __name__ == '__main__':
    principal()
