__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Procesamiento de Numeros Pares e Impares')

sumatoria = 0
cantidad_pares = 0
cantidad_impares = 0
ingreso_cero = False
anterior = -1
alternan = True

numero = int(
    input('Ingrese un numero (finaliza cuando ingrese un numero negativo): '))
while numero >= 0:
    if 50 < numero < 100:
        sumatoria += numero

    paridad = numero % 2
    if paridad == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    if numero == 0:
        ingreso_cero = True

    if anterior == paridad:
        alternan = False
    anterior = paridad
    numero = int(input('Ingrese otro numero a procesar: '))

print('Resultados')
print('=' * 80)
print('La sumatoria de los numeros comprendidos entre 50 y 100 fue de', sumatoria)
print('La cantidad de numeros pares procesados fue de', cantidad_pares)
print('La cantidad de numeros impares procesados fue de', cantidad_impares)
if ingreso_cero:
    print('El usuario al menos ingreso un numero cero en la secuencia')

if alternan:
    print('La secuencia tiene numeros pares e impares alternados')
else:
    print('La secuencia no tiene numeros pares e impares alternados')
