import math

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Procesamiento de puntos en el plano')
print('_' * 80)
n = int(input('Ingrese la cantidad de puntos a procesar: '))

cant_primer_cuadrante = 0
cant_tercer_cuadrante = 0
mayor_distancia = 0
mayor_punto = ()

for vuelta in range(n):
    eje_x = float(input('Ingrese el valor de la abscisa del punto: '))
    eje_y = float(input('Ingrese el valor de la ordenada del punto: '))

    if eje_x > 0:
        if eje_y > 0:
            cuadrante = "primer"
            cant_primer_cuadrante += 1
        else:
            cuadrante = "cuarto"
    else:
        if eje_y > 0:
            cuadrante = "segundo"
        else:
            cuadrante = "tercer"
            cant_tercer_cuadrante += 1

    print('El punto (', eje_x, ',', eje_y, ') ',
          'se encuentra en el ', cuadrante, ' cuadrante', sep='')

    distancia_origen = math.sqrt(pow(eje_x, 2) + pow(eje_y, 2))
    if distancia_origen > mayor_distancia:
        mayor_distancia = distancia_origen
        mayor_punto = eje_x, eje_y

    print('-' * 80)

print('_' * 80)
print('La cantidad de puntos en el primer cuadrante fue de: ', cant_primer_cuadrante)
print('La cantidad de puntos en el tercer cuadrante fue de: ', cant_tercer_cuadrante)
print('El punto con mayor distancia al origen fue (', mayor_punto[0], ',', mayor_punto[1], ")", sep='')
