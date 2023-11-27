__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Jornal de Operario')
print('=' * 80, '\n')

# Datos
turno = int(input('Ingrese el turnos del operario (1 - Diurno, 2 - Nocturno): '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))

# Proceso
if turno == 1:
    total = horas * 35.5
else:
    total = horas * 40.60

# Resultados
print('La empresa le debe pagar al operario un jornal de $', total)
