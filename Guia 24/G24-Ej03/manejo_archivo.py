__author__ = 'Algoritmos y Estructuras de Datos'

import os
import pickle

import manejo_vector
import registro


def generar_vector_pagos():
    v = []
    numero_linea = 0
    if os.path.exists('pagos.csv'):
        archivo_texto = open('pagos.csv', 'rt')
        for linea in archivo_texto:
            if numero_linea > 0:
                linea = linea[:-1]
                pago = registro.str_topago(linea)
                manejo_vector.add_in_order(v, pago)
            numero_linea += 1
        archivo_texto.close()
    return v


def grabar_archivo_texto(vector):
    m = open('pagos.csv', 'wt')
    m.write('numero,nombre,tipo_empleo,tipo_producto,monto_pagar,gastos')
    for pago in vector:
        m.write(pago.to_lineacsv())
    m.close()


def generar_archivo_binario(vector, promedio, nombre):
    m = open(nombre, 'wb')
    for pago in vector:
        neto = pago.monto_pagar - pago.gastos
        if neto > promedio and pago.tipo_producto < 3:
            pickle.dump(pago, m)
    m.close()


def mostrar_archivo_binario(nombre):
    if not os.path.exists(nombre):
        print('No existe un archivo llamado', nombre)
        return

    cad = '|{:<24} | {:<30} | {:<15} | {:<15} | {:>11} | {:>11} |\n'
    titulo = '_' * 120 + '\n'
    titulo += cad.format('Numero', 'Nombre', 'Tipo Empleo', 'Tipo Producto', 'Mto Pagar', 'Gastos')
    titulo += '_' * 120 + '\n'
    neto_total_pagar = 0

    m = open(nombre, 'rb')
    size = os.path.getsize(nombre)
    while m.tell() < size:
        pago = pickle.load(m)
        titulo += '|' + str(pago) + ' |\n'
        neto_total_pagar += pago.monto_pagar - pago.gastos
    m.close()
    titulo += '_' * 120 + '\n'
    titulo += 'El Neto Total a Pagar de Todos los Clientes fue de ${:>10.2f}\n'.format(neto_total_pagar)
    print(titulo)
