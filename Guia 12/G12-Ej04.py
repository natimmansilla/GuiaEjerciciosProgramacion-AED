__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_porcentaje(cantidad, total):
    porc = 0
    if total >= 0:
        porc = cantidad * 100 / total
    return round(porc, 2)


def es_par(numero):
    resto = numero % 2
    return resto == 0


def test():
    cantidad_t = pal_unica_t = cant_letra = letras_pal_ant = cant_palabras = pal_mayor_anterior = pal_pares_con_c = 0
    empieza_c = False

    print('La Letra T - Procesamiento de Texto')
    print('=' * 80)

    texto = input('Ingrese el texto a procesar, finaliza con un punto:')

    for caracter in texto:
        if caracter != ' ' and caracter != '.':
            cant_letra += 1

            if caracter == 't':
                cantidad_t += 1

            if cant_letra == 1 and caracter == 'c':
                empieza_c = True

        else:
            if cant_letra > 0:

                cant_palabras += 1

                if cantidad_t == 1:
                    pal_unica_t += 1

                if cant_palabras == 1:
                    letras_pal_ant = cant_letra
                else:
                    if cant_letra > letras_pal_ant:
                        pal_mayor_anterior += 1
                    letras_pal_ant = cant_letra

                if empieza_c and es_par(cant_letra):
                    pal_pares_con_c += 1

            cant_letra = 0
            cantidad_t = 0
            empieza_c = False

    porcentaje = calcular_porcentaje(pal_unica_t, cant_palabras)

    print('Resultados')
    print('=' * 80)
    print('La cantidad de palabras con una sola t son:', pal_unica_t)
    print('y representan el ', porcentaje, '% del total de palabras del texto', sep='')
    print('La cantidad de palabras con cantidad pares de letras y empiezan con c son:', pal_pares_con_c)
    print('La cantidad de palabras que tienen mas letras que la anterior son:', pal_mayor_anterior)


test()