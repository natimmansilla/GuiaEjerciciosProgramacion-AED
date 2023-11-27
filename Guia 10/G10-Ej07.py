__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_mayor(valor, mensaje):
    numero = int(input(mensaje))
    while numero <= valor:
        print('Error!!! El numero debe ser mayor a', valor)
        numero = int(input(mensaje))

    return numero


def es_multiplo(numero, divisor):
    paridad = numero % divisor
    if paridad == 0:
        return True
    else:
        return False


def multiplos_primer_valor():
    cantidad = 0
    numero = validar_mayor(-1, 'Ingrese un numero de la secuencia (finaliza con cero): ')
    es_primero = True
    primero = -1
    while numero != 0:
        if es_primero:
            es_primero = False
            primero = numero
        else:
            if es_multiplo(numero, primero):
                cantidad += 1
        numero = validar_mayor(-1, 'Ingrese otro numero de la secuencia: ')
    return cantidad


def leer_intervalo():
    p = validar_mayor(0, 'Ingrese la cota inferior del intervalo: ')
    q = validar_mayor(0, 'Ingrese la cota superior del intervalo: ')
    while q < p:
        print('El Intervalo definido no es correcto, reingrese los valores')
        p = validar_mayor(0, 'Ingrese la cota inferior del intervalo: ')
        q = validar_mayor(0, 'Ingrese la cota superior del intervalo: ')
    return p, q


def es_par(numero):
    return es_multiplo(numero, 2)


def analizar_intervalo(p, q, n):
    can_fuera = can_dentro, can_pares = 0
    for i in range(n):
        numero = int(input('Ingrese un numero a analizar: '))
        if numero < p or numero > q:
            can_fuera += 1
        else:
            can_dentro += 1
            if es_par(numero):
                can_pares += 1

    return can_fuera, can_dentro, can_pares


def calcular_promerio(dividendo, divisor):
    prom = 0
    if divisor != 0:
        prom = dividendo / divisor
    return round(prom, 2)


def analizar_pares_contiguos():
    numero = validar_mayor(0, 'Ingrese un numero de la secuencia: ')
    anterior = -1
    hay_pares_contiguos = False
    acumulador = contador = 0
    while numero < 100:
        if es_par(numero):
            contador += 1
            acumulador += numero

        if es_par(anterior) and es_par(numero):
            hay_pares_contiguos = True

        anterior = numero
        numero = validar_mayor(0, 'Ingrese un numero de la secuencia: ')

    prom = 0
    if hay_pares_contiguos:
        prom = calcular_promerio(acumulador, contador)
    return hay_pares_contiguos, prom


def test():
    menu = 'Menu de Opciones\n' \
           '1 - Secuencia de multiplos\n' \
           '2 - Analisis de rango\n' \
           '3 - Promedio de Pares\n' \
           '4 - Salir\n' \
           'Ingrese su opcion: '

    opcion = - 1
    while opcion != 4:
        opcion = int(input(menu))
        if opcion == 1:
            cant_numero = multiplos_primer_valor()
            print('La cantidad de numeros multiplos del primero son:', cant_numero)
        elif opcion == 2:
            p, q = leer_intervalo()
            n = validar_mayor(0, 'Ingrese la cantidad de numeros a procesar: ')

            cant_fuera, cant_dentro, cant_pares_dentro = analizar_intervalo(p, q, n)

            print('La cantidad de valores fuera de [', p, ':', q, '] son: ', cant_fuera, sep='')
            print('La cantidad de valores dentro de [', p, ':', q, '] son: ', cant_dentro, sep='')
            print('La cantidad de valores pares dentro de [', p, ':', q, '] son: ', cant_pares_dentro, sep='')
        elif opcion == 3:
            hay_pares, promedio = analizar_pares_contiguos()
            if hay_pares:
                print('En la secuencia hubo pares contiguos y su promedio es:', promedio)
            else:
                print('En la secuencia no hubo pares contiguos')


test()
