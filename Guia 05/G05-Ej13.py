__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Calculo del cuadrante de un punto')
print('*' * 80)

# Ingreso de datos
x = int(input('Ingrese la coordenada x del punto: '))
y = int(input('Ingrese la coordenada y del punto: '))

# Procesos
if x == 0 or y == 0:
    cuadrante = 'alguno de los ejes o el origen'
elif x > 0 and y > 0:
    cuadrante = 'Primer Cuadrante'
elif x > 0 and y < 0:
    cuadrante = 'Cuarto Cuadrante'
elif x < 0 and y > 0:
    cuadrante = 'Segundo Cuadrante'
elif x < 0 and y < 0:
    cuadrante = 'Tercer Cuadrante'

# Salida
print('El punto (',x,",",y,') se encuentra ubicado en:', cuadrante)