__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Carga de datos
a = int(input("Ingrese un número"))
b = int(input("Ingrese un número"))
c = int(input("Ingrese un número"))

# Proceso
suma = a + b + c
if suma > 10:
    resultado = suma // 2
else:
    resultado = suma ** 3

# Presentación de resultados
print("La suma es:", suma)
print("El resultado es:", resultado)
