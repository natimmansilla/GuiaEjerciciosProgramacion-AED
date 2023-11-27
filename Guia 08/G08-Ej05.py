__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

x = random.randint(-50, 50)
y = random.randint(-50, 50)
opcion = -1
while opcion != 0:
    print('-' * 80)
    print('MENU DE TITO EL ROBOT')
    print('Tito se encuentra en la posición (', x, ',', y, ')\n')
    print('1) Girar al norte y avanzar 10 pasos')
    print('2) Girar al sur y avanzar 20 pasos')
    print('3) Girar al este y avanzar 10 pasos')
    print('4) Girar al oeste y avanzar 20 pasos')
    print('0) Salir')
    opcion = int(input('\nIngrese la opcion: '))
    if opcion == 1:
        y += 10
    elif opcion == 2:
        y -= 20
    elif opcion == 3:
        x += 10
    elif opcion == 4:
        x -= 20
    print('-' * 80)
print('Hasta luego!')
