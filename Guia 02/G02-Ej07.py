__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


# Titulo y carga de datos
print('Porcentajes de votos parlamentarios')
votos_favor_ley = int(input('Ingrese cantidad de votos a favor de la ley: '))
votos_encontra_ley = int(input('Ingrese cantidad de votos en contra: '))

# Procesos
total = votos_favor_ley + votos_encontra_ley
porcentaje_favor = votos_favor_ley / total * 100
porcentaje_contra = votos_encontra_ley / total * 100

# Presentacion de resultados
print('El porcentaje de votos a favor fue de', porcentaje_favor, '%')
print('El porcentaje de votos en contra fue de', porcentaje_contra, '%')
