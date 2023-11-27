__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Visualización de un importe en forma de cadena')
importe = float(input('Ingrese un importe: '))

# Procesos
r1 = '$' + str(importe)
r2 = 'pesos ' + str(importe)
 
# Presentacion de resultados
print('Importe en formato 1:', r1)
print('Importe en formato 2:', r2)