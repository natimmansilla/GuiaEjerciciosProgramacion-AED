__author__ = 'Catedra Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Ejercicio: Raíces de un Polinomio de Segundo Grado ')
a = float(input('Ingrese el valor de la constante a del polinomio: '))
b = float(input('Ingrese el valor de la constante b del polinomio: '))
c = float(input('Ingrese el valor de la constante c del polinomio: '))

# Procesos
discriminante = b ** 2 - 4 * a * c
mensaje="****************** Resultado ******************\n"
if discriminante==0:
    solucion=(-b+ (b ** 2 - 4 * a * c)**0.5)/2*a
    mensaje+="Existen dos raíces reales e iguales, por lo tanto hay una solución.\n Solucion: "+str(solucion)
elif discriminante>0:
    solucion1=(-b+ (b ** 2 - 4 * a * c)**0.5)/2*a
    solucion2=(-b- (b ** 2 - 4 * a * c)**0.5)/2*a
    mensaje+="Ambas raíces son reales y distintas, por lo tanto hay dos soluciones.\n Solucion 1: "+str(solucion1)+"\n Solucion 2: "+str(solucion2)
else:
    mensaje+="Ambas raíces son números complejos."

# Presentacion de Resultados
print(mensaje)