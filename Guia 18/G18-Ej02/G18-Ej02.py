def menu():
    print("Menu de opciones: ")
    print("1_ Cargar datos")
    print("2_ Determinar monto promedio")
    print("3_ Generar listado")
    print("4_ Dia mayor cantidad")
    print("5_ Salir")
    return int(input("Ingrese opción: "))


def cargar_datos():
    cantidad = int(input("Ingrese la cantidad de transportes realizados: "))
    dias = [0] * cantidad
    descripciones = [''] * cantidad
    montos = [0.0] * cantidad

    for i in range(cantidad):
        dias[i] = int(input("Ingrese dia: "))
        descripciones[i] = input("Ingrese descripción: ")
        montos[i] = float(input("Ingrese monto: "))

    return dias, descripciones, montos


def calcular_promedio(montos):
    suma = 0
    for valor in montos:
        suma += valor
    return suma / len(montos)


def listar(dias, descripciones, montos):
    for i in range(len(dias)):
        print("Dia:", dias[i], "Monto:", montos[i],
              "Descripcion:", descripciones[i])


def ordenar(dias, descripciones, montos):
    n = len(montos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if montos[i] < montos[j]:
                montos[i], montos[j] = montos[j], montos[i]
                dias[i], dias[j] = dias[j], dias[i]
                descripciones[i], descripciones[j] = descripciones[j], descripciones[i]


def calcular_transportes_dia(dias):
    cant = [0] * 31
    for x in dias:
        cant[x - 1] += 1
    return cant


def dia_mas_transportes(dias):
    x_dia = calcular_transportes_dia(dias)
    mayor = mayor_dia = 0
    for i in range(len(x_dia)):
        if x_dia[i] > mayor:
            mayor = x_dia[i]
            mayor_dia = i
    return mayor_dia + 1, mayor


def main():
    op = 0
    while op != 5:
        op = menu()
        if op == 1:
            dias, descripciones, montos = cargar_datos()
        elif op == 2:
            promedio = calcular_promedio(montos)
            print("El monto promedio es:", promedio)
        elif op == 3:
            ordenar(dias, descripciones, montos)
            listar(dias, descripciones, montos)
        elif op == 4:
            mayor, cantidad = dia_mas_transportes(dias)
            print("El dia de mayor cantidad de transportes fue:", mayor)
            print("Con un total de", cantidad, "transportes realizados")


if __name__ == '__main__':
    main()
