__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print('VOTACION EN EL SENADO')

# Ingresar votos
favor = int(input('Ingrese votos a favor: '))
contra = int(input('Ingrese votos en contra: '))
abstenciones = int(input('Ingrese abstenciones: '))

# Calcular total de presentes para la votación
total = favor + contra + abstenciones

# Definir resultado
resultado = '\nLa ley fue '
if favor > (contra + abstenciones):
    resultado += 'aprobada por mayoría absoluta.'
elif favor > contra:
    resultado += 'aprobada por mayoría simple.'
else:
    resultado += 'rechazada.'

# Calcular ausentes
ausentes = 72 - total

# mostrar resultados
print(resultado)
print("La cantidad de senadores ausentes fue:", ausentes)