__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Solución realizada en clase al problema Piedra/Papel/Tijera

# import de librerías
import random

# creación de variables internas
elementos = ('PIEDRA', 'PAPEL', 'TIJERA')

# Titulos
print('Piedra, Papel o Tijera - Humano vs. Máquina')
print('*' * 80)

# Ingreso de datos
opcion = int(input('Ingrese (0->PIEDRA, 1->PAPEL o 2->TIJERA): '))
humano = elementos[opcion]
print('\n\nHumano elige', humano)

# Selección de la máquina
maquina = random.choice(elementos)
print('\n\nMáquina elige', maquina)

# Proceso
if humano == maquina:
    resultado = 'Empataron'
else:
    if (maquina == 'PIEDRA' and humano == 'TIJERA') \
            or (maquina == 'PAPEL' and humano == 'PIEDRA') \
            or (maquina == 'TIJERA' and humano == 'PAPEL'):
        resultado = 'Gana MAQUINA'
    else:
        resultado = 'Gana HUMANO'

# Mostrar resultados
print('\n\n¡', resultado, '!')
