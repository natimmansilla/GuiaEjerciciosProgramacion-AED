__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Sumador ángulos
# RESOLUCION CON TUPLAS (II)

#Títulos
print('SUMADOR DE ANGULOS')
print('-' * 80)

# Datos
print('Angulo 1')
grados = int(input('Ingrese grados: '))
minutos = int(input('Ingrese minutos: '))
segundos = int(input('Ingrese segundos: '))
angulo1 = grados, minutos, segundos

print('Angulo 2')
grados = int(input('Ingrese grados: '))
minutos = int(input('Ingrese minutos: '))
segundos = int(input('Ingrese segundos: '))
angulo2 = grados, minutos, segundos
print('\nSuma de', angulo1, '+', angulo2)

# Proceso

# Convertir angulo en segundos = grados * 3600 + minutos * 60 + segundos
ang1_seg = angulo1[0] * 3600 + angulo1[1] * 60 + angulo1[2]
ang2_seg = angulo2[0] * 3600 + angulo2[1] * 60 + angulo2[2]

# Sumar los segundos
suma_seg = ang1_seg + ang2_seg
print('\nSuma en segundos:', ang1_seg, '+', ang2_seg, '=', suma_seg)

# Convertir la suma a grados, minutos y segundos
# Segundos a grados --> division entera por 3600
# (el resto son segundos)
grados = suma_seg // 3600
resto_seg = suma_seg % 3600
# Segundos a minutos --> division entera por 60
# (el resto son segundos)
minutos = resto_seg // 60
segundos = resto_seg % 60
# Armar el ángulo resultante
angulo_suma = grados, minutos, segundos

# Resultado
print('\nSuma sexagesimal:', angulo_suma)