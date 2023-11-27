__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Postulantes a un empleo')
print('=' * 80, '\n')

# Entrada
print('Lectura de Datos del primer postulante')
nombre1 = input('Ingrese el nombre: ')
preguntas1 = int(input('Ingrese cuantas preguntas se le realizaron: '))
respondidas1 = int(input('Ingrese la cantidad de preguntas que respondio: '))

print('\nLectura de Datos del segundo postulante')
nombre2 = input('Ingrese el nombre: ')
preguntas2 = int(input('Ingrese cuantas preguntas se le realizaron: '))
respondidas2 = int(input('Ingrese la cantidad de preguntas que respondio: '))

print('\nLectura de Datos del tercer postulante')
nombre3 = input('Ingrese el nombre: ')
preguntas3 = int(input('Ingrese cuantas preguntas se le realizaron: '))
respondidas3 = int(input('Ingrese la cantidad de preguntas que respondio: '))

# Procesos
porcentaje1 = respondidas1 / preguntas1 * 100
porcentaje2 = respondidas2 / preguntas2 * 100
porcentaje3 = respondidas3 / preguntas3 * 100

# Determinar nivel en base al porcentaje de cada postulante
if porcentaje1 > 90:
    nivel1 = 'Nivel superior'
elif 75 <= porcentaje1 < 90:
    nivel1 = 'Nivel Medio'
elif 50 <= porcentaje1 < 75:
    nivel1 = 'Nivel Regular'
else:
    nivel1 = 'Fuera de Nivel'

if porcentaje2 > 90:
    nivel2 = 'Nivel superior'
elif 75 <= porcentaje2 < 90:
    nivel2 = 'Nivel Medio'
elif 50 <= porcentaje2 < 75:
    nivel2 = 'Nivel Regular'
else:
    nivel2 = 'Fuera de Nivel'

if porcentaje3 > 90:
    nivel3 = 'Nivel superior'
elif 75 <= porcentaje3 < 90:
    nivel3 = 'Nivel Medio'
elif 50 <= porcentaje3 < 75:
    nivel3 = 'Nivel Regular'
else:
    nivel3 = 'Fuera de Nivel'


if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
    mayor_nombre = nombre1
    mayor_nivel = nivel1
    mayor_porcentaje = porcentaje1
elif porcentaje2 > porcentaje3:
    mayor_nombre = nombre2
    mayor_nivel = nivel2
    mayor_porcentaje = porcentaje2
else:
    mayor_nombre = nombre3
    mayor_nivel = nivel3
    mayor_porcentaje = porcentaje3

# Presentación de resultados
print('El Postulante', nombre1, 'obtuvo el nivel', nivel1)
print('El Postulante', nombre2, 'obtuvo el nivel', nivel2)
print('El Postulante', nombre3, 'obtuvo el nivel', nivel3)

print('El postulante que obtuvo el puesto es', mayor_nombre, 'al responder \
correctamente el', mayor_porcentaje, '% obteniendo un nivel', mayor_nivel)