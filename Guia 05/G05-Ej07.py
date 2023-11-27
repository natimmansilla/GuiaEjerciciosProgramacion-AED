__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('El Antivirus mata Pantevil')
print('=' * 80)

pat_inf = input('Ingrese la patente modificada por el virus: ')

# Analizamos la primer parte de la cadena que corresponde de numeros

signos = pat_inf[0:2]
numeros = pat_inf[2:5]
if signos[0] == '+':
    numeros = str(int(numeros[0]) - 1) + str(int(numeros[1]) - 1) + str(int(numeros[2]) - 1)

char = signos[1]
if char == '#':
    numeros = numeros[0] + numeros[0] + numeros[2]
elif char == '$':
    numeros = numeros[0] + numeros[1] + numeros[0]
elif char == '*':
    numeros = numeros[0] + numeros[1] + numeros[1]

# Analizamos la segunda parte de la cadena que corresponde a las letras
letras = pat_inf[6: len(pat_inf)]
char = pat_inf[5]
if char == '@':
    letras = letras[2:4] * 3

inc = 2
letras = chr(int(letras[0:inc])) + chr(int(letras[inc:(inc + 2)])) + chr(int(letras[(inc + 2):]))

patente = letras + ' ' + numeros
print('La patente correcta es:', patente)