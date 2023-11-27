__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Proceso de discriminantes de polinomios de segundo grado')
print('=' * 75)

cant_2raices = 0
cant_1raiz = 0
cant_raices_complejas = 0

sigue = input('Dese procesar un discriminante (S/N): ')
while sigue == 'S':
    delta = int(input('Ingrese el discriminante a procesar: '))
    if delta > 0:
        cant_2raices += 1
    elif delta == 0:
        cant_1raiz += 1
    else:
        cant_raices_complejas += 1

    sigue = input('Desea continuar procesando otro discriminante (S/N): ')

total = cant_2raices + cant_1raiz + cant_raices_complejas

print('La cantidad de discriminantes con que se obtendran 2 raices son:', cant_2raices)
print('La cantidad de discriminantes con que se obtendra 1 raiz son:', cant_1raiz)
print('La cantidad de discriminantes con que se obtendran raices imaginarias son:',
      cant_raices_complejas)
if total > 0:
    porc = cant_raices_complejas * 100 / total
    print('El porcentaje de discriminantes que obtienen raices complejas es: ',
          round(porc, 2), '%', sep='')
