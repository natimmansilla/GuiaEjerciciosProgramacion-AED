__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


print('Calculo de Costos')
print('*' * 80)

presupuesto = float(input('Ingrese el monto total presupuestado: '))

ganancia = presupuesto * 0.17
costos = presupuesto - ganancia

print('Los costos del proyecto no deben exceder los $', costos)