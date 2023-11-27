# Sumador ángulos
# RESOLUCION CON VARIABLES

# Entrada ángulo 1 como g ' "
# Entrada ángulo 2 como g ' "
# Salida Final
#   Ángulo suma como g ' "

print('*' * 30)
print('   Sumador de Ángulos')
print('*' * 30)

print('Ingrese el primer ángulo:')
grados_a1 =   int(input('\tGrados:   '))
minutos_a1 =  int(input('\tMinutos:  '))
segundos_a1 = int(input('\tSegundos: '))

print('Ingrese el segundo ángulo:')
grados_a2 =   int(input('\tGrados:   '))
minutos_a2 =  int(input('\tMinutos:  '))
segundos_a2 = int(input('\tSegundos: '))

print()

seg_totales_a1 = segundos_a1 + minutos_a1 * 60 + \
                  grados_a1 * 60**2
seg_totales_a2 = segundos_a2 + minutos_a2 * 60 + grados_a2 * 60**2
# print("Segundos totales ángulo 1:", seg_totales_a1)
# print("Segundos totales ángulo 2:", seg_totales_a2)

seg_totales_suma = seg_totales_a1 + seg_totales_a2
# print("Suma total en segundos:", seg_totales_suma)

print()

grados_suma = seg_totales_suma // 60**2
segundos_restantes = seg_totales_suma % 60**2
minutos_suma = segundos_restantes // 60
segundos_suma = segundos_restantes % 60

print('*   Resultados')
#print('* El ángulo resultante: ','\n*\t', grados_suma, 'g ', minutos_suma, '\' ', segundos_suma, '"')
print('* El ángulo resultante: ', \
        '\n*\t', grados_suma, 'g ', \
        minutos_suma, '\' ', \
        segundos_suma, '"')
print('*' * 30)
print()
print('Fin.')
print()
input("Presione Enter para finalizar...")