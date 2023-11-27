__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Sistema de Calculo de Comisiones a Vendedores')
print('*' * 80)

tot_cat_1 = 0
tot_cat_2 = 0
tot_cat_3 = 0
tot_cat_4 = 0

print('Inicio de calculo de comision, al entrar una categoria igual a 0 el proceso termina')
categoria = int(input('Ingrese la categoria de vendedor (1-4): '))

while categoria != 0:
    venta = float(input('Ingrese el total vendido por este vendedor: '))

    if categoria == 1:
        tot_cat_1 += venta * 0.10
    elif categoria == 2:
        tot_cat_2 += venta * 0.25
    elif categoria == 3:
        tot_cat_3 += venta * 0.30
    else:
        tot_cat_4 += venta * 0.40

    categoria = int(input('Ingrese una nueva categoria de vendedor (1-4): '))

total = tot_cat_1 + tot_cat_2 + tot_cat_3 + tot_cat_4

print('Resultados de comisiones calculadas')
print('*' * 80)
print('El total de comisiones a pagar para la categoria 1 es de $', tot_cat_1, sep='')
print('El total de comisiones a pagar para la categoria 2 es de $', tot_cat_2, sep='')
print('El total de comisiones a pagar para la categoria 3 es de $', tot_cat_3, sep='')
print('El total de comisiones a pagar para la categoria 4 es de $', tot_cat_4, sep='')
print('El total de comisiones a pagar es de $', total, sep='')
