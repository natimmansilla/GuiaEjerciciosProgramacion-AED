__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def calcular_porcentaje(valor, total):
    porc = 0
    if total > 0:
        porc = round(valor * 100 / total, 2)
    return porc


def es_par(numero):
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False


def test():
    print('Analisis de Secuencia 5,5')
    print('-' * 80)

    n1 = int(input('Ingrese la cota minima del intervalo a definir: '))
    n2 = int(input('Ingrese la cota maxima del intervalo a definir: '))

    cant_num_intervalo = cant_numeros = cant_secuencia_5 = 0
    hay_par_impar = False
    anterior = 0
    numero = int(
        input('Ingrese un numero de la secuencia, con cero termina: '))
    while numero != 0:
        cant_numeros += 1
        if n1 < numero < n2:
            cant_num_intervalo += 1

        if cant_numeros > 1:
            if not es_par(anterior) and es_par(numero):
                hay_par_impar = True

            if anterior == 5 and numero == 5:
                cant_secuencia_5 += 1
        anterior = numero
        numero = int(input('Ingrese otro numero de la secuencia: '))

    porc = calcular_porcentaje(cant_num_intervalo, cant_numeros)
    print('La cantidad de numeros dentro del intevalo [',
          n1, ':', n2, '] es: ', cant_num_intervalo, sep='')
    print('El porcentaje de numero en el intervalo sobre el total de numeros es: ',
          porc, '%', sep='')
    print('La cantidad de secuencia 5,5 ingresada es:', cant_secuencia_5)
    if hay_par_impar:
        print('Se ha ingreseado al menos un numero impar seguido de un par')


test()
