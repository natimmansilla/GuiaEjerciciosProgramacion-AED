def quitar_barra_n(cadena):
    if cadena[-1] == '\n':
        cadena = cadena[:-1]

    return cadena


def separar_datos(cadena):
    l = cadena[:6].strip()
    n = cadena[7:28].strip()
    p1 = int(cadena[29:31].strip())
    p2 = int(cadena[32:34].strip())
    p3 = int(cadena[35:37].strip())
    tps = int(cadena[38:].strip())
    return l, n, p1, p2, p3, tps


# Retora 0 - libre, 1 - regular y 2 - Aprobado
def determinar_condicion_alumno(a, b, c, d):
    result = 0
    promedio = round((a + b + c) / 3, 0)
    if a >= 7 and b >= 7 \
            and c >= 7 and promedio >= 8 \
            and d >= 8:
        result = 2
    elif ((a >= 4 and b >= 4)
          or (a >= 4 and c >= 4) \
          or (c >= 4 and b >= 4)) \
            and d >= 4:
        result = 1
    return result


def procesar_linea(linea):
    linea = quitar_barra_n(linea)
    return separar_datos(linea)


def calcular_nota_final(p1, p2, p3, tps):
    return (p1 + p2 + p3 + tps) / 4


def porcentaje(porcion, total):
    return porcion * 100 / total
