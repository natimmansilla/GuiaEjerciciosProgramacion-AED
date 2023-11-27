__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Secuencia de numeros')
print('=' * 80)

cn5 = cn = cprimero = cma = primer_numero = numero_anterior = 0
numero = int(input('Ingrese el primer numero de la serie (finaliza con 0): '))
while numero != 0:
    cn += 1
    if cn == 1:
        primer_numero = numero
    else:
        if numero == primer_numero:
            cprimero += 1

        if numero > numero_anterior:
            cma += 1

    if numero % 10 == 5:
        cn5 += 1

    numero_anterior = numero
    numero = int(input('Ingrese otro numero de la secuencia: '))

print('_' * 80)
print('Presentacion de resultados')
print('Hay', cn5, 'numeros que terminan con cinco')
print('Aparece', cprimero, 'veces el primer numero de la secuencia')
print('Hay', cma, 'numeros que son mayores al anterior')
