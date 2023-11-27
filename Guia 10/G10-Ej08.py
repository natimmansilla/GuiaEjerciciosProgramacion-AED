__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_entre(minimo, maximo):
    mensaje = 'Ingrese un valor entre ' + \
              str(minimo) + ' y ' + str(maximo) + ': '
    valor = int(input(mensaje))
    while valor <= minimo or valor >= maximo:
        valor = int(input('Inválido! ' + mensaje))
    return valor


def validar_mayor_que(minimo):
    mensaje = 'Ingrese un valor mayor que ' + str(minimo) + ': '
    valor = int(input(mensaje))
    while valor <= minimo:
        valor = int(input('Inválido! ' + mensaje))
    return valor


def validar_punto_final():
    mensaje = 'Ingrese un texto terminado en punto: '
    texto = input(mensaje)
    while texto[-1] != '.':
        texto = input('Inválido! ' + mensaje)
    return texto


def impares():
    num = validar_entre(0, 11)
    for i in range(11):
        print(num, 'x', i, '=', num * i)


def mayor_y_menor():
    num = validar_mayor_que(-1)
    primero = True
    may = 0
    men = 0
    while num != 0:
        if primero:
            may = num
            men = num
            primero = False
        else:
            if num > may:
                may = num
            if num < men:
                men = num
        num = validar_mayor_que(-1)
    return may, men


def multiplos():
    a = validar_mayor_que(0)
    b = validar_mayor_que(a)
    suma = 0
    for multiplo in range(a, b, a):
        suma += multiplo
    return suma


def calcular_porcentaje(valor, total):
    if total == 0:
        return 0
    else:
        return round(valor * 100 / total, 2)


def texto():
    texto = validar_punto_final()
    # Procesar texto
    vocales = 'aeiou'
    pal_vocal = 0
    palabras = 0
    anterior = ''
    for letra in texto:
        if letra == '.' or letra == ' ':
            if anterior != '':
                palabras += 1
            if anterior in vocales:
                pal_vocal += 1
        else:
            anterior = letra
    # Calcular porcentaje
    porc = calcular_porcentaje(pal_vocal, palabras)
    return pal_vocal, porc


def test():
    opcion = -1
    while opcion != 0:
        print('*' * 80)
        print('OPCIONES REPETITIVAS')
        print('1-Impares')
        print('2-Mayor y menor')
        print('3-Múltiplos')
        print('4-Texto')
        print('0-Salir')
        opcion = int(input('\nIngrese su opción: '))
        if opcion == 1:
            impares()
        elif opcion == 2:
            may, men = mayor_y_menor()
            print('El mayor valor de la serie fue', may)
            print('El menor valor de la serie fue', men)
        elif opcion == 3:
            suma = multiplos()
            print('La suma de los múltiplos es', suma)
        elif opcion == 4:
            pal, porc = texto()
            print('Se detectaron', pal,
                  'palabras con vocal, y son el', porc, 'del texto')
        print('*' * 80)


test()
