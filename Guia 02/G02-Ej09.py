__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Carga de datos
ancho = int(input('Ingrese el ancho del rectángulo: '))
alto = int(input('Ingrese el alto del rectángulo: '))

# Cálculos
perimetro = alto * 2 + ancho * 2
superficie = alto * ancho

# Salidas
print('El perímetro del rectángulo ingresado es:', perimetro)
print('La superficie es:', superficie)