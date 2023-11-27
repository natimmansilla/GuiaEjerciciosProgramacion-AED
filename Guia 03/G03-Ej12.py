__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Calculo tiempo ganador de posta 4x100')
print('*' * 80)

# tomar cada estilo y pasarlo a centésimas para sumar
espalda = 52*100 + 15
pecho = 62*100 + 75
mariposa = 59*100 + 80
crol = 48*100 + 15

total = espalda + pecho + mariposa + crol

# convertir el total a minutos, segundos y centésimas para el tiempo total
# total de centésimas por minuto:
# 1 min -> 60 seg y 1 seg -> 10 cs => 1 min = 60 * 100 = 6000 centésimas.

minutos = total // 6000
resto = total % 6000

segundos = resto // 100
centesimas = resto % 100

print('Total:', minutos, 'minutos', segundos, 'segundos y', centesimas, 'centesimas')