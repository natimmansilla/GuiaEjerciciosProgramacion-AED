__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Busqueda del mayor par de orden par')
print('=' * 80)

orden = 0
mayor = None

numero = int(input('Ingrese un numero (finaliza cuando ingrese 0): '))

while numero != 0:
    # Si es número par en orden par,
    if orden % 2 == 0 and numero % 2 == 0:
        # se busca el mayor
        if mayor is None or numero > mayor:
            mayor = numero
    orden += 1
    numero = int(input('Ingrese otro numero: '))

if not mayor is None:
    print('El mayor numero par ingresado en orden par es', mayor)
else:
    print('No se ingresaron números pares en orden par')
