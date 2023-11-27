__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Analisis de Palabra')
print('=' * 80)

# Lectura de datos
palabra = input('Ingrese la palabara a analizar en mayusculas: ')

# Proceso
largo = len(palabra)
ultima_letra = palabra[largo - 1]

termina_vocal = False
if ultima_letra == 'A' or ultima_letra == 'E' or ultima_letra == 'I' or \
        ultima_letra == 'O' or ultima_letra == 'U':
    termina_vocal = True

# Salida
print('La palabra ingresada tiene una longitud de ', largo, ' letras')
if termina_vocal:
    print('La palabra ingresada termina en vocal')
