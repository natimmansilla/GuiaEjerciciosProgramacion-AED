__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

suma_tiempos = 0
menor_tiempo = None
menor_nombre = None

es_el_primero = True

n = int(input("Ingrese la cantidad de corredores: "))

for i in range(n):
    # La variable i toma los valores entre 0 y n-1
    # Este ciclo va a dar una vuelta por cada ciclista

    nombre = input("Ingrese el nombre del ciclista: ")
    tiempo = int(input("Ingrese el tiempo: "))

    # Búsqueda del menor tiempo
    # Tenemos que garantizar que menor_tiempo empiece igual al primer valor

    # Alternativas válidas
    # if i == 0 or tiempo < menor_tiempo:
    # if es_el_primero or tiempo < menor_tiempo:
    # if menor is None or tiempo < menor_tiempo:
    if es_el_primero or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        menor_nombre = nombre

    # Promedio: acumulador / contador
    suma_tiempos += tiempo
    es_el_primero = False

promedio_tiempos = suma_tiempos / n

# Esta variable podria ser ingresada al principio
tiempo_record = int(input("Ingrese el tiempo record: "))

if menor_tiempo < tiempo_record:
    print("El ganador batió el record!!!!")

print("El nombre del ciclista que hizo el menor tiempo es: ", menor_nombre)
print("El promedio de tiempos es:", promedio_tiempos)
