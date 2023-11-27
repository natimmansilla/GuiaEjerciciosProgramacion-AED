__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Calculo de polinomio y discriminante ecuacion 2do. grado')
a = float(input('Ingrese el valor de la constante a del polinomio: '))
b = float(input('Ingrese el valor de la constante b del polinomio: '))
c = float(input('Ingrese el valor de la constante c del polinomio: '))
x = float(input('Ingrese el valor de la x del polinomio: '))

# Procesos
y = a * (x ** 2) + b * x + c
discriminante = b ** 2 - 4 * a * c

# Presentacion de resultados
print('El valor del polinomio en el valor x=', x, 'es:', y)
print('El discriminante del polinomio es:', discriminante)