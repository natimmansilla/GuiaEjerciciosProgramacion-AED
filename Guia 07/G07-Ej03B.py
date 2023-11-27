__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('SUELDOS Y AGUINALDO')
print('*' * 80)

# Datos y proceso
total = 0
for mes in range(1, 7):
    sueldo = float(input("Ingrese sueldo mes " + str(mes) + ": "))
    if mes == 1:
        may = sueldo
        men = sueldo, 1
    else:
        if sueldo > may:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo, mes
    total += sueldo

# Resultados
aguinaldo = may / 2
print("\nEl aguinaldo es de $", aguinaldo)
print("El menor sueldo fue de $", men[0], "y lo obtuvo en el mes", men[1])
promedio = round(total / 6, 2)
print("El sueldo promedio es de $", promedio)
