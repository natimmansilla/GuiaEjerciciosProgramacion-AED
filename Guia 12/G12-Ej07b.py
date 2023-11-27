__author__ = 'Cátedra de Algorítmos y Estructuras de datos'


def calcular_porcentaje(muestras, total):
    """
    Calcula el porcentaje que representan las muestras en el total
    :param muestras: La cuenta de muestras
    :param total: El total sobre el que se contaron las muestras
    :return: El porcentaje que representan las muestras en el total si total es distinto a 0.
    0 en caso contrario
    """
    porcentaje = 0
    if total != 0:
        porcentaje = (muestras * 100) / total
    return porcentaje


def es_vocal(caracter):
    """
    Comprueba si un caracter es una vocal o no
    :param caracter: El caracter que se quiere comprobar
    :return: True si es una vocal, False si no lo es
    """
    vocales = 'aeiouáéíóú'  # Vocales (en minúsculas)
    for vocal in vocales:
        if caracter == vocal:
            return True

    return False


def es_digito(caracter):
    """
    Comprueba si un caracter es un dígito o no
    :param caracter: El caracter a comprobar
    :return: True si es un dígito, False en caso contrario
    """
    if caracter >= '0' and caracter <= '9':
        return True
    return False


def main():
    """
    Función principal del programa. Toda la lógica del mismo está contemplada aquí
    :return: None
    """
    ####################################################################################################################
    # Variables Generales (Variables que no se van a reiniciar, son los resultados del programa)                       #
    ####################################################################################################################
    cont_palabras = 0  # Contador de palabras del texto
    # Punto 1
    cont_punto_1 = 0  # Contador de Palabras con 3 vocales
    # Punto 2
    cont_punto_2 = 0  # Contador de palabras con dígitos y más de 4 caracteres
    # Punto 3
    cant_caracteres_menor = None  # Cantidad de carac. de la menor palabra que termina con la primera letra del texto
    pos_menor_palabra = None  # Posición de la palabra con menos carc. entre las que termina con la primera letra
    # Punto 4
    cont_punto_4 = 0  # Contador de palabras que contienen 'men' en la primera mitad de la palabra

    ####################################################################################################################
    # Variables por palabra (Variables que tienen sentido palabra por palabra, se reinician ante un serparador)        #
    ####################################################################################################################
    cont_letras_palabra = 0  # Contador de letras de la palabra que se está analizando
    # Punto 1
    cont_vocales_palabra = 0  # Contador de vocales de la palabra que se está analizando
    # Punto 2
    b_tiene_digito = False  # Bandera que indica si una palabra tiene o no un dígito entre sus caracteres
    # Punto 4
    b_m = b_me = False      # Banderas que indican si se vió una 'm' o si se vió 'me'
    b_tiene_men = False     # Bandera que indica si se encontró 'men' en la palabra
    pos_silaba_men = 0      # Posición en la que termina la sílaba 'men' si se la encontró en la palabra

    # Carga del texto
    texto = input('Ingrese texto: (Terminar con "."): ')
    # Conversión a minúsculas (Notar que esto no sirve si el enunciado solicita discriminar mayúsculas y minúsculas)
    texto = texto.lower()

    # Recorrido de la cadena
    for car in texto:

        if car != ' ' and car != '.':
            # De este lado, estamos dentro de una palabra
            cont_letras_palabra += 1

            # Para el punto 1 -> Contar vocales
            if es_vocal(car):
                cont_vocales_palabra += 1
            else:
                # Para el punto 2 -> ver si es un dígito. Notar que esto está en el else.
                # Esto es así, porque si es una vocal, no va a ser un dígito...
                if es_digito(car):
                    b_tiene_digito = True

            # Para el punto 3 -> determinar la primera letra del el texto. Para que se la primera
            # letra del texto, debe ser la primera palabra y el primer caracter de esa palabra.
            if cont_palabras == 0 and cont_letras_palabra == 1:
                primera_letra = car

            # Para el punto 4 -> Determinar si se encuentra 'men' y en qué posición de la palabra
            if car == 'm' and not b_tiene_men:
                # Si se encuentra una 'm' y todavía no se encontró 'men' en la palabra...
                b_m = True
            else:
                # Si se trata de una 'e' y en el caracter anterior se vió una 'm'
                if car == 'e' and b_m:
                    # Si entramos aquí, ya vimos 'me'
                    b_me = True
                else:
                    # Si vemos 'n' y teníamos 'me'
                    if car == 'n' and b_me:
                        # Entonces, vimos 'men'
                        b_tiene_men = True
                        # Pero también nos interesa la posición donde determinamos que vimos 'men'
                        pos_silaba_men = cont_letras_palabra
                    # Se baja la bandera b_me, para evitar que quede levantada si hemos visto 'me'
                    # pero no 'men'
                    b_me = False
                # Se baja la bandera b_m. Esto es para evitar que quede levantada la bandera cuando
                # no se vió 'me'
                b_m = False

            # Para el punto 3 -> se almacena el último caracter, para saber con qué termina la palabra.
            # Se hace al final del if por una cuestión de orden, en este caso pudo estar antes
            ultimo_car = car

        else:
            # En esta rama, estamos ante la posible terminación de una palabra
            if cont_letras_palabra > 0:
                # Únicamente se cuenta una palabra (y se la procesa) si consta de más de un caracter
                cont_palabras += 1

                # Para el punto 1 -> Si tiene exactamente 3 vocales, se la cuenta
                if cont_vocales_palabra == 3:
                    cont_punto_1 += 1

                # Para el punto 2 -> Si tiene un dígito y más de 4 letras
                if b_tiene_digito and cont_letras_palabra > 4:
                    cont_punto_2 += 1

                # Para el punto 3 -> Si termina con la primera letra del texto
                if ultimo_car == primera_letra:
                    # Pero como piden saber, dentro de todas las palabras que terminan con la primera letra
                    # del texto, cuál es la posición de la de menor cantidad de caracteres...
                    if cant_caracteres_menor is None or cont_letras_palabra < cant_caracteres_menor:
                        # Como en cualquier búsqueda de menor, nos quedamos con la cantidad de caracteres
                        # y la posición de la palabra (que es lo que nos piden)
                        cant_caracteres_menor = cont_letras_palabra
                        pos_menor_palabra = cont_palabras

                # Para el punto 4 -> Si contiene 'men' en la primera mitad de la palabra
                if b_tiene_men and pos_silaba_men <= (cont_letras_palabra / 2):
                    cont_punto_4 += 1

            # Reseteo de las variables que tienen que ver con cada palabra
            cont_letras_palabra = 0
            cont_vocales_palabra = 0
            b_tiene_digito = False
            pos_silaba_men = 0
            b_tiene_men = False

    # Terminó el for, aquí se procesan los resultados
    porc_punto_2 = calcular_porcentaje(cont_punto_2, cont_palabras)
    print('=============================== RESULTADOS ==============================')
    print('Total de palabras procesadas: ', cont_palabras)
    print('1) Cantidad de palabras con 3 vocales: ', cont_punto_1)
    print('2) Procentaje de palabras con algún dígito y más de 4 letras: ', round(porc_punto_2, 2))
    if pos_menor_palabra is not None:
        print('3) Posición de la menor palabra que termina con la primera letra del texto: ', pos_menor_palabra)
    else:
        print('3) No hubo palabras que terminasen con la primera letra del texto')
    print('4) La cantidad de palabras que contienen "men" en la primera mitad de la palabra es: ', cont_punto_4)


if __name__ == '__main__':
    main()