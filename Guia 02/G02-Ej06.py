__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Precios de venta')
lista = (int(input('Ingrese precio de lista del artículo: ')))

# Procesos
contado = lista - lista * 10/100
tarjeta = lista + lista * 5/100

# Presentacion de resultados
print ("Precio contado $:", contado)
print ("Precio con tarjeta $:", tarjeta)