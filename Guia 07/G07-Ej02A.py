__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('SECUENCIA DE IMPARES')
print('=' * 40)

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro: '))

# Identificamos menor y mayor para saber como ordenar la secuencia
if num1 < num2:
    men, may = num1, num2
else:
    men, may = num2, num1

# Ajustamos valores si son pares
if men % 2 == 0:
    men += 1
if may % 2 == 0:
    may -= 1

# Resultados
print('Secuencia ascendente:')
ascend = range(men, may + 1, 2)
for num in ascend:
    print(num, end=' | ')

print('\nSecuencia descendente:')
descend = range(may, men - 1, -2)
for num in descend:
    print(num, end=' | ')
