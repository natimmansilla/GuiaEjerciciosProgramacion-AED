def validar_mayor_que(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Valor incorrecto!")
    return n


def read(vec):
    for i in range(len(vec)):
        vec[i] = int(input("Ingrese el elemento vec["+str(i)+"]: "))


def write(vec):
    for i in range(len(vec)):
        print("Elemento", i, ":", vec[i])


def promedio(vec):
    cant = len(vec)
    acu = 0
    for i in range(cant):
        acu += vec[i]
    prom = acu / cant
    return prom


def contar_mayores(vec, prom):
    cont = 0
    for i in range(len(vec)):
        if vec[i] > prom:
            cont += 1
    return cont
