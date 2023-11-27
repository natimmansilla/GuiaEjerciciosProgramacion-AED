__author__ = 'Algoritmos y Estructuras de Datos'

def validate(mensaje):
    n = 0
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print("Valor incorrecto!")
    return n

def validate_range(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Ingrese el tipo de artículo, entre "+ str(inf) + " y " + str(sup) + ": "))
        if n < inf or n > sup:
            print("Valor incorrecto!")
    return n

def read(art, cant):
    for i in range(len(art)):
        print("Venta", i)
        art[i] = validate_range(0, 3)
        cant[i] = validate("Ingrese la cantidad vendida de dicho articulo: ")

def write(art, cant):
    for i in range(len(art)):
        print("Venta:", i)
        print("Artículo:", art[i], "- Cantidad:", cant[i])

def contar(art, cant):
    acu = [0] * 4
    for i in range(len(art)):
        acu[art[i]] += cant[i]

    print("\nCantidades vendidas por artículo")
    for i in range(len(acu)):
        print("Cantidad vendida del articulo", i, ":", acu[i])

def test():
    n = validate("Ingrese la cantidad de ventas del día: ")
    art = [0] * n
    cant = [0] * n
    read(art, cant)
    write(art, cant)
    contar(art, cant)


if __name__ == "__main__":
    test()