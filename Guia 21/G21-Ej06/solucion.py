__author__ = "Cátedra de Algoritmos y Estructuras de Datos"


def cargar_matriz(f, c):
    mat = [[0] * c for i in range(f)]
    for i in range(f):
        for j in range(c):
            print("Ingrese fila {0}, columna {1}".format(i, j), end=" ")
            mat[i][j] = int(input())
    return mat


def suma_todo(mat):
    suma = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            suma += mat[i][j]
    return suma


def suma_por_filas(mat):
    f = len(mat)
    suma = [0] * f
    for i in range(f):
        for j in range(len(mat[i])):
            suma[i] += mat[i][j]
    return suma


def suma_por_columnas(mat):
    c = len(mat[0])
    suma = [0] * c
    for i in range(len(mat)):
        for j in range(c):
            suma[j] += mat[i][j]
    return suma


def suma_contorno(mat):
    f = len(mat)
    c = len(mat[0])
    suma = 0
    for i in range(f):
        suma += mat[i][0] + mat[i][c - 1]
    for j in range(1, c - 1):
        suma += mat[0][j] + mat[f - 1][j]
    return suma


def suma_mitad_arriba(mat):
    f = len(mat)
    suma = 0
    for i in range(f // 2):
        for j in range(len(mat[i])):
            suma += mat[i][j]
    return suma


def suma_esquina_inferior_derecha(mat):
    f = len(mat)
    c = len(mat[0])
    suma = 0
    for i in range(f // 2, f):
        for j in range(c // 2, c):
            suma += mat[i][j]
    return suma


def principal():
    f = int(input("Ingrese cantidad de filas"))
    c = int(input("Ingrese cantidad de columnas"))

    matriz = cargar_matriz(f, c)
    print("Suma de todo", suma_todo(matriz))
    print("Suma por filas", suma_por_filas(matriz))
    print("Suma por columnas", suma_por_columnas(matriz))
    print("Suma del contorno", suma_contorno(matriz))
    print("Suma mitad de arriba", suma_mitad_arriba(matriz))
    print("Suma de la esquina", suma_esquina_inferior_derecha(matriz))


if __name__ == "__main__":
    principal()
