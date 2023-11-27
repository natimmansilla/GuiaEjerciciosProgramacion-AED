__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def es_vocal(car):
    vocales = 'aeiouAEIOU'
    if car in vocales:
        return True
    else:
        return False


def es_consonante(car):
    consonantes = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
    if car in consonantes:
        return True
    else:
        return False


def calcular_porcentaje(cant,total):
    if total == 0:
        return 0
    else:
        return cant * 100 / total