__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('SECUENCIA DE IMPARES')
print('=' * 40)

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro: '))

# Definimos límites de la secuencia ascendente
if num1 < num2:
    inicio, fin = num1, num2 + 1
else:
    inicio, fin = num2, num1 + 1

# Corregimos inicio si es par
if inicio % 2 == 0:
    inicio += 1

# Mostramos secuencia
print('Secuencia ascendente')
for num in range(inicio, fin, 2):
    print(num, end=' ')

# Definimos límites de la secuencia descendente
if num1 > num2:
    inicio, fin = num1, num2 - 1
else:
    inicio, fin = num2, num1 - 1

# Corregimos inicio si es par
if inicio % 2 == 0:
    inicio += 1

# Mostramos secuencia
print('\nSecuencia descendente')
for num in range(inicio, fin, -2):
    print(num, end=' ')
