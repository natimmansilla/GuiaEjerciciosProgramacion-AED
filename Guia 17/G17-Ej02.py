__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'

def validar_tamanio():
    n = int(input('Ingrese el tamaño del arreglo: '))
    while n<= 0:
        n = int(input('Debe ser un valor positivo. Ingrese otro: '))
    return n


def validar_dado(mensaje):
    dado = int(input(mensaje))
    while dado <1 or dado > 6:
        dado = int(input('Error!' + mensaje))
    return dado

def cargar(n):
    dado1 = list()
    dado2 = list()
    for i in range(n):
        print('Lanzamiento',i+1)
        dado = validar_dado('Ingrese el valor del dado 1: ')
        dado1.append(dado)
        dado = validar_dado('Ingrese el valor del dado 2: ')
        dado2.append(dado)
    return dado1, dado2


def contar_iguales(dado1, dado2):
    iguales = 0
    for i in range(len(dado1)):
        if dado1[i] == dado2[i]:
            iguales += 1
    return iguales


def buscar_suma_impar(dado1, dado2):
    for i in range(len(dado1)):
        if (dado1[i]  + dado2[i]) % 2 != 0:
            return i+1
    return -1


def buscar_mayor(v):
    mayor = v[0]
    repeticiones = 1
    for i in range(1,len(v)):
        if v[i] > mayor:
            mayor = v[i]
            repeticiones = 1
        elif v[i] == mayor:
            repeticiones += 1
    return mayor, repeticiones


def contar_sumas(dado1, dado2):
    conteo = [0]*13
    for i in range(len(dado1)):
        suma = dado1[i] + dado2 [i]
        conteo[suma] += 1
    return conteo


def mostrar(conteo):
    for i in range(len(conteo)):
        print('Suma',i,'->',conteo[i],'veces')

def sumas_mayores_promedio(dado1, dado2):
    ac = 0
    for i in range(len(dado1)):
        ac += dado1[i]
        ac += dado2[i]

    promedio = ac / len(dado1)
    cant_mayores = 0

    for i in range(len(dado1)):
        s = dado1[i] + dado2[i]
        if s > promedio:
            cant_mayores += 1
    return cant_mayores


def test():
    print('PROGRAMA ESTADÍSTICO')
    n = validar_tamanio()
    dado1, dado2 = cargar(n)
    print()
    print('Dado 1', dado1)
    print('Dado 2', dado2)
    print()
    iguales = contar_iguales(dado1,dado2)
    porcentaje = round(iguales * 100 / n, 2)
    print('Los dados fueron iguales',iguales,'veces y representa el',porcentaje,'% del total')
    print()
    lanzamiento = buscar_suma_impar(dado1, dado2)
    if lanzamiento == -1:
        print('Nunca hubo una suma impar')
    else:
        print('La primer suma impar apareció en el lanzamiento',lanzamiento)
    print()
    mayor, repeticiones = buscar_mayor(dado1)
    print('El mayor valor del dado 1 es',mayor,'y apareció',repeticiones,'veces')
    mayor, repeticiones = buscar_mayor(dado2)
    print('El mayor valor del dado 2 es',mayor,'y apareció',repeticiones,'veces')
    conteo = contar_sumas(dado1,dado)
    print()
    print('Repeticiones')
    mostrar(conteo)
    cantidad_mayores = sumas_mayores_promedio(dado1, dado2)
    print('En', cantidad_mayores, 'tiradas la suma fue mayor al promedio')

test()