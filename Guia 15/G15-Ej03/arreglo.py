from funciones import es_primo


def crear(tam):
    vec = list()
    for i in range(tam):
        dato = int(input('Ingese el valor para la posicion vec[' + str(i) + ']: '))
        vec.append(dato)
    return vec


def generar_vector_primos(vec):
    primos = []
    for item in vec:
        if es_primo(item):
            primos.append(item)
    return primos


def promedio(vec):
    tam = len(vec)
    if tam > 0:
        suma = 0
        for item in vec:
            suma += item
        return round(suma / tam, 2)
    else:
        return 0


def mostrar(vec):
    tam = len(vec)
    cadena = '['
    for pos in range(tam):
        if pos == (tam - 1):
            cadena += str(vec[pos])
        else:
            cadena += str(vec[pos]) + ' - '

    cadena += ']'
    return cadena
