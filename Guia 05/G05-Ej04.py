__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Observatorio Metereologico')
print('=' * 80)

# entrada de datos
temp1 = int(input('Ingrese la primer temperatura del dia: '))
temp2 = int(input('Ingrese la segunda temperatura del dia: '))
temp3 = int(input('Ingrese la tercer temperatura del dia: '))
temp4 = int(input('Ingrese la cuarta temperatura del dia: '))

# Procesos

promedio = (temp1 + temp2 + temp3 + temp4) / 4

if temp1 > temp2 and temp1 > temp3 and temp1 > temp4:
    mayor = temp1
else:
    if temp2 > temp3 and temp2 > temp4:
        mayor = temp2
    else:
        if temp3 > temp4:
            mayor = temp3
        else:
            mayor = temp4

if temp1 < temp2 and temp1 < temp3 and temp1 < temp4:
    menor = temp1
else:
    if temp2 < temp3 and temp2 < temp4:
        menor = temp2
    else:
        if temp3 < temp4:
            menor = temp3
        else:
            menor = temp4

supera_promedio = False
if temp1 > promedio or temp2 > promedio or temp3 > promedio or temp4 > promedio:
    supera_promedio = True

# Salidas
print('La temperatura promedio del dia fue de', promedio, 'grados')
print('La temperatura minima fue de', menor, 'grados')
print('La temperatura maxima fue de', mayor, 'grados')
if supera_promedio:
    print('Algunas de las temperaturas tomadas supero a la temperatura promedio del dia')
