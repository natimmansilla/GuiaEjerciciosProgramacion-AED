__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

TIEMPO_TAXI = 45

# Titulo y carga de datos
print('Determinacion de tiempo de llegada a aeropuerto')
print('Las horas se ingresaran en formato hh:mm (ejemplo: 14:45 o 05:30)')
partida = input('Ingrese la hora de partida en formato hh:mm :')
llegada = input('Ingrese la hora de llegada en formato hh:mm :')

# Procesos

# Sacamos la hora de partida y la convertimos a número entero...
hp = partida[0] + partida[1]
hora_partida = int(hp)

# Ahora los minutos de esa hora, en formato entero...
mp = partida[3] + partida[4]
minutos_partida = int(mp)

# Sacamos la hora llegada y hacemos lo mismo...
hl = llegada[0] + llegada[1]
hora_llegada = int(hl)

# Igual se procede con los minutos...
ml = llegada[3] + llegada[4]
minutos_llegada = int(ml)

# Transformamos hh de la hora de partida a minutos 
# y la acumulamos a los mm de los minutos de partida
minutos_partida = minutos_partida + hora_partida * 60

# Transformamos la hh de la hora de llegada a minutos 
# y la acumulamos a los mm de los minutos de llegada
minutos_llegada = minutos_llegada + hora_llegada * 60

# Duracion del viaje...
duracion_viaje_minutos = minutos_llegada - minutos_partida
hora_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) // 60
minutos_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) % 60

# Presentacion de resultados
print('La duracion del viaje es de:', duracion_viaje_minutos, 'minutos')
print('Llega a las', (str(hora_llegada_hotel) + ':' + str(minutos_llegada_hotel)))