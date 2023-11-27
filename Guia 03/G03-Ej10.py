__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('TRIATLÓN')
natacion = input("Ingrese tiempo de natación (mm:ss):")
ciclismo = input("Ingrese tiempo de ciclismo (mm:ss):")
pedestre = input("Ingrese tiempo de carrera pedestre (mm:ss):")

# Procesos

# Identificar componentes y convertir a segundos
natacion_seg = int(natacion[0] + natacion[1])*60 + int(natacion[3] + natacion[4])
ciclismo_seg = int(ciclismo[0] + ciclismo[1])*60 + int(ciclismo[3] + ciclismo[4])
pedestre_seg = int(pedestre[0] + pedestre[1])*60 + int(pedestre[3] + pedestre[4])

# Calcular el total en segundos
total = natacion_seg + ciclismo_seg + pedestre_seg
horas = divmod(total,3600)
total_hh = horas[0]
minutos = divmod(horas[1],60)
total_mm = minutos[0]
total_ss = minutos[1]

#Determinar el mayor y menor tiempo
mayor_tiempo = max(natacion_seg,ciclismo_seg,pedestre_seg)
menor_tiempo = min(natacion_seg,ciclismo_seg,pedestre_seg)

#Determinar tiempo promedio y redondearlo
promedio = (natacion_seg + ciclismo_seg + pedestre_seg)/3
promedio = round(promedio,2)

# Resultados
print("\nEstadísticas")
print("El tiempo total es: ", total_hh,":",total_mm,":",total_ss)
print("El mayor tiempo (en segundos) es: ",mayor_tiempo)
print("El menor tiempo (en segundos) es: ",menor_tiempo)
print("El tiempo promedio(en segundos) es: ",promedio)