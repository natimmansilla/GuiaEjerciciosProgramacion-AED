__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Palabra enmascarada')
palabra = input('Ingrese palabra a enmascarar: ')

# Procesos

n = len(palabra)
asteriscos = "*" * (n-2)
enmascarada = palabra[0] + asteriscos + palabra[n-1]

# Resultados
print('\nLa palabra enmascarada es:', enmascarada)