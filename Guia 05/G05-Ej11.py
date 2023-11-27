__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Cargar los datos
modelo = int(input("Ingrese año de fabricación: "))
tipo = input("Ingrese tipo (P/T/R): ")
antig = 2020 - modelo

# Determinar impuestos
if tipo == "P" or tipo == "T":
    if antig < 10:
        impuestos = 200
    elif antig > 20:
        impuestos = 150
    else:
        impuestos = 0
    if tipo == "T":
        impuestos = impuestos + 150
else:
    impuestos = 100 * antig

print("El vehículo debe abonar $ ", impuestos)
