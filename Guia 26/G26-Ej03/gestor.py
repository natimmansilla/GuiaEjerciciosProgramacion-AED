import disco


def mostrar_vector(vec):
    for x in vec:
        print(x)


def cargar_discos():
    file = open("datos.txt", "rt")
    n = int(file.readline())
    v = [None] * n
    for i in range(n):
        titulo = file.readline().strip()
        artista = file.readline().strip()
        anio = int(file.readline())
        genero = int(file.readline())
        reproducciones = int(file.readline())
        v[i] = disco.Disco(titulo, artista, anio, genero, reproducciones)
    file.close()
    return v


def menu():
    print("1 _ Mas reproducciones")
    print("2 _ Cantidad por genero")
    print("3 _ Actualizar reproducciones")
    print("4 _ Agregar disco")
    print("5 _ Eliminar disco")
    print("6 _ Salir")
    return int(input("Ingrese opción: "))


def agregar_disco(v):
    print("Ingrese datos del disco: ")
    dis = disco.cargar_disco()
    v.append(dis)


def grabar_discos(v):
    file = open("datos.txt", "wt")
    n = len(v)
    file.write(str(n) + "\n")
    for dis in v:
        file.write(dis.titulo + "\n")
        file.write(dis.artista + "\n")
        file.write(str(dis.anio) + "\n")
        file.write(str(dis.genero) + "\n")
        file.write(str(dis.reproducciones) + "\n")
    file.close()


def eliminar_disco(v, x, y):
    for i in range(len(v)):
        if v[i].titulo == x and v[i].artista == y:
            del v[i]
            break


def disco_mas_reproducido(v):
    mayor = None
    for i in range(len(v)):
        if i == 0 or v[i].reproducciones > mayor.reproducciones:
            mayor = v[i]
    return mayor


def cantidad_por_genero(v):
    cont = [0] * 21
    for dis in v:
        cont[dis.genero] += 1
    return cont


def incrementar_reproducciones(v, x, cant):
    for dis in v:
        if dis.titulo == x:
            dis.reproducciones += cant
            break


def main():
    v = cargar_discos()
    mostrar_vector(v)
    op = 0
    while op != 6:
        op = menu()
        if op == 1:
            mayor = disco_mas_reproducido(v)
            print("El disco con mas reproducciones es: ")
            print(mayor)
        elif op == 2:
            cantidades = cantidad_por_genero(v)
            for i in range(len(cantidades)):
                if cantidades[i] != 0:
                    print("La cantidad del género", i, "es :", cantidades[i])
        elif op == 3:
            x = input("Ingrese titulo: ")
            cant = int(input("Ingrese nueva cantidad de reproducciones: "))
            incrementar_reproducciones(v, x, cant)
        elif op == 4:
            agregar_disco(v)
        elif op == 5:
            x = input("Ingrese titulo: ")
            y = input("Ingrese artista: ")
            eliminar_disco(v, x, y)
        elif op == 6:
            grabar_discos(v)


if __name__ == '__main__':
    main()
