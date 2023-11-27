__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Presentación e ingreso de datos
print('GALERÍA DE ARTE')
cuadro1 = int(input('Ingrese año de creación del cuadro 1: '))
cuadro2 = int(input('Ingrese año de creación del cuadro 2: '))
cuadro3 = int(input('Ingrese año de creación del cuadro 3: '))

# Proceso
# Todos los cuadros son anteriores al siglo XX?
mensaje_sxx = ' son anteriores al siglo XX'
if cuadro1 < 1900 and cuadro2 <= 1900 and cuadro3 <= 1900:
    mensaje_sxx = 'TODOS' + mensaje_sxx
else:
    mensaje_sxx = 'NO TODOS' + mensaje_sxx
# Alguno fue creado en cierto año?
anio = int(input('\nIngrese año de creación a buscar: '))
mensaje_anio = ' hay cuadros correspondientes al año ' + str(anio)
if cuadro1 == anio or cuadro2 == anio or cuadro3 == anio:
    mensaje_anio = 'SÍ' + mensaje_anio
else:
    mensaje_anio = 'NO' + mensaje_anio
# Diferencia entre más nueva y más antigua
nueva = max(cuadro1, cuadro2, cuadro3)
antigua = min(cuadro1, cuadro2, cuadro3)
diferencia = nueva - antigua

# Resultados
print(mensaje_sxx)
print(mensaje_anio)
print('La diferencia entre la obra más nueva (', nueva, ') y la más antigua (', antigua, ') es', diferencia, 'años')
