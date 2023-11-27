__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print("Secuencia de numeros")
print("=" * 80)

cn = suma_multiplos_6 = cant_multiplos_6 = multiplos_anterior = 0
secuencia_ascendente = cantidad_secuencias = 0
es_ascendente = False
num_anterior = 0
numero = int(input("Ingrese un numero (la carga finaliza cuando ingrese 0): "))
while numero != 0:

    cn += 1
    if numero % 6 == 0:
        suma_multiplos_6 += numero
        cant_multiplos_6 += 1

    if cn > 1:
        if num_anterior % numero == 0:
            multiplos_anterior += 1

        if num_anterior % 2 != 0 and numero % 2 != 0 and numero > num_anterior:
            secuencia_ascendente += 1
        else:
            if secuencia_ascendente >= 2:
                cantidad_secuencias += 1
            secuencia_ascendente = 0

    num_anterior = numero
    numero = int(input("Ingrese otro numero: "))

print('Hay', cant_multiplos_6, 'numeros en la secuencia que son multiplos de 6')
print('Hay', cantidad_secuencias, 'secuencias ascendentes de numeros impares '
                                  'en la secuencia de numeros')
print('Hay', multiplos_anterior, 'numeros que son divisor exacto del numero '
                                 'anterior')
