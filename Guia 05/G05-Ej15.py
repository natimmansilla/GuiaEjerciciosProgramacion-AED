__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Comercio')
print('Carga de Articulos Vendidos')
print('=' * 40)

print('Datos del primer Articulo')
print('_' * 40)
nombre1 = input('Ingrese el nombre del articulo: ')
cantidad1 = int(input('Ingrese la cantidad vendida del articulo: '))
precio1 = float(input('Ingrese el precio unitario del articulo: '))

print('\n')
print('Datos del segundo Articulo')
print('_' * 40)
nombre2 = input('Ingrese el nombre del articulo: ')
cantidad2 = int(input('Ingrese la cantidad vendida del articulo: '))
precio2 = float(input('Ingrese el precio unitario del articulo: '))

print('\n')
print('Datos del tercer Articulo')
print('_' * 40)
nombre3 = input('Ingrese el nombre del articulo: ')
cantidad3 = int(input('Ingrese la cantidad vendida del articulo: '))
precio3 = float(input('Ingrese el precio unitario del articulo: '))

# Calculo de la ganancia obtenida por cada tipo de articulo
ganancia1 = cantidad1 * precio1
ganancia2 = cantidad2 * precio2
ganancia3 = cantidad3 * precio3

# Busqueda de la mayor ganancia
if ganancia1 > ganancia2 and ganancia1 > ganancia3:
    mayor = nombre1, ganancia1
elif ganancia2 > ganancia3:
    mayor = nombre2, ganancia2
else:
    mayor = nombre3, ganancia3

# Salida con calculo de porcentajes
print('El articulo que mayor aporte realizo fue', mayor[0],
      'con una ganancia de $', mayor[1])

total = ganancia1 + ganancia2 + ganancia3
porcentaje = mayor[1] * 100 / total
print('y representa el', round(porcentaje, 2), '% del total de ingresos')
