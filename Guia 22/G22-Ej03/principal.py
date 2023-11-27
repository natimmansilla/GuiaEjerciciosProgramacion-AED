from utilidades import *

__author__ = 'Algoritmos y Estructuras de Datos'


def menu():
    cadena = "\nMenu de Opciones\n" \
             "==================================================================\n" \
             "1) - Cargar listado de números de telefonía celular bloqueados\n" \
             "2) - Cargar el listado de números telefónicos a validar\n" \
             "3) - Calcular el porcentaje de números telefónicos bloqueados\n" \
             "4) - Determinar la cantidad de numeros que se han vendido para cada característica.\n" \
             "0) - Salir\n" \
             "Ingrese su opcion: "
    return cadena


def cargar_bloqueados(vector, cantidad):
    for i in range(cantidad):
        numero_telefonico = generar_numero_telefonico()
        vector.append(numero_telefonico)


def cargar_lista_numeros(cantidad):
    vector = []
    for i in range(cantidad):
        numero_telefono = generar_numero_telefonico()
        vector.append(numero_telefono)
    return vector


def es_valido(numero, vector_bloqueados):
    pos = busqueda_binaria(numero, vector_bloqueados)
    return pos == -1


def validar_numeros(vector, vector_bloqueados):
    cantidad = 0
    for numero in vector:
        if not es_valido(numero, vector_bloqueados):
            cantidad += 1
    return cantidad


def contar_por_carasteristica(vector, vector_bloqueados):
    vc = [0] * 10
    for numero in vector:
        if es_valido(numero, vector_bloqueados):
            pos = numero.index("-")
            caracteristica = int(numero[0:pos]) - 1
            vc[caracteristica] += 1

    return vc


def principal():
    opcion = -1
    bloqueados = []
    numeros = None
    while opcion != 0:
        opcion = int(input(menu()))
        if opcion == 1:
            if len(bloqueados) == 0:
                n = validar_mayor(0, "Ingrese la cantidad de numeros bloqueados a cargar: ")
                cargar_bloqueados(bloqueados, n)
                ordenar(bloqueados)

            else:
                print("Ya ha cargado el listado de telefonos de bloqueados....")
        elif opcion == 2:
            n = validar_mayor(0, "Ingrese la cantidad de numeros a validar: ")
            numeros = cargar_lista_numeros(n)

        elif numeros is not None:
            if opcion == 3:
                cantidad = validar_numeros(numeros, bloqueados)
                porcentaje = calcular_porcentaje(cantidad, len(numeros))
                print("EL porcentaje de numeros bloqueados fue de", round(porcentaje, 2), "%")

            elif opcion == 4:
                conteo = contar_por_carasteristica(numeros, bloqueados)
                for i in range(len(conteo)):
                    print("La cantidad de numeros para la caracteristica", (i + 1), "fueron:", conteo[i])
        else:
            print("Debe ejecutar la opcion 2 que carga numeros a validar")


if __name__ == '__main__':
    principal()
