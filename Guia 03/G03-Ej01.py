__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Calculo de interés y saldo final en un plazo fijo')
capital = float(input('Ingrese el capital del plazo fijo: '))

# Procesos
capital_final = capital * 1.023 - 20

# La función round(x, n) retorna el número flotante x, 
# pero redondeado a n digitos a la derecha del punto decimal.
capital_final = round(capital_final, 2)

# Presentacion de resultados
print('El capital final que se obtiene del plazo fijo es:', capital_final)