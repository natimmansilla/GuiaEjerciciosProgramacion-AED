__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Analisis de texto con silabra dre')
print('-' * 80)

texto = input('Ingrese el texto a analizar, debe finalizar con punto: ')
anterior = ''
cont_letras = pal_3let = cant_pal = pal_terminan_s = pal_dre = 0
tiene_d = tiene_dr = tiene_dre = False
for letra in texto:
    if letra == ' ' or letra == '.':
        if cont_letras > 0:
            cant_pal += 1

            if cont_letras == 3:
                pal_3let += 1

            if anterior == 's':
                pal_terminan_s += 1

            if tiene_dre:
                pal_dre += 1

            tiene_dre = False
            cont_letras = 0
    else:
        cont_letras += 1
        if letra == 'd':
            tiene_d = True
            tiene_dr = False
        else:
            if letra == 'r' and tiene_d:
                tiene_dr = True
            else:
                if letra == 'e' and tiene_dr:
                    tiene_dre = True
                tiene_dr = False
            tiene_d = False
        anterior = letra

porc = 0
if cant_pal != 0:
    porc = round(pal_3let * 100 / cant_pal, 2)

print('Presentacion de Resultados')
print('-' * 80)
print('Cantidad de palabras con exactamente tres letras:', pal_3let)
print('La cantidad de palabras que terminan con \'s\' son:', pal_terminan_s)
print('La cantidad de palabras que contienen \'dre\' son:', pal_dre)
print('El porcentaje de palabra de tres letras respecto del total de palabras del texto es: ', porc, '%', sep='')
