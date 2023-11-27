__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Pago a proveedores')
print('=' * 80)

print('\nCarga de Datos del Proveedor')
categoria = input('Ingrese la categoria del proveedor (A o B): ')
importe = float(input('Ingrese el importe que se le debe pagar al proveedor: '))

# Proceso

if categoria == 'A' and importe > 1000:
    total = importe - importe * 0.05
elif categoria == 'B' and 1500 <= importe <= 2500:
    total = importe - importe * 0.02
else:
    total = importe

# Salidas
print("El importe total al proveedor es de $", total)