__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Conversion de metros a kilimetros de viaje recorridos')
print('=' * 80)
print('\n')

distancia = 3641.3 * 1000
x = int(input('Ingrese la cantidad de metros recorridos: '))

km = x // 1000
mts = x % 1000

porc = (x * 100) / distancia

print('El viajero recorrio ', km , ' kilometros con ', mts, ' metros')
print('Siginifica que el viajero recorrio solo un ', porc, '% del total del viaje')