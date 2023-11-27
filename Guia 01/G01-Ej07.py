__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Constantes
ADICIONAL_KM = 0.30

# Titulo y carga de datos
print('Costo del boleto de un viaje')
costo_base = float(input('Ingrese el costo base del boleto: '))
kilometros = int(input('Ingrese los kilometros a recorrer: '))

# Procesos
adicional = kilometros * ADICIONAL_KM
costo_total = costo_base + adicional

# Presentacion de resultados
print('El costo del viaje es', costo_total)
