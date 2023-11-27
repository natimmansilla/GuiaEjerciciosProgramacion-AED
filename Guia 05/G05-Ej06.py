__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Administracion cupos grados de escuela')
print('=' * 80)

# entrada de datos
cupo = int(input('Ingrese el cupo de alumnos maximo a considerar: '))

identificacion = input('Ingrese la identificacion del grado: ')
ninos = int(input('Ingrese la cantidad de niños inscriptos al grado: '))
ninas = int(input('Ingrese la cantidad de niñas inscriptos al grado: '))
grado1 = identificacion, ninos, ninas,cupo, (ninos + ninas)

identificacion = input('Ingrese la identificacion de otro grado: ')
ninos = int(input('Ingrese la cantidad de niños inscriptos al grado: '))
ninas = int(input('Ingrese la cantidad de niñas inscriptos al grado: '))
grado2 = identificacion, ninos, ninas,cupo, (ninos + ninas)

identificacion = input('Ingrese la identificacion del ultimo grado: ')
ninos = int(input('Ingrese la cantidad de niños inscriptos al grado: '))
ninas = int(input('Ingrese la cantidad de niñas inscriptos al grado: '))
grado3 = identificacion, ninos, ninas,cupo, (ninos + ninas)

# procesos

if grado1[4] < grado2[4] and grado1[4] < grado3[4]:
    menor = grado1
else:
    if grado2[4] < grado3[4]:
        menor = grado2
    else:
        menor = grado3

porc_fem_grado1 = grado1[2] * 100 / grado1[4]
porc_fem_grado2 = grado2[2] * 100 / grado2[4]
porc_fem_grado3 = grado3[2] * 100 / grado3[4]

porc_masc_grado1 = grado1[1] * 100 / grado1[4]
porc_masc_grado2 = grado2[1] * 100 / grado2[4]
porc_masc_grado3 = grado3[1] * 100 / grado3[4]

promedio = (grado1[4] + grado2[4] + grado3[4]) // 4

supera = False
if grado1[4] > grado1[3] or grado2[4] > grado2[3] or grado3[4] > grado3[3]:
    supera = True

# salida
print('El grado con menor cantidad de inscriptos es', menor[0])
print('Hay un ', porc_fem_grado1, '% de niñas inscriptas en un grado')
print('Hay un ', porc_fem_grado2, '% de niñas inscriptas en otro grado')
print('Hay un ', porc_fem_grado3, '% de niñas inscriptas en el ultimo grado')
print('Hay un ', porc_masc_grado1, '% de niños inscriptas en un grado')
print('Hay un ', porc_masc_grado2, '% de niños inscriptas en otro grado')
print('Hay un ', porc_masc_grado3, '% de niños inscriptas en el ultimo grado')

print('El promedio general de alumnos inscriptos fue de ', promedio, 'alumnos')
if supera:
    print('Algun grado desbordo el cupo maximo permitido, debe abrirse otra division')