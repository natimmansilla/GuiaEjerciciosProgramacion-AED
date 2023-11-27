__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

from clase import *
import random


def validar_positivo(mensaje):
    n = 0
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print("Valor incorrecto!")
    return n


def read(tickets):
    for i in range(len(tickets)):
        num = random.randint(1, 1000)
        tipo = random.randint(0, 1)
        if tipo == 0:
            desc = "Error "
        else:
            desc = "Reporte "
        desc += str(num)
        estado = random.randint(0, 2)
        tickets[i] = Ticket(num, tipo, desc, estado)


def mostrar_vector(tickets):
    for i in range(len(tickets)):
        print(tickets[i])


def matriz(tickets):
    mat = [0] * 2
    for i in range(len(mat)):
        mat[i] = [0] * 3

    for i in range(len(tickets)):
        fila = tickets[i].tipo
        col = tickets[i].estado
        mat[fila][col] += 1

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                print("Tipo", i, "- Estado", j, "- Cantidad:", mat[i][j])


def buscar(tickets, x):
    for i in range(len(tickets)):
        if x == tickets[i].numero:
            return i
    return -1


def principal():
    n = validar_positivo("Ingrese la cantidad de tickets del mes: ")
    tickets = [None] * n
    carga = False
    op = 1
    while op != 5:
        print("Menú Opciones")
        print("1-Cargar datos")
        print("2-Mostrar vector")
        print("3-Cantidad por tipo y estado")
        print("4-Buscar")
        print("5-Salir")
        op = int(input("Ingrese su opción: "))

        if op == 1:
            read(tickets)
            carga = True
        elif op == 2:
            if carga:
                mostrar_vector(tickets)
            else:
                print("Primero debe cargar los datos")
        elif op == 3:
            if carga:
                matriz(tickets)
            else:
                print("Primero debe cargar los datos")
        elif op == 4:
            if carga:
                x = int(input("Ingrese el número de ticket a buscar: "))
                pos = buscar(tickets, x)
                if pos == -1:
                    print("No se encontró el ticket buscado")
                else:
                    tickets[pos].estado = 2
                    print(tickets[pos])
            else:
                print("Primero debe cargar los datos")

        elif op == 5:
            print("Adiós!")
        else:
            print("Opción incorrecta!")


if __name__ == "__main__":
    principal()
