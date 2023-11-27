__author__ = 'Catedra Algoritmos y Estructuras de Datos'


# Titulo y carga de datos
print('Suma de cuadrados y promedio de cubos')
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

# Procesos
# Calculo de los cuadrados...
cuad1 = n1 ** 2
cuad2 = n2 ** 2

# Calculo de los cubos...
cubo1 = n1 ** 3
cubo2 = n2 ** 3

# Calculo de la suma y el promedio...
suma = cuad1 + cuad2
prom = (cubo1 + cubo2) / 2

# Visualización de resultados
print('Suma de los cuadrados:', suma)
print('Promedio de los cubos:', prom)
