__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Titulos y carga de Datos
print('Calculo de angulos')
x = float(input('Ingrese el valor de la suma de los angulos a buscar: '))
y = float(input('Ingrese el valor de la resta de los angulos a buscar: '))

# Procesos: se sabe que:
# x = alfa + beta
# y = alfa - beta

# De donde:
# x = alfa + beta
# =>  alfa = x - beta

# Por lo tanto:
# y = alfa - beta
# => y = x - beta - beta
# => y = x - 2*beta
# => y + 2*beta = x
# => 2*beta = x - y
# => beta = (x-y)/2

# Entonces:
# Si y = alfa - beta
# => alfa = y + beta

beta = (x-y)/2
alfa = y + beta

print('Valor del angulo alfa:', alfa)
print('Valor del angulo beta:', beta)