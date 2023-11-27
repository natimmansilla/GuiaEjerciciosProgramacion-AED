import os


def obtener_texto_procesar(archivo):
    cadena = ''
    if not os.path.exists(archivo):
        print('El archivo a procesar no existe....')
        return cadena
    
    texto = open(archivo, 'rt')
    cadena = texto.read()
    texto.close()
    return cadena


def es_digito(letra):
    return letra in '0123456789'


def principal():
    print('Primer Ejercicio de Tratamiento de Caracteres')
    print('UTLIZANDO ARCHIVOS DE TEXTO')
    print('='*80)
    
    texto = obtener_texto_procesar('./G12-Ej01b.txt')
    if len(texto) == 0:
        exit(1)

    cant_letras = 0
    palabra_digito = pal_3letras = pal_4a6letras = pal_mas6letras = pal_demitad = 0
    pos_desilaba = 0
    tiene_digitos = tiene_d = tiene_de = False
    mayor_longitud = None

    for letra in texto:
        if letra != ' ' and letra != '.':
            cant_letras += 1

            if es_digito(letra):
                tiene_digitos = True

            if letra == 'd' or letra == 'D':
                tiene_d = True
            else:
                if tiene_d and (letra == 'e' or letra == 'E'):
                    tiene_de = True
                    pos_desilaba = cant_letras
                tiene_d = False

        else:
            if cant_letras > 0:
                mitad = cant_letras // 2
                if tiene_de and pos_desilaba <= mitad:
                    pal_demitad += 1

                if tiene_digitos:
                    palabra_digito += 1

                if cant_letras <= 3:
                    pal_3letras += 1
                elif 4 <= cant_letras <= 6:
                    pal_4a6letras += 1
                else:
                    pal_mas6letras += 1

                if mayor_longitud is None or cant_letras > mayor_longitud:
                    mayor_longitud = cant_letras

            cant_letras = 0
            tiene_digitos = False
            tiene_de = False

    print('Presentacion de Resultados')
    print('-' * 80)
    print('La cantidad de palabras que contienen al menos un digito: ', palabra_digito)
    print('La cantidad de palabras que contienen hasta 3 letras es:', pal_3letras)
    print('La cantidad de palabras que contienen entre 4 y 6 letras es:', pal_4a6letras)
    print('La cantidad de palabras que contienen mas de 6 letras es:', pal_mas6letras)
    print('La cantidad de palabras con la expresion \"de\" en la primera mitad es:', pal_demitad)
    print('La palabra con la mayor longitud de letras es:', mayor_longitud)


principal()