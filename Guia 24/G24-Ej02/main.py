__author__ = 'Algoritmos y Estructuras de Datos'

import random

import manejo_archivo
import manejo_vector
import registro
from registro import Alquiler


def menu():
    cadena = 'Menu de Opciones \n' \
             '====================================================================================================' \
             '\n' \
             '1 - Mostrar el vector incluyendo, la descripcion del tipo de residencias\n' \
             '2 - Agregar un nuevo alquiler al arreglo. Validar que el numero sea unico antes de solicitar' \
             ' el resto de la informacion\n' \
             '3 - Determinar el monto total de los alquileres, por tipo de residencia y cantidad de personas que' \
             ' habitaran la residencia\n' \
             '4 - Crear un nuevo arreglo con todas los alquileres segun criterio\n' \
             '5 - Indicar para un tipo de residencia cual es el monto total a cobrar\n' \
             '0 - Salir del programa\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def mostrar_alquileres(alquileres):
    cad = '|{:<8} | {:<30} | {:^10} | {:<20} | {:>11} | {:^4} |\n'
    titulo = '_' * 101 + '\n'
    titulo += cad.format('Numero', 'Nombre', 'Cant Pers.', 'Tipo Residencia', 'Monto', 'Dias')
    titulo += '_' * 101 + '\n'
    for alquiler in alquileres:
        titulo += '|' + str(alquiler) + ' |\n'
    titulo += '_' * 101 + '\n'
    print(titulo)


def agregar_alquiler(alquileres):
    nombres = ('Cyrus Phelps', 'Nigel Graham', 'Brett Andrews', 'Nasim Saunders', 'Hop Oneill', 'Kevin Crane',
               'Jermaine Allen', 'Hakeem Burn', 'Keegan Hawk', 'Daquan Luca', 'Tate Simon')
    numero = registro.generar_numero_alquiler()
    while manejo_vector.existe(numero, alquileres):
        print('El numero existe, se generara y comprobara un nuevo numero de alquiler')
        numero = registro.generar_numero_alquiler()

    nombre = random.choice(nombres)
    personas = random.randint(1, 8)
    tipo = random.randrange(6)
    monto = random.uniform(100, 1000)
    dias = random.randint(1, 28)
    alquiler = Alquiler(numero, nombre, personas, tipo, monto, dias)
    alquileres.append(alquiler)


def generar_matriz(vector):
    matriz = [[0] * 8 for i in range(6)]
    for alquiler in vector:
        fila = alquiler.tipo_residencia
        columna = alquiler.cantidad_personas - 1
        matriz[fila][columna] += alquiler.monto * alquiler.cantidad_dias

    return matriz


def mostrar_matriz(matriz):
    cad = 'El monto total de los alquileres para el tipo de residencia {} con {} personas ' \
          'fue ${:<10.2f}'
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 0:
                res = registro.descripcion_tipo_residencia(i)
                pers = j + 1
                print(cad.format(res, pers, matriz[i][j]))


def generar_lista_por_monto(vector, x):
    v = []
    for alquiler in vector:
        if alquiler.monto < x and alquiler.tipo_residencia < 4:
            v.append(alquiler)
    return v


def totalizar_tipo_residencia(matriz, tr):
    total = 0
    for j in range(len(matriz[tr])):
        total += matriz[tr][j]
    return total


def principal():
    opcion = -1
    alquileres = manejo_archivo.generar_arreglo()
    matriz = None
    matriz_generada = False

    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            mostrar_alquileres(alquileres)

        elif opcion == 2:
            agregar_alquiler(alquileres)

        elif opcion == 3:
            matriz_generada = True
            matriz = generar_matriz(alquileres)
            mostrar_matriz(matriz)

        elif opcion == 4:
            x = float(input('Ingrese el monto por dia maximo que desea buscar: '))
            lista = generar_lista_por_monto(alquileres, x)
            manejo_vector.ordenar(lista)
            mostrar_alquileres(lista)

        elif opcion == 5:
            if matriz_generada:
                tr = random.randrange(6)
                total = totalizar_tipo_residencia(matriz, tr)
                print('El total para el tipo de residencia' + registro.descripcion_tipo_residencia(tr) + 'fue de $' +
                      str(round(total, 2)))
            else:
                print('Para totalizar primero debe ejecutar la opcion 3')
        elif opcion == 0:
            manejo_archivo.grabar_arreglo(alquileres)


if __name__ == '__main__':
    principal()
