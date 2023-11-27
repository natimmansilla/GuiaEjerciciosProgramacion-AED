__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Analisis de Texto')
print('=' * 80)

vocales = 'aeiouAEIOU'
clet = cpal = cpecv = palabras_li = palabras_menos_4 = 0
emp_conso = tiene_li = False
car_ant = ''
texto = input('Ingrese el texto a analizar, separados por blancos y termina en punto: ')
for caracter in texto:

    if caracter == ' ' or caracter == '.':
        if clet > 0:
            cpal += 1
            if emp_conso and car_ant in vocales:
                cpecv += 1

            if tiene_li:
                palabras_li += 1

            if clet < 4:
                palabras_menos_4 += 1
        clet = 0
        emp_conso = False
        tiene_li = False

    else:
        clet += 1
        if clet == 1:
            if caracter not in vocales:
                emp_conso = True

        elif clet > 3:
            if car_ant == 'l' and caracter == 'i':
                tiene_li = True

    car_ant = caracter

if cpal > 0:
    print('Hay', cpecv, ' palabras en el texto que empiezan con consonante y terminan con vocal')
    print('Hay', palabras_li, 'palabras en el texto que poseen la secuencia "li" a partir de la tercer letra')
    por = palabras_menos_4 * 100 / cpal
    print('Hay', palabras_menos_4, 'palabras en el texto con menos de 4 letras y representan el', por,
          '% de palabras del texto')
else:
    print('No se ha ingresado un texto para analizar')
