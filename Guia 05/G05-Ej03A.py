__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Mantenimiento informatico')
print('='* 80)

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo1 = numero_pc, tiempo_reparacion, causa

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo2 = numero_pc, tiempo_reparacion, causa

numero_pc = int(input('Ingrese numero de identificacion de la pc: '))
tiempo_reparacion = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa = int(input('Ingrese la causa del mantemiento (1 - Hardware, 2 - Software'))
equipo3 = numero_pc, tiempo_reparacion, causa

# procesos

total_mant = equipo1[1] + equipo2[1] + equipo3[1]
prom_mant = total_mant / 3

if equipo1[1] > equipo2[1] and equipo1[1] > equipo3[1]:
    mayor = equipo1
else:
    if equipo2[1] > equipo3[1]:
        mayor = equipo2
    else:
        mayor = equipo3

mant_por_hardware = False
if equipo1[2] == 1 and equipo2[2] == 1 and equipo3[2] == 1:
    mant_por_hardware = True

# Salidas
print('El tiempo total de reparacion de las tres PC fue de', total_mant,'minutos')
print('La PC con mayor tiempo de reparacion fue la numero', mayor[0])
print('El tiempo promedio de reparacion fue de', prom_mant, 'minutos')

if mant_por_hardware:
    print('Todas las PC recibiron mantenimiento por problemas de harware')
else:
    print('Las PC recibieron distintos tipos de mantenimiento')