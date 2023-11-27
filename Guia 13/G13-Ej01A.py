__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# determina si car es una vocal en mayuscula...
def is_vocal(car):
    if car in 'AEIOU':
        return True

    return False


# calcula el porcentaje y el promedio...
def calcular(cp, cv, ac):
    pc = 0
    pm = 0
    if cp > 0:
        pc = cv * 100 / cp
        pm = ac / cp

    return pc, pm


# funcion principal del programa...
def test():
    print("PROCESADOR DE TEXTO\n")

    # inicializamos variables
    ss = ssi = scc = False
    cvocal = clet = cc = cpal = cif = 0
    csi = cvi = clv = ccc = acu = 0
    primera = ultima = None
    menor = 0

    # carga del texto y conversión a maysucula...
    texto = input("Ingrese el texto a procesar (finalice con un punto): ")
    texto = texto.upper()

    # procesamiento del texto...
    for car in texto:
        if car != " " and car != ".":
            clet += 1

            # detector SI
            if car == "S" and clet == 1:
              ss = True

            else:
                if car == 'I' and ss:
                    ssi = True
                ss = False

            # detector vocales
            if is_vocal(car):
                cvocal += 1

            # inicio - fin
            if clet == 1:
                primera = car

            ultima = car

            # detector cc
            if car == "C":
                cc += 1
                if cc == 2:
                    scc = True

            else:
                cc = 0

        # fin de palabra
        else:
            if clet > 0:
                cpal += 1

                if cpal == 1:
                    menor = clet

                elif clet < menor:
                    menor = clet

                if ssi:
                    csi += 1

                if cvocal == 1:
                    clv += 1

                if is_vocal(ultima) and clet % 2 == 1:
                    cvi += 1

                if scc:
                    ccc += 1

                acu += clet

                if primera == ultima:
                    cif += 1

                clet = cc = cvocal = 0
                ss = ssi = scc = False

    # calculamos promedios y porcentajes
    porc, prom = calcular(cpal, cvi, acu)

    # visualización de resultados...
    print("Cantidad de palabras que comienzan con la expresión \"SI\":", csi)
    print("Cantidad que termina en vocal y con cantidad impar de letras:", cvi)
    print("Cantidad con una única vocal:", clv)
    print("Cantidad que comienza y termina con la misma letra:", cif)
    print("Cantidad que contiene la expresión \"CC\":", ccc)
    print("Porcentaje terminada en vocal y total impar de letras:", porc, "%")
    print("Longitud de la palabra más corta:", menor)
    print("Promedio de letras por palabra:", prom)


# script principal...
test()