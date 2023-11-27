import random
from trafico import *


def validar_mayor_cero(mensaje='Ingrese un valor: '):
    numero = 0
    while numero <= 0:
        numero = int(input(mensaje))
        if numero <= 0:
            print('Incorrecto!!!! El valor debe ser mayor a cero.')
    return numero


def cargar_datos(direcciones):
    ip_origen = random.choice(direcciones)
    ip_destino = random.choice(direcciones)
    num_bytes = random.randint(1024, 92160)
    return Trafico(ip_origen, ip_destino, num_bytes)


def cargar(n, direcciones):
    v = n * [None]
    for i in range(n):
        v[i] = cargar_datos(direcciones)
    return v


def principal():
    print('Analisis de Trafico de Red')
    print('=' * 80)

    direcciones = ('124.43.5.120','124.43.5.12','124.43.5.20','124.43.5.10','124.43.5.2','124.43.5.80',
                   '124.43.5.240','124.43.5.35','124.43.5.45')
    ip_total_envio = random.choice(direcciones)
    ip_porcentaje = random.choice(direcciones)

    total_bytes = cantidad = cant_rec_ip = total = 0
    menor = None

    n = validar_mayor_cero('Ingrese la cantidad de registros a procesar: ')
    v = cargar(n, direcciones)

    for info in v:
        total += info.tamanio
        cantidad += 1

        if ip_total_envio == info.direccion_origen:
            total_bytes += info.tamanio

        if ip_porcentaje == info.direccion_destino:
            cant_rec_ip += 1

        if menor is None or menor.tamanio > info.tamanio:
            menor = info

    porcentaje = 0
    if cantidad > 0:
        porcentaje = cant_rec_ip * 100 / cantidad

    print('=' * 80)
    print('Visualización de resultados')
    print('_' * 80)
    print('El total de información enviada por la máquina', ip_total_envio, 'fue de', total_bytes, 'bytes')
    print(menor)
    print('La máquina', ip_total_envio, 'recibió un', round(porcentaje, 2), '% del total del tráfico de bytes')


if __name__ == '__main__':
    principal()
