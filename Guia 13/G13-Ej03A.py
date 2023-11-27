__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

def es_vocal(letra):
    vocales = ('a', 'e', 'i', 'o', 'u')
    return letra in vocales


def leer_texto():
    texto = input('Ingrese el texto (termina con "." y las plabras se separan por espacio)\n')
    while texto[-1] != '.':
        print('Error: el texto debe terminar con "."')
        texto = input('Ingrese el texto (termina con "." y las plabras se separan por espacio)\n')
    texto = texto.lower()
    return texto


def leer_entero_en_rango(lim_inferior, lim_superior, mensaje):
    resp = int(input(mensaje))
    while resp < lim_inferior or resp > lim_superior:
        print('Error: el numero debe estar entre ' + str(lim_inferior) + ' y ' + str(
            lim_superior) + ', vuelva a intentarlo.')
        resp = int(input(mensaje))

    return resp


def mostrar_menu():
    print('*' * 40)
    print('       Procesador de Textos')
    print('       Opciones:')
    print('*' * 40)
    print(' 1 - Cargar el Texto')
    print(' 2 - Mostrar el promedio de letras por palabra del texto')
    print(' 3 - Cantidad de palabras terminadas en vocal')
    print(' 4 - Orden de la palabra más larga')
    print(' 5 - Cantidad de palabras que contienen l + <vocal>')
    print(' 6 - Salir')


def pausa():
    input('\n\nPresione enter para continuar...\n')


def test():
    # Inicialización de contadores y acumuladores Generales
    texto_cargado = False
    acumulador_letras = 0
    contador_palabras = 0
    cont_pal_term_vocal = 0
    cont_pal_l_vocal = 0
    orden_mas_larga = 0
    letras_mas_larga = 0

    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = leer_entero_en_rango(1, 6, 'Ingrese su opción: ')

        if opcion == 1:  # Cargar el texto

            # Inicializaciones
            contador_letras = 0
            ultima_letra = ' '
            vino_l = False
            vino_l_vocal = False

            texto = leer_texto()

            for car in texto:
                if car != ' ' and car != '.':  # Por verdadero estoy procesando las letras dentro de una palabra
                    # Cuento las letras de la palabra
                    contador_letras += 1
                    # Me guardo cada letra para tener la última cuando la palabra termine
                    ultima_letra = car

                    # Detecto si vino l + vocal
                    if car == 'l':
                        vino_l = True
                    else:
                        if vino_l and es_vocal(car):
                            vino_l_vocal = True
                        vino_l = False
                else:  # Por el falso esto al final de una palabra (o entre 2 palabras, parado en el espacio)
                    # Cuento las palabras
                    contador_palabras += 1

                    # Acumulo las letras para tener el total de letras para el promedio
                    acumulador_letras += contador_letras

                    # Cuentos las palabras con la última letra vocal
                    if es_vocal(ultima_letra):
                        cont_pal_term_vocal += 1

                    # Chequeo si la palabra anterior fue más larga y guardo los datos si asi fuera
                    if contador_palabras == 1 or contador_letras > letras_mas_larga:
                        letras_mas_larga = contador_letras
                        orden_mas_larga = contador_palabras

                    # Cuento las palabras con l + vocal
                    if vino_l_vocal:
                        cont_pal_l_vocal += 1

                    # Vuelvo al inicio los contadores y banderas para la próxima palabra
                    contador_letras = 0
                    vino_l = False
                    vino_l_vocal = False

            print('\n\nTexto procesado correctamente...\n\n')
            texto_cargado = True
            pausa()

        elif opcion == 6:  # Chau
            print('Gracias por usar el Procesador de Textos!!!')
            print('Fin!.')

        else:
            if texto_cargado:
                if opcion == 2:  # Mostrar promedio
                    if contador_palabras > 0:
                        promedio = acumulador_letras / contador_palabras
                    else:
                        promedio = 0
                    print('El promedio de letras por palabra fue:', promedio)
                    pausa()
                elif opcion == 3:  # Mostrar terminadas en vocal
                    print('La cantidad de palabras terminadas en vocal fue:', cont_pal_term_vocal)
                    pausa()
                elif opcion == 4:  # Mostrar terminadas en vocal
                    print('La ', orden_mas_larga, '° fue la palabra más larga, y tuvo ', letras_mas_larga, ' letras',
                          sep='')
                    pausa()
                elif opcion == 5:  # Mostrar terminadas en vocal
                    print('La cantidad de palabras que incluyeron "l + <vocal>" fue:', cont_pal_l_vocal)
                    pausa()
            else:
                print('Debe cargar el texto primero ingresando a la opción 1')
                pausa()


test()
