__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Secuencia de numeros')
print('=' * 80)

cn = cnd3 = cnca = mayor = pos = 0
primero = True
numero = int(input('Ingrese el primer numero de la serie (Con cero finaliza): '))
while numero != 0:
    cn += 1
    if numero % 3 == 0:
        cnd3 += 1

    # Aqui se puede reemplazar de las siguientes maneras haciendo al inicio import math
    # if cn > 1 and int(math.sqrt(numero)) == numero_anterior:
    # if cn > 1 and numero == numero_anterior ** 2:
    if cn > 1 and int(numero ** 0.5) == numero_anterior:
        cnca += 1

    if numero % 2 != 0:
        if primero:
            mayor = numero
            pos = 1
            primero = False
        else:
            if numero > mayor:
                mayor = numero
                pos = cn

    numero_anterior = numero
    numero = int(input('Ingrese otro numero de la secuencia: '))

print('_' * 80)
print('Presentacion de resultados')

if cn != 0:
    por = cnd3 * 100 / cn
    print('Hay', cnd3, 'numeros divisibles por 3 en la secuencia y representan el', round(por, 2),
          '% del total de numeros')
    print('La cantidad de numeros que son el cuadrado del anterior son', cnca)
    print('El mayor numero impar es', mayor, 'y se encuentra en la posicion', pos)
else:
    print('No hay numero procesados')
