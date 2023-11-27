__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Cálculo del área de un rectángulo')
perimetro = float(input('Ingrese el valor perímetro del rectángulo: '))
lado1 = float(input('Ingrese el valor del primer lado del rectángulo: '))

# Procesos
lado2 = (perimetro - 2*lado1) / 2
area = lado1 * lado2

# Presentación de resultados
print('El área del rectángulo es:', area)
