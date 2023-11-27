__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

largo = int(input('Ingrese el largo de la parcela: '))
ancho = int(input('Ingrese el ancho de la parcela: '))

superficie = largo * ancho
rinde = (superficie * 2) // 10

print('El rinde que obtiene el productor en', superficie, 'metros cuadrados')
print('es de', rinde, 'quintales')