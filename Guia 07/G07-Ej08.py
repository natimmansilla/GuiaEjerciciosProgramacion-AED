__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Encabezado de la consola
print()
print('_' * 40)
print('Programa de estadísticas del Club Naútico')
print('_' * 40)
print()

# Leer la cantidad de datos a cargar (n que representa la cantidad de barcos)
n = int(input('Ingrese la cantidad de Embarcaciones a cargar: '))

# Segmento de inicialización de contadores acumuladores y banderas
total_anual_veleros = total_anual_lanchas = 0
primero = True
suma_total_mensual = suma_mensual_veleros = suma_mensual_lanchas = 0
cantidad = 0

# Comienza la carga y proceso de los datos
print()
print('Cargue los datos de las Embarcaciones...')
print()
for i in range(n):
    # Lectura de datos de cada barco
    nombre = input('Ingrese el nombre de la Embarcación: ')
    tipo = int(input('Ingrese el tipo de embarcación (1 - para Veleros o 2 - para Lanchas): '))
    importe_mensual = float(input('Ingrese el importe mensual pagado: '))

    if tipo == 1:
        # Incremento el total anual de los veleros
        # Esto también se podría resolver al final a partir del total mensual
        total_anual_veleros += importe_mensual * 12

        # Busco el velero con mayor cuota mensual
        # Utilizamos la alternativa que sirve para todos los casos por más que como dijimos en este caso había otras opciones
        if primero or importe_mensual > mayor_cuota:
            mayor_cuota = importe_mensual
            nombre_mayor = nombre
            primero = False

        # Incremento la suma mensual para los veleros para el cálculo de los porcentajes
        suma_mensual_veleros += importe_mensual
    else:
        # Incremento el total anual de las lanchas
        # También se podría resolver al final a partir del total mensual
        total_anual_lanchas += importe_mensual * 12

        # Incremento la suma mensual para las lanchas para el cálculo de los porcentajes
        suma_mensual_lanchas += importe_mensual

    # Incremento la suma total
    # (como también dijimos en clase este valor también se podía calcular porque en este caso en ambas ramas del if estamos sumando cada importe
    suma_total_mensual += importe_mensual

    # Cuento la cantidad de barcos
    cantidad += 1

# Si se cargaron barcos, Calculo el promedio pedido en el punto 3
if cantidad > 0:
    promedio = suma_total_mensual / cantidad

# Calculo los porcentajes solicitados en el punto 4
porcentaje_veleros = suma_mensual_veleros * 100 / suma_total_mensual
porcentaje_lanchas = suma_mensual_lanchas * 100 / suma_total_mensual

# Muestro los resultados solicitados
print()
print('_' * 40)
print('Resultados estadísticos')
print('_' * 40)
print()

print('El total anual aportado por los Veleros es:', round(total_anual_veleros, 2))
print('El total anual aportado por las Lanchas es:', round(total_anual_lanchas, 2))

# Para el caso del mayor valido que se haya cargado algun velero y sino muestro un mensaje
print()
if not primero:
    print('El Velero que mayor cuota mensual paga es:', nombre_mayor, 'y paga:', mayor_cuota)
else:
    print('No se cargaron Veleros, por lo que no hay Velero con mayor cuota mensual...')

print()
print('La cuota mensual promedio abonada por todas las embarcaciones fue:', round(promedio, 2))

print()
print('De un total mensual recuadudado de:', suma_total_mensual)
print('Los Veleros aportaron un ' + str(round(porcentaje_veleros, 2)) + '%')
print('Las Lanchas aportaron un ' + str(round(porcentaje_lanchas, 2)) + '%')

# Muestro un mensaje de fin y solicito que presione enter para finalizar
print()
print('_' * 40)
print('Fin.')
print('_' * 40)
