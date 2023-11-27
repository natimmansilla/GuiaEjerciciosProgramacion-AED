__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'


def validate(inf, msg='Ingrese un valor.'):
    n = inf
    while n <= inf:
        n = int(input(msg + ' Valor superior a ' + str(inf) + ', por favor: '))
        if n <= inf:
            print('Error. Valor Incorrecto!')
    return n


def validate_range(inf, sup, msg='Ingrese un valor.'):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(msg + ' Comprendido en [' + str(inf) + ':' + str(sup) + '], por favor: '))
        if n < inf or (n > sup):
            print('Error. Valor Incorrecto!')
    return n


def read(v, inf, sup, msg):
    for i in range(len(v)):
        v[i] = validate_range(inf, sup, msg)


def pto_1(codigos, importes):
    aux = [0] * 5
    for i in range(len(codigos)):
        indi = codigos[i] % 5
        aux[indi] += importes[indi]
    return aux


def pto_2(codigos):
    aux = [0] * 20
    for i in range(len(codigos)):
        aux[codigos[i] - 1] += 1
    may = aux[0]
    may_cod = 1
    for i in range(1, 20):
        if aux[i] > may:
            may, may_cod = aux[i], i + 1
    return may, may_cod


def test():
    n = validate(0, 'Ingrese cantidad de multas.')
    infracciones = [None] * n
    importes = [None] * 5

    # Cargar los n códigos de infracción labrados
    read(infracciones, 1, 20, 'Ingrese un código de infracción.')

    # Cargar los 5 importes correspondientes a los tipos de infracciones
    read(importes, 1, 50000, 'Ingrese un importe en pesos.')

    # Generar un tercer vector con los Importes totales facturados por tipo de infracción
    totales = pto_1(infracciones, importes)
    print('Totales facturados por tipo:')
    for i in range(5):
        if totales[i] != 0:
            print('Tipo ' + str(i) + ': ' + str(totales[i]), ' pesos.')

    # Determinar el código de infracción que más apareció en las multas y la cantidad de multas labradas para dicho código.
    cod, cant = pto_2(infracciones)
    print('Código de infracción más frecuente: ' + str(cod) + ', con ' + str(cant), ' multas.')
    # Informar el importe total facturado durante el fin de semana.
    acu = 0
    for i in range(5):
        acu += totales[i]
    print('Importe total facturado durante el fin de semana: ' + str(acu) + ' pesos.')


if __name__ == '__main__':
    test()

