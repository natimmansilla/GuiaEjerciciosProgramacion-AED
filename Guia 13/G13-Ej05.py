__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_digito(letra):
    return letra in '0123456789'


def calcular_promerio(cantidad, total):
    prom = 0
    if total != 0:
        prom = round(cantidad / total, 2)
    return prom


def principal():
    texto = input('Ingrese el texto a procesar. Debe finalizar con punto: ')
    texto = texto.lower()
    cant_digitos = pal_digitos = pal_tiene_la = pal_ll_con_v = 0
    cont_letras = cont_letras_la = 0
    comienza_l = tiene_la = tiene_ll = tiene_v = False
    for letra in texto:
        if letra != ' ' and letra != '.':
            cont_letras += 1

            if es_digito(letra):
                cant_digitos += 1

            if cont_letras == 1 and letra == 'l':
                comienza_l = True
            else:
                if cont_letras == 2:
                    if comienza_l and letra == 'a':
                        tiene_la = True

                    if comienza_l and letra == 'l':
                        tiene_ll = True

                    comienza_l = False

            if letra == 'v':
                tiene_v = True

        else:
            if cant_digitos >= 2:
                pal_digitos += 1

            if tiene_la:
                pal_tiene_la += 1
                cont_letras_la += cont_letras

            if tiene_ll and tiene_v:
                pal_ll_con_v += 1

            cant_digitos = 0
            tiene_la = False
            tiene_ll = False
            tiene_v = False
            cont_letras = 0

    prom = calcular_promerio(cont_letras_la, pal_tiene_la)

    print('La cantidad de palabra con al menos 2 digitos son:', pal_digitos)
    print('La cantidad de palabras que comienzan con \"la\" son:', pal_tiene_la)
    print('El promedio de letras que comienzan con \"la\" es:', prom)
    print('La cantidad de palabras con \"ll\" con alguna \"v\" son', pal_ll_con_v)


if __name__ == '__main__':
    principal()
