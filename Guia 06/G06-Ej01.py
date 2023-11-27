__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('COMPLEJO DE CINES')
print('*' * 80)

# Inicializar contadores y acumuladores
monto = 0
funciones = 0
funciones_dto = 0

# Primera carga de datos de corte antes del ciclo
espectadores = int(input('Espectadores (con 0 termina): '))

# Proceso repetitivo
while espectadores != 0:
    # Carga de datos que no determinan el corte del ciclo
    descuento = input('Descuento (S/N): ')
    # Definir precio
    if descuento == 'S':
        precio = 50
    else:
        precio = 75
    # Acumular monto recaudado por función
    monto = monto + (espectadores * precio)
    # Contar funciones con descuento y total de funciones
    if descuento == 'S':
        funciones_dto += 1
    funciones += 1
    # Nueva carga de datos de corte dentro del ciclo
    espectadores = int(input('Espectadores (con 0 termina): '))

# Resultados
print('*'*80)
print('Recaudación total $', monto)
if funciones != 0:
    porc = funciones_dto * 100 / funciones
else:
    porc = 0
print('Porcentaje de funciones con descuento:', porc, '%')
