__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Entrada de datos
p1_formula = input("Ingrese fórmula del partido 1: ")
p1_cant = int(input("Ingrese cantidad de votos partido 1: "))
p2_formula = input("Ingrese fórmula del partido 2: ")
p2_cant = int(input("Ingrese cantidad de votos partido 2: "))
p3_formula = input("Ingrese fórmula del partido 3: ")
p3_cant = int(input("Ingrese cantidad de votos partido 3: "))

# Proceso
total_votos = p1_cant + p2_cant + p3_cant
porc1 = p1_cant * 100 / total_votos
porc2 = p2_cant * 100 / total_votos
porc3 = p3_cant * 100 / total_votos

if porc1 > porc2:
    if porc2 > porc3:
        primero = porc1
        f1 = p1_formula
        segundo= porc2
        f2 = p2_formula
        tercero = porc3
        f3 = p3_formula
    else:
        tercero = porc2
        f3 = p2_formula
        if porc1 > porc3:
            primero = porc1
            f1 = p1_formula
            segundo= porc3
            f2 = p3_formula
        else:
            primero = porc3
            f1 = p3_formula
            segundo= porc1
            f2 = p1_formula
else:
    if porc1 > porc3:
        primero = porc2
        f1 = p2_formula
        segundo= porc1
        f2 = p1_formula
        tercero = porc3
        f3 = p3_formula
    else:
        tercero = porc1
        f3 = p1_formula
        if porc2 > porc3:
            primero = porc2
            f1 = p2_formula
            segundo= porc3
            f2 = p3_formula
        else:
            primero = porc3
            f1 = p3_formula
            segundo= porc2
            f2 = p2_formula

flag = False
if primero >= 45 or primero >= 40 and (primero-segundo) > 10:
    flag = True

# Salida
print("Fórmula con mayor porcentaje:", f1)

if flag == True:
    print("La fórmula resultó elegida, no hay segunda vuelta.")
else:
    print("Hay segunda vuelta. Los participantes son:")
    print("Primer puesto: ", f1)
    print("Segundo puesto: ", f2)