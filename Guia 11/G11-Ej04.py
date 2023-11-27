__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Tratamiento de Caracteres, longitud de palabras')
print('-' * 90)

cl = 0
cl_previa = 0
cantidad_palabras = 0

texto = input('Ingrese el texto a procesar: ')
texto = texto.upper()

for car in texto:
    if car != ' ' and car != '.':
        cl += 1
    else:
        if cl_previa != 0 and cl_previa <= cl:
            cantidad_palabras += 1
        cl_previa = cl
        cl = 0

print('Resultados')
print('-' * 90)
print('Hay', cantidad_palabras, ' que son antecedidas por una de menor o igual longitud en el texto')
