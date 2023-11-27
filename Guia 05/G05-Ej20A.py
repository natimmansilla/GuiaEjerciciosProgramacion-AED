__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print('PREMIO POR VENTAS DEL TRIMESTRE')

# Ingreso de datos
monto1 = int(input('Ingrese monto mes 1: '))
monto2 = int(input('Ingrese monto mes 2: '))
monto3 = int(input('Ingrese monto mes 3: '))

# Buscar menor monto
if monto1 < monto2 and monto1 < monto3:
    menor = monto1
elif monto2 < monto3:
    menor = monto2
else:
    menor = monto3

# Calcular premio
premio = menor * 50 / 100

# Calcular adicional
if monto1 > 1000 and monto2 > 1000 and monto3 > 1000:
    adicional = premio * 10 / 100
else:
    adicional = 0
premio += adicional

# Resultados
print('\nEl premio es de $', premio)
if adicional > 0:
    print('(Incluye adicional de $', adicional, 'por ventas altas)')
