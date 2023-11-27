__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Datos
cant_arrobas = 0
pos_arroba = -1
dos_puntos = False
anterior = None
print('INICIO DE SESIÓN')
cuenta = input('Ingrese cuenta: ')

# Proceso
pos = 0
for car in cuenta:
    if car == '@':
        cant_arrobas += 1
        pos_arroba = pos
    elif car == '.' and anterior == '.':
        dos_puntos = True
    pos += 1
    anterior = car

# Resultados
if cant_arrobas != 1 or pos_arroba == 0 or pos_arroba == len(cuenta) - 1:
    print('Error! La cantidad y/o ubicacion de @ es incorrecta.')
elif dos_puntos:
    print('Error! La cuenta tiene dos puntos seguidos.')
elif cuenta[0] == '.' or cuenta[-1] == '.':
    print('Error! La cuenta empieza o termina con punto.')
else:
    print('Cuenta válida. Ingreso autorizado')
