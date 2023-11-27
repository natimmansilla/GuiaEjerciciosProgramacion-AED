__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Conversion de distancias')
pies = float(input('Ingrese la distancia en pies que desea convertir: '))

# Procesos
yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

# Presentacion de resultados
print('En', pies, 'pies hay', yardas, 'yardas')
print('En', pies, 'pies hay', pulgadas, 'pulgadas')
print('En', pies, 'pies hay', centimetros, 'centimetros')
print('En', pies, 'pies hay', metros, 'metros')
