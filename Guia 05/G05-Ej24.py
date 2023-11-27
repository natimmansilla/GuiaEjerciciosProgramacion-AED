__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Prueba calculo Podio Triatlón Ironman')
print('=' * 80)

# Entrada
nombre = input('Ingrese el nombre del primer corredor: ')
hora = '0' + str(random.randint(5, 17))
minuto = '0' + str(random.randrange(60))
segundo= '0' + str(random.randrange(60))

tiempo_hora = hora[0] + hora[1]
if len(hora) > 2:
    tiempo_hora = hora[1] + hora[2]

tiempo_min = minuto[0] + minuto[1]
if len(minuto) > 2:
    tiempo_min = minuto[1] + minuto[2]

tiempo_seg = segundo[0] + segundo[1]
if len(tiempo_seg) > 2:
    tiempo_seg = segundo[1] + segundo[2]

corredor_1 = nombre, tiempo_hora + ':' + tiempo_min + ':' + tiempo_seg

nombre = input('Ingrese el nombre del segundo corredor: ')
hora = '0' + str(random.randint(5, 17))
minuto = '0' + str(random.randrange(60))
segundo= '0' + str(random.randrange(60))

tiempo_hora = hora[0] + hora[1]
if len(hora) > 2:
    tiempo_hora = hora[1] + hora[2]

tiempo_min = minuto[0] + minuto[1]
if len(minuto) > 2:
    tiempo_min = minuto[1] + minuto[2]

tiempo_seg = segundo[0] + segundo[1]
if len(tiempo_seg) > 2:
    tiempo_seg = segundo[1] + segundo[2]

corredor_2 = nombre, tiempo_hora + ':' + tiempo_min + ':' + tiempo_seg

nombre = input('Ingrese el nombre del tercer corredor: ')
hora = '0' + str(random.randint(5, 17))
minuto = '0' + str(random.randrange(60))
segundo= '0' + str(random.randrange(60))

tiempo_hora = hora[0] + hora[1]
if len(hora) > 2:
    tiempo_hora = hora[1] + hora[2]

tiempo_min = minuto[0] + minuto[1]
if len(minuto) > 2:
    tiempo_min = minuto[1] + minuto[2]

tiempo_seg = segundo[0] + segundo[1]
if len(tiempo_seg) > 2:
    tiempo_seg = segundo[1] + segundo[2]

corredor_3 = nombre, tiempo_hora + ':' + tiempo_min + ':' + tiempo_seg

tiempo = corredor_1[1]
tpo_segundos_corr1 = int(tiempo[0] + tiempo[1]) * 3600 + int(tiempo[3] + tiempo[4]) * 60 + int(tiempo[6] + tiempo[7])

tiempo = corredor_2[1]
tpo_segundos_corr2 = int(tiempo[0] + tiempo[1]) * 3600 + int(tiempo[3] + tiempo[4]) * 60 + int(tiempo[6] + tiempo[7])

tiempo = corredor_3[1]
tpo_segundos_corr3 = int(tiempo[0] + tiempo[1]) * 3600 + int(tiempo[3] + tiempo[4]) * 60 + int(tiempo[6] + tiempo[7])

# Tiempo promedio
total = tpo_segundos_corr1 + tpo_segundos_corr2 + tpo_segundos_corr3
promedio = total // 3
horas = divmod(promedio, 3600)
minutos = divmod(horas[1], 60)

# Podio (el menor tiempo gana, ordenar tres tiempos
if tpo_segundos_corr1 < tpo_segundos_corr2 and tpo_segundos_corr1 < tpo_segundos_corr3:
    medalla_oro = corredor_1[0]
    if tpo_segundos_corr2 < tpo_segundos_corr3:
        medalla_plata = corredor_2[0]
        medalla_bronce = corredor_3[0]
    else:
        medalla_plata = corredor_3[0]
        medalla_bronce = corredor_2[0]
elif tpo_segundos_corr2 < tpo_segundos_corr3:
    medalla_oro = corredor_2[0]
    if tpo_segundos_corr1 < tpo_segundos_corr3:
        medalla_plata = corredor_1[0]
        medalla_bronce = corredor_3[0]
    else:
        medalla_plata = corredor_3[0]
        medalla_bronce = corredor_1[0]
else:
    medalla_oro = corredor_3[0]
    if tpo_segundos_corr1 < tpo_segundos_corr2:
        medalla_plata = corredor_1[0]
        medalla_bronce = corredor_2[0]
    else:
        medalla_plata = corredor_2[0]
        medalla_bronce = corredor_1[0]

# Salidas

print('El tiempo promedio de la prueba fue:', str(horas[0]) + ':' + str(minutos[0]) + ':' + str(minutos[1]))
print('El podio de la competencia fue: ')
print('\t- Medalla de Oro:', medalla_oro)
print('\t- Medalla de Plata:', medalla_plata)
print('\t- Medalla de Bronce:', medalla_bronce)

if tpo_segundos_corr1 > promedio:
    print('El tiempo del ganador de la prueba fue superior al promedio')