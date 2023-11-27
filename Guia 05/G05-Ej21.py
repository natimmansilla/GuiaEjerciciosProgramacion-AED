__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print("Análisis Estadístico")

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

multiplo_5 = False
if num1 % 5 == 0 or num2 % 5 == 0 or num3 % 5 == 0:
    multiplo_5 = True

todos_impares = False
if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
    todos_impares = True

if num1 > num2 and num1 > num3:
    may = num1
    # otro1 = num2
    # otro2 = num3
    suma = num2 + num3
else:
    if num2 > num3:
        may = num2
        # otro1 = num1
        # otro2 = num3
        suma = num1 + num3
    else:
        may = num3
        # otro1 = num1
        # otro2 = num2
        suma = num1 + num2

supera_suma = False
# suma = otro1 + otro2
if may > suma:
    supera_suma = True

if multiplo_5:
    print("Al menos uno de los valores es múltiplo de 5")
else:
    print("Ningún valor es múltiplo de 5")

if todos_impares:
    print("Todos los valores son impares")
else:
    print("No todos los valores son impares")

if supera_suma:
    print("El mayor de los valores supera la suma de los otros dos")
else:
    print("El mayor de los valores no supera la suma de los otros dos")
