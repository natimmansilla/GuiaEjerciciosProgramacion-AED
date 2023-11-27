__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

# Fijar la semilla según indica el enunciado
random.seed(20220512)

# Acumulador de TODOS los números generados, como elemento de control...
st = 0

contador_mul_3 = contador_mul_5 = contador_no_mul = 0
suma_pares_mult = contador_pares_mult = 0

# Para la alternativa de búsqueda del mayor con bandera
bandera_primer_caso = True

n = 25000
for i in range(n):
    num = random.randint(1, 45000)
    st += num

    if num % 3 == 0:
        contador_mul_3 += 1
    else:
        if num % 5 == 0:
            contador_mul_5 += 1
        else:
            contador_no_mul += 1

    cadena_numero = str(num)
    primer_digito = cadena_numero[0]
    if primer_digito == '1':
        if bandera_primer_caso:
            mayor = num
            bandera_primer_caso = False
        else:
            if num > mayor:
                mayor = num

    if num % 2 == 0 and num % 11 == 0:
        suma_pares_mult += num
        contador_pares_mult += 1

porc_mul_3 = int(contador_mul_3 * 100 / n)
porc_mul_5 = int(contador_mul_5 * 100 / n)
porc_no_mul = int(contador_no_mul * 100 / n)

if contador_pares_mult > 0:
    promedio = suma_pares_mult // contador_pares_mult
else:
    promedio = 0

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Resultados pedidos por el enunciado:')
print('Cantidad de números múltiplos de 3:', contador_mul_3)
print('Cantidad de números múltiplos de 5 y no de 3:', contador_mul_5)
print('Cantidad restante de números:', contador_no_mul)
print('Número Mayor: ', mayor)
print('Promedio de pares múltiplos de 11:', promedio)
print('Porcentaje de números múltiplos de 3:', porc_mul_3)
print('Porcentaje de números múltiplos de 5 y no de 3:', porc_mul_5)
print('Porcentaje restante de números:', porc_no_mul)
