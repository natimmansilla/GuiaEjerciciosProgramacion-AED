_author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random


def es_mayuscula(letra):
    return letra >= 'A' and letra <= 'Z'


def es_digito(car):
    digitos = '0123456789'
    return car in digitos


def validar_token(token):
    cant_may = 0
    cant_dig = 0
    pos = 0
    pos_numeral = 0
    for car in token:
        if es_mayuscula(car):
            cant_may += 1
        elif es_digito(car):
            cant_dig += 1
        elif car == '#':
            pos_numeral = pos
        pos += 1
    if cant_may == 2 and cant_dig >= 2 and pos_numeral > len(token) // 2:
        return True
    else:
        return False


def validar_positivo(mensaje):
    num = int(input(mensaje))
    while num <= 0:
        print('Inválido! Debe ser un valor mayor que cero')
        num = int(input(mensaje))
    return num


def generar_datos():
    tipos = 'Particular', 'Empresa'
    monedas = 'Pesos', 'Dolares'
    tipo = random.choice(tipos)
    monto = round(random.uniform(100, 100000), 2)
    moneda = random.choice(monedas)
    return tipo, monto, moneda


def calcular_porcentaje(cant, total):
    if total != 0:
        return cant * 100 / total
    else:
        return 0


def calcular_promedio(suma, cant):
    if cant != 0:
        return suma / cant
    else:
        return 0


def mostrar_menu(n, monto_particulares, porc_dolares, prom_empresas):
    opcion = -1
    while opcion != 0:
        print('-' * 60)
        print('Menu de Opciones')
        print('1 - Cantidad de operaciones')
        print('2 - Porcentaje de operaciones en dolares')
        print('3 - Monto total operado en pesos por particulares')
        print('4 - Monto promedio operado por empresas')
        print('0 - Salir')
        opcion = int(input('Ingrese su opcion: '))
        if opcion == 1:
            print('Total de operaciones =', n)
        elif opcion == 2:
            print('Porcentaje de operaciones en dolares =', round(porc_dolares, 2))
        elif opcion == 3:
            print('Monto total operado en pesos por particulares =', round(monto_particulares, 2))
        elif opcion == 4:
            print('Monto promedio operado en pesos por empresas =', round(prom_empresas, 2))
        print('-' * 60)


def principal():
    print('=' * 20, 'OPERACIONES BANCARIAS', '=' * 20)
    # SUB1 : Validar token
    token = input('Ingrese su token: ')
    if validar_token(token):
        # SUB2: Procesar operaciones
        n = validar_positivo('Ingrese cantidad de operaciones: ')
        ops_dolares = 0
        monto_particulares = 0
        monto_empresas = 0
        ops_empresas = 0
        for i in range(n):
            # Generar datos
            tipo, monto, moneda = generar_datos()
            print('Cliente', tipo, ' - Monto', monto, 'en', moneda)
            # Procesar
            if moneda == 'Dolares':
                ops_dolares += 1
            if moneda == 'Pesos':
                if tipo == 'Particular':
                    monto_particulares += monto
                elif tipo == 'Empresa':
                    monto_empresas += monto
                    ops_empresas += 1
        # Resultados
        porc_dolares = calcular_porcentaje(ops_dolares, n)
        prom_empresas = calcular_promedio(monto_empresas, ops_empresas)
        # SUB3: MOSTRAR MENU
        mostrar_menu(n, monto_particulares, porc_dolares, prom_empresas)
    else:
        print('El token ya no es valido')


principal()