frente = float(input('Ingrese el frente del terreno (en metros): '))
fondo = float(input('Ingrese fondo del terreno (en metros): '))

# Proceso
if frente == fondo:
    forma = "CUADRADA"
else:
    forma = "RECTANGULAR"

superficie = round(frente * fondo, 2)

# Resultados
print('El terreno tiene forma', forma, 'y', superficie, 'metros cuadrados de superficie')
