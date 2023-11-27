__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def obtener_provincia(linea):
    if 'CO' in linea:
        return 'Córdoba'
    elif 'BA' in linea:
        return 'Buenos Aires'
    elif 'SF' in linea:
        return 'Santa Fé'
    else:
        return 'Entre Ríos'


def es_digito_impar(caracter):
    return caracter == '1' or caracter == '3' or caracter == '5' or caracter == '7' or caracter == '9'


def es_digito(caracter):
    return '0' <= caracter <= '9'


def es_vocal(caracter):
    return caracter in 'aeiouAEIOU'


def contar_cuenta(cuenta):
    resp = False
    tiene_dig_impar = True
    tiene_k = False
    cant_vocales = 0

    # Agrego el punto para finalizar correctamente el texto y considerar el ultimo caracter
    if cuenta[-1] != '.':
        cuenta += '.'

    for letra in cuenta:
        if letra != '.' and letra != ' ':
            if letra == 'K':
                tiene_k = True

            elif es_vocal(letra):
                cant_vocales += 1

            elif es_digito(letra) and not es_digito_impar(letra):
                tiene_dig_impar = False
        else:
            if (tiene_k or cant_vocales == 2) and tiene_dig_impar:
                resp = True

    return resp


def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total

    return round(porcentaje, 2)


def principal():
    linea = ''
    texto = open('cobros.txt', 'rt')

    primer_linea = True
    cant_tipo_cobro_0 = cant_tipo_cobro_1 = cant_tipo_cobro_2 = 0
    cant_cobros = cant_cobros_local = 0
    total_cobrado = 0
    cantidad_cuentas = 0

    for linea in texto:
        if primer_linea:
            provincia = obtener_provincia(linea)
            primer_linea = False
        else:
            cant_cobros += 1
            fecha_cobro = linea[0:8]
            tipo_cobro = int(linea[8])
            monto = float(linea[9:16])
            cuenta = linea[16:27]
            local = int(linea[27])

            if tipo_cobro == 0:
                cant_tipo_cobro_0 += 1
                mes = int(fecha_cobro[4:6])
                if mes == 7 or mes == 8:
                    total_cobrado += monto

            elif tipo_cobro == 1:
                cant_tipo_cobro_1 += 1
            elif tipo_cobro == 2:
                cant_tipo_cobro_2 += 1

            if contar_cuenta(cuenta):
                cantidad_cuentas += 1

            if local <= 7:
                cant_cobros_local += 1

    print('La provincia que emitio el reporte de cobros es:', provincia)
    print('La Cantidad de cobros para el tipo 0 fueron de:', cant_tipo_cobro_0)
    print('La Cantidad de cobros para el tipo 1 fueron de:', cant_tipo_cobro_1)
    print('La Cantidad de cobros para el tipo 2 fueron de:', cant_tipo_cobro_2)
    print('El monto total recaudado en los meses de Julio y Agosto para el tipo de cobro 0 es:', total_cobrado)
    print('La cantidad de cuentas con dos vocales o la letra "K" y solo digitos impares son:', cantidad_cuentas)
    porcentaje = calcular_porcentaje(cant_cobros_local, cant_cobros)
    print('El Porcentaje que representan los cobros de los locales menores o iguales a 7 es:', porcentaje, '%')


principal()
