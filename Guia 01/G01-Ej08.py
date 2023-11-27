__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Cálculo del perímetro de un cuadrado')
area = float(input('Ingrese el área del cuadrado: '))

# Procesos
lado = pow(area, 0.5)
perimetro = 4 * lado

# Presentación de resultados
print('El perímetro del cuadrado es:', perimetro)
