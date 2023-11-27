__author__ = 'Algoritmos y Estructuras de Datos'

import os

import registro


def generar_arreglo():
    """
    Funcion que procesa un archivo si existe, leyendo linea por linea, para armar un registro
    y agregarlo a un arreglo
    :return: el arreglo de los registros leidos del archivo
    """

    v = []
    if os.path.exists('alquileres.csv'):
        m = open('alquileres.csv', 'rt')
        lineas = m.readlines()[1:]
        for linea in lineas:
            alquiler = registro.str_toalquiler(linea)
            v.append(alquiler)
        m.close()
    return v


def grabar_arreglo(vector):
    """
    Por cada registro que tengo en el vector, convertilos a una linea de texto y
    grabarlo
    :param vector:
    :return:
    """
    m = open('alquileres.csv', 'wt')
    m.write('numero,nombre,personas,tipo,monto,dias')
    for alquiler in vector:
        linea = alquiler.to_lineascsv()
        m.write(linea)
    m.close()
