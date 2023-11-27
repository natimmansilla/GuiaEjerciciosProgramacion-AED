from generales import *
from vector import *
import random

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def cargar_manual(n):
    tabla = [[0] * 3 for f in range(10)]
    for i in range(n):
        caja = validar_entre(0, 9, 'Ingrese el numero de caja: ')
        turno = validar_entre(0, 2, 'Ingrese el turno: ')
        monto = validar_mayor_que(0, 'Ingrese el monto a cobrar del servicio: ')
        tabla[caja][turno] += monto
    return tabla


def cargar_automatico(n):
    tabla = [[0] * 3 for f in range(10)]
    for i in range(n):
        caja = random.randrange(10)
        turno = random.randrange(3)
        monto = random.randint(100, 1000)
        tabla[caja][turno] += monto
    return tabla


def mostrar(tabla):
    print('Turno', 'Mañana', 'Tarde', 'Noche', sep='\t', end='')
    for f in range(len(tabla)):
        print('\nCaja ', f, ': ', sep='', end='')
        for c in range(len(tabla[f])):
            print('\t$', tabla[f][c], sep='', end=' ')


def calcular_promedio(tabla, caja):
    total = 0
    turnos = len(tabla[caja])
    for col in range(turnos):
        total += tabla[caja][col]
    return round(total / turnos, 2)


def totalizar_turnos(tabla):
    va = [0] * len(tabla[0])
    for col in range(len(tabla[0])):
        for fila in range(len(tabla)):
            va[col] += tabla[fila][col]
    return va


def menor_recaudacion(tabla):
    menor = tabla[0][0]
    caja, turno = 0, 0
    for fila in range(len(tabla)):
        for col in range(len(tabla[fila])):
            if tabla[fila][col] < menor:
                menor = tabla[fila][col]
                caja, turno = fila, col
    return caja, turno


def principal():
    n = validar_mayor_que(0, 'Ingrese la cantidad de servicios: ')

    tipo_carga = input('Ingrese si la carga sera (M)anual o (A)utomatica: ')
    if tipo_carga == 'M':
        tabla = cargar_manual(n)
    else:
        tabla = cargar_automatico(n)

    mostrar(tabla)

    opcion = -1
    while opcion != 0:
        print('Menu de Opciones')
        print('1 - Recaudacion Promedio de una Caja')
        print('2 - Total Recaudado por turno')
        print('3 - Caja/Turno con menor recaudacion')
        print('0 - Salir')
        opcion = int(input('Ingrese su opcion: '))
        if opcion == 1:
            caja = validar_entre(0, 9, 'Ingrese la caja a calcular el promedio recaudado: ')
            promedio = calcular_promedio(tabla, caja)
            print('El promedio recaudado para la caja', caja, 'es', promedio)

        elif opcion == 2:
            vec_total_turnos = totalizar_turnos(tabla)
            mayor = buscar_mayor(vec_total_turnos)
            total = sumar_vector(vec_total_turnos)
            porcentaje = calcular_porcentaje(mayor, total)
            print('Total por turnos:', vec_total_turnos)
            print('El mayor monto fue', mayor, 'y representa el', porcentaje, '% del total')

        elif opcion == 3:
            caja, turno = menor_recaudacion(tabla)
            print('La menor recaudacion fue de la caja', caja, 'en el turno', turno)


if __name__ == '__main__':
    principal()
