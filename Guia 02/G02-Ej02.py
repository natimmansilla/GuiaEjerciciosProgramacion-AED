__author__ = 'Algoritmos y Estructuras de Datos'


# Titulo y carga de datos
print('Calculo de descuento en un medicamento')
precio_actual = float(input('Ingrese el precio actual: '))

# Procesos
# Calculo del descuento...
descuento = precio_actual * 0.35

# Calculo del nuevo precio...
precio_nuevo = precio_actual - descuento

# Visualización de resultados
print('Precio original:', precio_actual)
print('Descuento del 35%:', descuento)
print('Nuevo precio:', precio_nuevo)
