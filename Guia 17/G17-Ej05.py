import random


def menu():
    print("1 _ Cargar datos")
    print("2 _ Mostrar datos")
    print("3 _ Monto total")
    print("4 _ Listado por tipo")
    print("5 _ Cantidad por tipo")
    print("6 _ Salir")
    op = int(input("Ingrese su opción:"))
    return op


def cargar_datos(n):
    descripciones = [""] * n
    montos = [0.0] * n
    tipos = [0] * n

    for i in range(n):
        descripciones[i] = input("Ingrese descripción: ")
        montos[i] = float(input("Ingrese monto: "))
        tipos[i] = int(input("Ingrese tipo: "))

    return descripciones, montos, tipos


def cargar_datos_random(n):
    descripciones = [""] * n
    montos = [0.0] * n
    tipos = [0] * n

    for i in range(n):
        descripciones[i] = "Articulo " + str(random.randint(1, 100))
        montos[i] = round(random.uniform(100, 2000), 2)
        tipos[i] = random.randint(0, 9)

    return descripciones, montos, tipos


def mostrar_ventas(descripciones, montos, tipos):
    for i in range(len(descripciones)):
        print("Descripción:", descripciones[i], "Monto:", montos[i], "Tipo:", tipos[i])


def mostrar_ventas_tipo(descripciones, montos, tipos, filtro):
    for i in range(len(descripciones)):
        if tipos[i] == filtro:
            print("Descripción:", descripciones[i], "Monto:", montos[i], "Tipo:", tipos[i])


def validar(descripciones):
    if len(descripciones) == 0:
        print("Debe ingresar los datos primero")
        return False
    return True


def calcular_monto_total(montos):
    suma = 0
    for monto in montos:
        suma += monto

    return suma


def ordenar(descripciones, montos, tipos):
    n = len(descripciones)
    for i in range(n-1):
        for j in range(i+1, n):
            if descripciones[i] > descripciones[j]:
                descripciones[i], descripciones[j] = descripciones[j], descripciones[i]
                montos[i], montos[j] = montos[j], montos[i]
                tipos[i], tipos[j] = tipos[j], tipos[i]


def cantidad_por_tipo(tipos):
    cantidad = [0] * 10
    for t in tipos:
        cantidad[t] += 1

    return cantidad


def main():
    op = -1
    descripciones = montos = tipos = []
    while op != 6:
        op = menu()
        if op == 1:
            n = int(input("Ingrese cantidad de ventas: "))
            descripciones, montos, tipos = cargar_datos_random(n)
            ordenar(descripciones, montos, tipos)
        elif op == 2:
            if validar(descripciones):
                mostrar_ventas(descripciones, montos, tipos)
        elif op == 3:
            if validar(descripciones):
                monto = calcular_monto_total(montos)
                print("El monto total es:", monto)
        elif op == 4:
            if validar(descripciones):
                tipo = int(input("Ingrese tipo a mostrar: "))
                mostrar_ventas_tipo(descripciones, montos, tipos, tipo)
        elif op == 5:
            if validar(descripciones):
                cantidades = cantidad_por_tipo(tipos)
                for i in range(len(cantidades)):
                    if cantidades[i] != 0:
                        print("Tipo:", i, "Cantidad:", cantidades[i])


if __name__ == '__main__':
    main()