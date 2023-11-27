__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Importamos random para la simulación de la tirada de dados
import random

# Encabezado de la consola
print('*' * 40)
print('Simulador de tirada del Juego del Punto')
print('*' * 40)

# Solicitamos la carga de los puntos previos
puntos_previos = int(input('\nIngrese sus puntos previos: '))

# Simulamos la tirada de dados e informamos cual fue el valor que salió
d1 = random.randint(1, 6)
print('Dado 1:', d1)

d2 = random.randint(1, 6)
print('Dado 2:', d2)

d3 = random.randint(1, 6)
print('Dado 3:', d3)

# Definimos banderas y acumuladores
duplica = False
puntos = 0

# Primero evaluamos si duplica,
# ya que de ser verdad el resto de la evaluación no hace falta.
if (d1 % 2) == 0 and d1 == d2 and d1 == d3:
    duplica = True
else:
    # Evaluamos los puntos obtenidos para el dado 1
    if d1 == 1:
        puntos += 1
    else:
        if d1 == 3:
            puntos += 2
        else:
            if d1 == 5:
                puntos += 4
    # Evaluamos los puntos obtenidos para el dado 2
    if d2 == 1:
        puntos += 1
    elif d2 == 3:
        puntos += 2
    elif d2 == 5:
        puntos += 4
    # Evaluamos los puntos obtenidos para el dado 3
    if d3 == 1:
        puntos += 1
    elif d3 == 3:
        puntos += 2
    elif d3 == 5:
        puntos += 4

# Mostramos los resultados
puntos_previos += puntos
print('\n Puntos obtenidos en esta tirada:', puntos)
print('\n Puntos totales acumulados:', puntos_previos)

if duplica:
    print('\n Suertudo!!! duplica puntaje')

print('\n\n Fin!')
