__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Pares e Impares')
print('*' * 80)

# Antes de comenzar el juego, se debe ingresar el récord del campeón (y prever una bandera para detectar si se supera
campeon = int(input('Ingrese record del campeon: '))
superado = False

# Primera ronda entre los retadores:
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print("Primera ronda: Los dados suman:", suma, "(", dado1, "y", dado2, ")")
if suma % 2 != 0:
    retador1 = suma
    retador2 = 0
else:
    retador1 = 0
    retador2 = suma
print("Retador 1:", retador1, "vs Retador 2:", retador2)
# Superaron el record?
if retador1 > campeon or retador2 > campeon:
    superado = True

# Segunda ronda entre los retadores
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2
print("Segunda ronda: Los dados suman:", suma, "(", dado1, "y", dado2, ")")
if suma % 2 != 0:
    retador1 = retador1 + max(dado1, dado2)
    retador2 = retador2 - min(dado1, dado2)
else:
    retador2 = retador2 + max(dado1, dado2)
    retador1 = retador1 - min(dado1, dado2)
print("Retador 1:", retador1, "vs Retador 2:", retador2)
# Superaron el record?
if retador1 > campeon or retador2 > campeon:
    superado = True

# Ronda final
if campeon >= retador1 and campeon >= retador2:
    resultado = "El Campeon retiene su titulo"
elif retador1 > retador2:
    resultado = "Retador 1 es el nuevo campeon!"
elif retador2 > retador1:
    resultado = "Retador 2 es el nuevo campeon!"
else:
    resultado = "Retador 1 y Retador 2 empataron!"

if superado == True:
    print('El record fue superado durante el juego')
else:
    print('El record NO fue superado durante el juego')

# Resultado
print('*' * 80)
print('[' * 5, resultado, ']' * 5)
