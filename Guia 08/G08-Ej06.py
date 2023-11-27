__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print("Nuestro primer programa controlado por menú")

opc = 0
while opc != 4:  # mientras la opción sea distinta de salir
    print("\nMenú de opciones")
    print("1-Promedio")
    print("2-Contar positivos y negativos")
    print("3-Nota alumno")
    print("4-Salir")
    opc = int(input("\nIngrese su opción: "))
    if opc == 1:
        suma = cant = 0
        num = int(input("Ingrese un número (finaliza con -1): "))
        while num != -1:
            suma += num
            cant += 1
            num = int(input("Ingrese un número (Finaliza con -1): "))
        if cant != 0:
            prom = suma / cant
        else:
            prom = 0
        print("Promedio de los valores:", round(prom, 2))
        input("Presione enter para continuar")

    elif opc == 2:
        n = int(input("Ingrese la cantidad de números a generar: "))
        positivos = negativos = 0
        for i in range(n):
            num = random.randint(-100, 100)
            if num >= 0:
                positivos += 1
            else:
                negativos += 1
        print("Cantidad de positivos:", positivos)
        print("Cantidad de negativos:", negativos)
        input("Presione enter para continuar")

    elif opc == 3:
        nota = -1
        while nota < 0 or nota > 10:  # nota incorrecta
            nota = int(input("Ingrese una nota: "))
            if nota < 0 or nota > 10:
                print("Nota incorrecta!!")
        if nota >= 4:
            print("Está aprobado")
        else:
            print("No está aprobado")
        input("Presione enter para continuar")

    elif opc == 4:
        print("Adiós!!")
    else:
        print("Opción incorrecta!")
