__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Constantes
C = 299792.458

# Titulo y carga de datos
print('Calculo de conversion de masa en energia (Einstein)')
masa = float(input('Ingrese la masa del objeto que desea calcular: '))

# Procesos
e = masa * (C ** 2)

# Visualización de resultados
print('La energia de la masa ingresada es:', e)