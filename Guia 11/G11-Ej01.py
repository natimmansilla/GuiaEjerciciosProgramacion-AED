__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Analisis de Texto')
print('=' * 80)

vocales = 'aeiouAEIOU'
texto = input('Ingrese el texto a analizar, separados por blancos y termina en punto: ')
cp = cl = cpev = cpeucpa = 0
emp_vocal = False
ult_car_pal = car_ant = ''

for caracter in texto:
    cl += 1
    if caracter == ' ' or caracter == '.':
        if cl > 1:
            cp += 1
            ult_car_pal = car_ant
            if emp_vocal and car_ant in vocales:
                cpev += 1
                emp_vocal = False
        cl = 0
    else:
        if cl == 1:
            if caracter in vocales:
                emp_vocal = True

            if ult_car_pal == caracter:
                cpeucpa += 1
                ult_car_pal = ''

    car_ant = caracter

if cp > 0:
    por = cpev * 100 / cp

    print('Hay', cpev, 'palabras que empiezan y terminan en vocales que representan el', por, '% de palabras del texto')
    print('Hay', cpeucpa, 'palabras que comienzan con el ultimo caracter de la palabra anterior')
else:
    print('No se ingreso texto a analizar')
