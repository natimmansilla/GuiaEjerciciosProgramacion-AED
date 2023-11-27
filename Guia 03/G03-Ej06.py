__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Actualización del sueldo de un empleado')
nombre = input('Ingrese el nombre del empleado: ')
area = input('Ingrese el area funcional en la que trabaja: ')
sueldo = float(input('Ingrese el importe de su sueldo actual: '))

# Procesos
aumento = sueldo * 0.08
descuento = sueldo * 0.025
nuevo_sueldo = sueldo + aumento - descuento

# Presentacion de resultados
print('Nombre empleado:', nombre, '\t\tNuevo sueldo $:', nuevo_sueldo)
print('Area funcional:', area)
print('Sueldo anterior: $', sueldo)