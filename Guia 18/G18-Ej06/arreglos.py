__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'


def busqueda_binaria(vec, x):
    """
    Realiza una búsqueda binaria de x en vec

    :param vec: El vector sobre el que se realiza la búsqueda
    :param x: El valor a buscar
    :return: El índice donde se encuentra x, si se encuentra,
    -1 en caso contrario
    """
    # Inicialización de los índices
    izq, der = 0, len(vec) - 1
    # Mientras no se crucen los índices
    while izq <= der:
        c = (izq + der) // 2

        if vec[c] == x:
            # El elemento se encontró
            return c

        if vec[c] < x:
            # El elemento podría estar a la derecha de c
            izq = c + 1
        else:
            # El elemento podría estar a la izquierda de c
            der = c - 1

    # No lo encontramos
    return -1


def buscar_mayor(vec):
    """
    Busca el elemento de mayor valor dentro de vec

    :param vec: El vector sobre el cuál se realiza la búsqueda
    :return: El índice donde se encuentra el mayor valor y el mayor valor
    """
    n = len(vec)  # Longitud del vector
    # Precaución por si el vector viene vacío
    if n == 0:
        return -1, None

    # Búsqueda del mayor
    indice_mayor = 0  # En principio el primer elemento
    mayor = vec[0]  # En principio el valor mayor es el primero

    # Se recorre el vector, evitando el primer elemento que ya se visitó
    for i in range(1, n):
        # Si es mayor que el mayor hasta ahora
        if vec[i] > mayor:
            # Se actualizan los valores
            indice_mayor = i
            mayor = vec[i]

    # Retorno de los valores
    return indice_mayor, mayor


def ordenar_seleccion_directa(vec):
    """
    Ordena, de menor a mayor, un vector con el algoritmo
    de selección directa.

    :param vec: El vector a ordenar
    :return: None
    """
    n = len(vec)
    # i no llega hasta el último elemento
    for i in range(n - 1):
        # j inicia a la derecha de i
        for j in range(i + 1, n):
            # Si hay que dar vuelta los valores...
            if vec[i] > vec[j]:
                vec[i], vec[j] = vec[j], vec[i]
