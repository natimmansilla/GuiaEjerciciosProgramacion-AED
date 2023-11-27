__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Datos
edad1 = int(input('Participante 1 - Ingrese edad: '))
edad2 = int(input('Participante 2 - Ingrese edad: '))
edad3 = int(input('Participante 3 - Ingrese edad: '))

minimo = int(input('Ingrese edad minima para participar: '))

# Proceso y resultado
if edad1 >= minimo and edad2 >= minimo and edad3 >= minimo:
    print('TODOS los participantes cumplen con la edad mínima')
else:
    print('NO TODOS los participantes cumplen con la edad mínima')
