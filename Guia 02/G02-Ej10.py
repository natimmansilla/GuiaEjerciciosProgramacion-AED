__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y Carga de Datos
print('Calculo de pago de ganancias de peliculas a actores')
print('---------------------------------------------------')

# Carga de Datos  (Entrada)
ganancias = float(input('Ingrese las ganancias totales del palicula: '))
actor = input('Ingrese el nombre del actor: ')
porcentaje = float(input('Ingrese el porcentaje de ganacias que el actor recibira: '))

# Procesos
ganancia_actor = ganancias * porcentaje / 100

# Salidas
print('El Actor', actor, 'recibira un total de $', ganancia_actor, 'por participar de la pelicula')
