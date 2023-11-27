__author__ = 'Algoritmos y Estructuras de Datos'

print('Calculo de Precio de Venta')
print('=' * 60)

precio_unitario = float(input('Ingrese el precio unitario del articulo: '))
cantidad = int(input('Ingrese la cantidad que se vendio del producto: '))
es_efectivo = input('La venta del articulo, se abono en efectivo? (Responda S o N): ')

print('...Procesando')
precio = precio_unitario * cantidad

if es_efectivo == 'S' and cantidad > 10:
    descuento = precio * 0.15
else:
    descuento = (precio * 0.05)

precio_final = precio - descuento

print('\nSalidas')
print('-' * 60, '\n')
print('El Precio Final que se cobro del articulo fue de $', round(precio_final, 2))
print('se le aplico un ', descuento, '% de descuento a la operacion')
