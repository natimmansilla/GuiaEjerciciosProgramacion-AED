__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

cant_venta = 0
tot_venta = 0
cant_venta1 = 0
cont_venta400 = 0
cont_venta500 = 0
cont_venta600 = 0
hay_menor_50 = False

venta = int(input('Ingrese una cantidad de ventas (negativo para terminar): '))
while venta >= 0:
    # Permite ir contabilizando la cantidad de ventas
    cant_venta += 1
    # Permite acumular el total de ventas.
    tot_venta += venta

    # Permite contabilizar la cantidad de ventas entre 200 y 300 unidades.
    if (venta >= 100 and venta <= 300):
        cant_venta1 += 1
    # Permite contabilizar la cantidad de ventas con 400, 500 y 600 unidades.
    if venta == 400:
        cont_venta400 += 1
    if venta == 500:
        cont_venta500 += 1
    if venta == 600:
        cont_venta600 += 1

    # Determina si hubo una venta inferior a 50 unidades.
    if venta < 50:
        hay_menor_50 = True

    venta = int(
        input('Ingrese otra cantidad de ventas (0 cero para terminar): '))

print('La cantidad de ventas ingresadas fueron: ', cant_venta)
print('El total de ventas ingresadas fue:', tot_venta)
print('La cantidad de ventas comprendidas entre 200 y 300 unidades es:', cant_venta1)
print('La cantidad de ventas con 400 unidades es:', cont_venta400)
print('La cantidad de ventas con 500 unidades es:', cont_venta500)
print('La cantidad de ventas con 600 unidades es:', cont_venta600)

if hay_menor_50 == True:
    print('Hubo al menos alguna venta con menos de 50 unidades')
else:
    print('No hubo venta con menos de 50 unidades')
