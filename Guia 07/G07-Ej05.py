__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

n = int(input("Ingrese la cantidad de nros. a procesar: "))
contador_positivos = 0
suma_positivos = 0
mayor_negativos = 0

for i in range(n):

    # Entrada
    print("Ingrese el número ", i + 1)
    numero = int(input())

    # Subproblema 1: Búsqueda del segundo menor
    if i == 0:
        menor = numero
    elif i == 1:
        if numero < menor:
            segundoMenor = menor
            menor = numero
        else:
            segundoMenor = numero
    else:
        if numero < menor:
            segundoMenor = menor
            menor = numero
        elif numero < segundoMenor:
            segundoMenor = numero

    # Subproblema 2: El promedio de los numeros positivos
    if numero >= 0:
        contador_positivos += 1
        suma_positivos += numero

    # Subproblema 3: El mayor de los numeros negativos.
    else:
        if mayor_negativos == 0:
            mayor_negativos = numero
        elif mayor_negativos < numero:
            mayor_negativos = numero

if contador_positivos != 0:
    promedio = suma_positivos / contador_positivos
else:
    promedio = 0

# Salida
print("El segundo menor es:", segundoMenor)
print("El promedio de numeros positivos es: ", promedio)
print("El mayor de los numeros negativos es: ", mayor_negativos)
