__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


print('CARRERA DE CICLISTAS')
print('-' * 40)
cont = acum = 0
ganador = None

n = int(input('Ingrese la cantidad de ciclistas que participan de la carrera: '))

for i in range(n):
    print('Ciclista', i)
    nombre = input('Ingrese nombre: ')
    tiempo = int(input('Ingrese tiempo: '))
    if ganador is None or tiempo < ganador[1]:
        ganador = nombre, tiempo
    cont += 1
    acum += tiempo

print('-' * 40)
if n > 0:
    record = int(input('Ingrese record actual: '))
    print('El ganador es', ganador[0])
    if ganador[1] < record:
        print('El ganador supero el record!')
    if cont > 0:
        promedio = round(acum / cont, 2)
    else:
        promedio = 0
    print('Tiempo promedio general', promedio)
else:
    print('No se ingresaron datos')
