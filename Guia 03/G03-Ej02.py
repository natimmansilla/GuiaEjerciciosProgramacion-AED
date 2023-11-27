__author__ = 'Catedra de Algoritmos y Estructura de Datos'

# Titulo y carga de datos
print('Ver una fecha en diferente formato')
fecha = input('Cargue la fecha en formato dd/mm/yyyy (incluyendo ceros): ')

# Procesos
dia = fecha[0] + fecha [1]
mes = fecha[3] + fecha[4]
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]

# Presentacion de Resultados
print('Dia:', dia, '- Mes:', mes, '- Año:', anio)