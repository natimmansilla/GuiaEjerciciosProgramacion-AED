__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Mantenimiento informatico')
print('='* 80)

#Datos
numero1 = int(input('Ingrese numero de identificacion de la primera PC: '))
tiempo1 = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa1 = int(input('Ingrese la causa del mantemiento (1=Hardware / 2=Software): '))

numero2 = int(input('Ingrese numero de identificacion de la segunda PC: '))
tiempo2 = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa2 = int(input('Ingrese la causa del mantemiento (1=Hardware / 2=Software): '))

numero3 = int(input('Ingrese numero de identificacion de la tercera PC: '))
tiempo3 = int(input('Ingrese el tiempo en minutos de reparacion: '))
causa3 = int(input('Ingrese la causa del mantemiento (1=Hardware / 2=Software): '))

#Proceso
tiempo_total = tiempo1 + tiempo2 + tiempo3


if tiempo1 > tiempo2 and tiempo1 > tiempo3:
    mayor = numero1,tiempo1
else:
    if tiempo2 > tiempo3:
        mayor = numero2, tiempo2
    else:
        mayor = numero3, tiempo3

promedio = round(tiempo_total / 3,2)

if causa1 == 1 and causa2 == 1 and causa3 == 1:
    todos_hardare = True
else:
    todos_hardare = False

# Salidas
print()
print('El tiempo total de reparacion de las tres PC fue de', tiempo_total,'minutos')
print('La PC con mayor tiempo de reparacion fue la numero', mayor[0],'con',mayor[1],'minutos')
print('El tiempo promedio de reparacion fue de', promedio, 'minutos')

if todos_hardare:
    print('Todas las PC recibiron mantenimiento por problemas de hardware')
else:
    print('Las PC recibieron distintos tipos de mantenimiento')