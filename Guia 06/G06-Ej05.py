__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Buscar el mayor de los valores')
print('=' * 80)

CANTIDAD_VALORES = 10000  # Constante con la cantidad de valores requeridos
mayor = None             # Hasta el momento no se conoce el mayor
contador_positivos = 0   # Inicialización del contador en 0
i = 0                    # Variable para controlar la cantidad de números generados

while i < CANTIDAD_VALORES:
    n = random.randint(-100000, 100000)

    # Si es el primer valor evaluado o si este es mayor al mayor actual
    if mayor is None or n > mayor:
        # Actualizar el nuevo mayor
        mayor = n

    # Contar los positivos para calcular el porcentaje
    if n > 0:
        contador_positivos += 1

    i += 1

# Cálculo del porcentaje de positivos
porcentaje = contador_positivos * 100 / CANTIDAD_VALORES

print('El mayor valor de los 10000 numeros aleatorios es:', mayor)
print('El porcentaje de positivos respecto al total es: ',
      str(round(porcentaje, 2)) + '%')
print("Fin del programa :)")
