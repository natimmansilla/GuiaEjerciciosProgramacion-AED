from random import randint

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_mayor(limite, mensaje):
    valor = int(input(mensaje))
    while valor <= limite:
        print('Error!!! El valor ingresado debe ser >', limite)
        valor = int(input(mensaje))
    return valor


def validar_rango(inferior, superior, mensaje):
    numero = int(input(mensaje))
    while numero < inferior or numero > superior:
        print('Error! El numero ingresado debe estar comprandido en el rango [', inferior, ':', superior, ']')
        numero = int(input(mensaje))
    return numero


def menu():
    print('Menu de Opciones')
    print('-' * 90)
    print('1 - Total de horas para un rol')
    print('2 - Total de horas para un proyecto')
    print('3 - Promedio de Horas para Rango de Proyectos')
    print('4 - Total a Cobrar por proyecto')
    print('5 - Salir')
    return int(input('Ingrese su opcion: '))


def generar_matriz(filas, columnas):
    m = [[0] * columnas for _ in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            m[f][c] = validar_mayor(0, 'Ingrese la cantidad de horas para el proyecto ' + str(f) + ' del rol' + str(c))
    return m


def generar_matriz_aleatoria(filas, columnas):
    m = [[0] * columnas for _ in range(filas)]
    for f in range(filas):
        for c in range(columnas):
            m[f][c] = randint(1, 60)
    return m


def totalizar_rol(matriz, rol):
    total = 0
    for f in range(len(matriz)):
        total += matriz[f][rol]
    return total


def totalizar_proyecto(matriz, proyecto):
    total = 0
    for c in range(len(matriz[proyecto])):
        total += matriz[proyecto][c]
    return total


def totalizar_horas(matriz, desde, hasta):
    total = 0
    for f in range(desde, hasta + 1):
        for c in range(len(matriz[desde])):
            total += matriz[f][c]
    return total


def costo_total_por_proyecto(matriz):
    va = [0] * len(matriz)
    for proy in range(len(matriz)):
        va[proy] = totalizar_proyecto(matriz, proy) * 175
    return va


def principal():
    print('Empresa de Tecnologia - Analisis de Proyectos')
    print('_' * 90)

    n = validar_mayor(0, 'Ingrese la cantidad de proyectos de la empresa: ')
    m = validar_mayor(0, 'Ingrese la cantidad de roles que tiene la empresa: ')

    tipo_carga = input('Desea generar la matriz en forma (M)anual o (A)utomatica? ')
    if tipo_carga == 'M':
        matriz = generar_matriz(n, m)
    else:
        matriz = generar_matriz_aleatoria(n, m)

    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            rol = validar_rango(0, m, 'Ingerse el rol que desea totalizar: ')
            total = totalizar_rol(matriz, rol)
            print('El total de horas cargadas por el rol', rol, 'fueron:', total)

        elif opcion == 2:
            proyecto = validar_rango(0, n, 'Ingrese el proyecto que desea totalizar: ')
            total = totalizar_proyecto(matriz, proyecto)
            print('El total de horas cargadas por el proyecto', proyecto, 'fueron:', total)

        elif opcion == 3:
            proy_desde = validar_rango(0, n, 'Ingrese el proyecto que desea totalizar: ')
            proy_hasta = validar_rango(proy_desde, n, 'Ingrese el proyecto que desea totalizar: ')
            total_horas = totalizar_horas(matriz, proy_desde, proy_hasta)
            print('Las horas promedio para los proyecto comprendidos entre', proy_desde, 'y', proy_hasta, end=' ')
            print('fue de ', round(total_horas / (proy_hasta - proy_desde), 2))

        elif opcion == 4:
            va = costo_total_por_proyecto(matriz)
            for i in range(len(va)):
                print('El total a cobrar para el proyecto ', i, ' sera de $', va[i], sep='')


if __name__ == '__main__':
    principal()
