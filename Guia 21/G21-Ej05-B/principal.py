import random

from generales import *


def cargar_matriz(n, carga, m):
    for i in range(n):
        if carga == 'M':
            caja = validar_entre(0, 9, 'Ingrese caja (0-9): ')
            turno = validar_entre(0, 2, 'Ingrese turno (0-2): ')
            monto = validar_mayor_que(0, 'Ingrese monto: $')
        else:
            caja = random.randint(0, 9)
            turno = random.randint(0, 2)
            monto = random.randint(100, 1000)
            print('Cobranza', i, ': Caja', caja, 'Turno', turno, 'Monto $', monto)
        m[caja][turno] += monto


def mostrar_matriz(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > 0:
                print('Caja', f, 'Turno', c, ': $', m[f][c])


def mostrar_menu():
    print('=' * 80)
    print('Menú de opciones')
    print('1. Recaudación promedio por caja')
    print('2. Total recaudado por cada turno')
    print('3. Menor recaudacion')
    print('0. Salir')
    opcion = int(input('Ingrese opción: '))
    return opcion


def promediar_fila(m, caja):
    suma = 0
    cols = len(m[caja])
    for c in range(cols):
        suma += m[caja][c]
    return suma / cols


def sumar_columnas(m):
    cols = len(m[0])
    suma = [0] * cols
    for f in range(len(m)):
        for c in range(cols):
            suma[c] += m[f][c]
    return suma


def buscar_mayor(v):
    may = 0
    for i in range(1, len(v)):
        if v[i] > v[may]:
            may = i
    return may


def sumar_vector(v):
    total = 0
    for i in range(len(v)):
        total += v[i]
    return total


def buscar_menor(m):
    menf, menc = 0, 0
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] < m[menf][menc]:
                menf, menc = f, c
    return menf, menc


def principal():
    print('COBRO DE SERVICIOS')
    # Carga de datos
    n = validar_mayor_que(0, 'Ingrese cantidad de cobranzas: ')
    carga = input('Elija carga (M)anual o (A)utomatica: ')
    m = [[0] * 3 for f in range(10)]
    cargar_matriz(n, carga, m)
    print('\nRESUMEN DE COBRANZAS')
    mostrar_matriz(m)
    # Menú de opciones
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            # Recaudación promedio, para una caja que se ingresa por teclado
            caja = validar_entre(0, 9, 'Ingrese caja (0-9) a promediar: ')
            prom = promediar_fila(m, caja)
            print('Promedio para la caja', caja, '$', prom)
        elif opcion == 2:
            # Total recaudado por cada turno, cuál es el mayor y qué porcentaje representa sobre la recaudación total.
            turnos = sumar_columnas(m)
            print('Total recaudado por turno', turnos)
            may = buscar_mayor(turnos)
            print('La mayor recaudación fue en el turno', may, ' $', turnos[may])
            total = sumar_vector(turnos)
            porc = turnos[may] * 100 / total
            print('Representa el', round(porc, 2), '% sobre el total de $', total)
        elif opcion == 3:
            # Qué caja y turno tuvo la menor recaudación acumulada
            caja, turno = buscar_menor(m)
            print('La menor recaudación fue en la caja', caja, ' en el turno', turno, ': $', m[caja][turno])
        elif opcion == 0:
            print('Hasta pronto!')
        else:
            print('Opción inválida')


if __name__ == '__main__':
    principal()
