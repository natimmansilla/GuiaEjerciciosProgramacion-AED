__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Calculo presupuestario en un hospital')
presupuesto = float(input('Ingrese monto del presupuesto total: '))

# Procesos
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

# Presentacion de resultados
print('Monto asignado a Urgencias:', urgencias)
print('Monto asignado a Pediatria:', pediatria)
print('Monto asignado a Traumatologia:', traumatologia)