__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Obtener los ultimos digitos de un numero')
numero = int(input('Ingrese un numero: '))

# Procesos
unidad = numero % 10
decenas = numero % 100

# Presentacion de resultados
print('El ultimo digito del numero', numero, 'es', unidad)
print('Los ultimos 2 digitos del numero', numero, 'son', decenas)
