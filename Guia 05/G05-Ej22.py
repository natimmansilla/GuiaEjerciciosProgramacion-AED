__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print('ANALISIS ESTADISTICO')

# Ingreso de datos
val1 = int(input('Ingrese 1er valor: '))
val2 = int(input('Ingrese 2do valor: '))
val3 = int(input('Ingrese 3er Valor: '))

# Alguno es multiplo de 5?
algun_multiplos_5 = 'NO'
if val1 % 5 == 0 or val2 % 5 == 0 or val3 % 5 == 0:
    algun_multiplos_5 = 'SI'

# Contar impares
cant_impares = 0
if val1 % 2 != 0:
    cant_impares += 1
if val2 % 2 != 0:
    cant_impares += 1
if val3 % 2 != 0:
    cant_impares += 1

# El mayor supera a la suma de los otros dos?
if val1 > val2 and val1 > val3:
    may = val1
    suma = val2 + val3
elif val2 > val3:
    may = val2
    suma = val1 + val3
else:
    may = val3
    suma = val1 + val2

if may > suma:
    mensaje_may = 'Supera'
else:
    mensaje_may = 'No supera'
mensaje_may = mensaje_may + ' a la suma de los otros dos.'

# Resultados
print('-' * 50)
print(algun_multiplos_5, 'hay algun multiplo de 5')
print('Hay', cant_impares, 'valores impares')
print('El valor mayor es', may, '.', mensaje_may)