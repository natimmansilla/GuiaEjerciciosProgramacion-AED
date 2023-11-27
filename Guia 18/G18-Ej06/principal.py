import random
import arreglos
import validaciones


def convertir_codigo_a_marca(codigo):
    """
    Convierte el código de marca a la
    descripción de la misma

    :param codigo: El código de marca
    :return: La descripción de la marca
    """
    # Todas las descripciones de las marcas soportadas
    descripciones = (
        "Vusa", "American Slow", "MaterCard",
        "Tarjeta Pomelo", "Launcher's club", "JNoCB",
        "AsiaPay", "Undiscovered Card", "AED Card"
    )
    # Por defecto, la marca sería desconocida
    marca = "Desconocida"
    # Si está en el rango válido...
    if 1 <= codigo <= len(descripciones):
        return descripciones[codigo - 1]
    # Se devuelve la marca que corresponde al código
    return marca


def generar_tarjetas_bloqueadas(n):
    """
    Genera un vector con strings representando números de
    tarjeta aleatorios válidos (16 dígitos, no comienzan en 0).
    Y lo devuelveordenado.

    *********************** ATENCION ****************************
    NO es buena idea ordenar un vector para hacer unas pocas
    búsquedas. El costo de ordenamiento con una algoritmo de
    selección directa (como el que se implementa aquí) es
    altísimo.

    Para ESTE ejercicio en particular, donde se simula que el
    vector se ordena una única vez y se busca muchísimas veces
    sobre él, y donde el enunciado dice explícitamente que la
    lista se tiene ya ordenada, se realiza el ordenamiento luego
    de la creación
    *************************************************************

    :param n: La cantidad de tarjetas que se quieren en la lista
    :return: Un vector ORDENADO de menor a mayor con n tarjetas
    """
    lista_bloqueadas = [''] * n
    # Se generan los valores
    for i in range(n):
        # No es válido que inicie con cero
        lista_bloqueadas[i] = str(random.randint(1000000000000000, 9999999999999999))

    # Se ordena el vector (leer el comentario)
    arreglos.ordenar_seleccion_directa(lista_bloqueadas)
    # Se devuelve el vector
    return lista_bloqueadas


def cargar_lote_pagos(n):
    """
    Crea un vector con n pagos realizados, solicitándole
    al usuario los números de tarjeta de los pagos

    :param n: La cantidad de pagos a cargar
    :return: un vector con n pagos cargados
    """
    vec = [None] * n
    # Ya se creó el vector con valores None, ahora se le carga un
    # valor a cada elemento
    for i in range(n):
        vec[i] = validaciones.validar_tarjeta("Ingrese Nro. Tarjeta: ")

    # Retorno del vector
    return vec


def calcular_rechazos_por_marca(lote_pagos, tarjetas_bloqueadas):
    """
    Calcula la cantidad de pagos rechazados, discriminado por "marca"
    de tarjeta. La discriminación se realiza de acuerdo al primer
    dígito del número de tarjeta. Por ejemplo:
    La tarjeta 4203688416671910, tiene por primer dígito a 4, que
    corresponde a "Tarjeta Pomelo".
    Como las marcas de tarjeta van de 1 a 9, pero los índices del vector
    de 0 a 8, se resta 1 para colocarlo en el casillero correcto

    :param lote_pagos: El lote de pagos a verificar
    :param tarjetas_bloqueadas: El vector de tarjetas bloqueadas
    :return: Un vector contando los rechazos por cada marca.

    Por ejemplo:
    Si en el lote se rechazan
        * 3 tarjetas "Vasa (Cod. 1)",
        * 2 tarjetas "Tarjeta Pomelo (Cod. 4)" y
        * 5 tarjetas "Tarjeta AED (9)"
    El retorno será:
                -------------------------------------
    Valores:    | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 5 |
                -------------------------------------
    Índices:      0   1   2   3   4   5   6   7   8

    """
    vec_rechazos_por_marca = [0] * 9
    # Recorrer el lote de pagos
    for i in range(len(lote_pagos)):  # pudo ser for tarjeta in lote_pagos:
        # Uno de los pagos a procear
        tarjeta = lote_pagos[i]
        # Revisar si está bloqueada
        if arreglos.busqueda_binaria(tarjetas_bloqueadas, tarjeta) != -1:
            # Este print no es necesario, ni se pondrían en un
            # Software real, está puesto para ver el procesamiento
            print('Tarjeta:', tarjeta, 'BLOQUEADA')

            # Se obtiene el código de marca de ese número de tarjeta
            cod_marca = int(tarjeta[0])

            # Contamos un rechazo para la marca cod_marca
            vec_rechazos_por_marca[cod_marca - 1] += 1
        else:
            # Este print no es necesario, ni se pondrían en un
            # Software real, está puesto para ver el procesamiento
            print('Tarjeta:', tarjeta, 'NO Bloqueada')

    # Retorno del vector
    return vec_rechazos_por_marca


def mostrar_rechazos_por_marca(rechazos_marca):
    """
    Muestra el vector de rechazos por marca, pero
    convirtiendo el código a la descripción de la
    marca de la tarjeta

    :param rechazos_marca: El vector con los contadores de rechazo
    :return: None
    """
    # Se recorre el vector
    for i in range(len(rechazos_marca)):
        # El código de marca, es el índice + 1.
        # índice 0 -> código 1 -> Marca "Vasa"
        cod_marca = i + 1
        # Se muestran los rechazos
        print(convertir_codigo_a_marca(cod_marca), '\t\t\t\t-->', rechazos_marca[i])


def emitir_reporte_rechazos(lote_pagos, tarjetas_bloqueadas):
    # Cálculo de los rechazos por cada "marca" de tarjeta
    rechazos_por_marca = calcular_rechazos_por_marca(lote_pagos, tarjetas_bloqueadas)
    # Se muestra el vector de rechazos
    print('Rechazos por marca: \n')
    mostrar_rechazos_por_marca(rechazos_por_marca)

    # Nos piden la marca de tarjeta menos segura. Esto sería, aquella que
    # tuvo mayor cantidad de rechazos (para nuestro ejemplo). Con lo cual
    # El problema se traduce en buscar, dentro del vector de rechazos por marca,
    # Aquel con el contador mayor
    indice, mayor = arreglos.buscar_mayor(rechazos_por_marca)
    cod_marca = indice + 1
    # Se muestra el resultado
    if mayor > 0:
        print('La marca menos segura es:', convertir_codigo_a_marca(cod_marca), 'con', mayor, 'rechazos')
    else:
        print('No hubo rechazos de ninguna marca')


def main():
    """
    Función principal del programa, maneja el menú e
    invoca a las funciones necesarias para resolver
    cada punto del problema.

    :return: None
    """

    lote_pagos = None
    b_lote_cargado = False  # Indica si ya se cargó el lote de pagos

    # Carga de la lista de tarjetas bloqueadas (Para pruebas, 30 está OK)
    tarjetas_bloqueadas = generar_tarjetas_bloqueadas(30)

    op = -1  # Opción para forzar el ingreso al menú
    # Mientras la opción no sea salir...
    while op != 0:
        # Se presenta el menú
        print('=========== MENÚ DE OPCIONES ===========\n'
              '1) Cargar Lote de Pagos\n'
              '2) Mostrar Lista de Bloqueadas\n'
              '3) Mostrar lote de transacciones\n'
              '4) Informe de rechazos por marca\n'
              '0) Salir')

        # Se solicita el ingreso de la opción, no hace falta validarla con una función
        # porque el procesamiento de las opciones ya filtra las opciones inválidas
        op = int(input('Seleccione Opción: '))

        # Procesamiento de las opciones
        if op == 1:  # Cargar Lote de transacciones
            # Pedir al usuario la cantidad de pagos a cargar
            n = validaciones.validar_mayor_igual(1, "Ingrese cantidad de pagos: ")
            # Generación del vector con los pagos
            lote_pagos = cargar_lote_pagos(n)
            # Se indica que ya se generó el lote
            b_lote_cargado = True

        elif op == 2:  # Mostrar Lista de Bloqueadas
            # Se podría hacer una función para mostrar las tarjetas de manera
            # más prolija
            print('Tarjetas Bloqueadas: \n', tarjetas_bloqueadas)

        elif 3 <= op <= 4:
            if b_lote_cargado:
                if op == 3:  # Mostrar lote de transacciones
                    # Se podría hacer una función para mostrar las tarjetas de manera
                    # más prolija
                    print('Lote de Pagos: \n', lote_pagos)

                elif op == 4:  # Informe de rechazos por marca
                    emitir_reporte_rechazos(lote_pagos, tarjetas_bloqueadas)
            else:

                # Aún no se cargó un lote de transacciones, no se debe continuar
                # con las subsiguientes opciones
                print('Todavía no cargó el lote de transacciones')

        elif op == 0:
            print('Hasta luego!')

        else:
            # Si la opción no es ninguna de las válidas...
            print('Opción inválida!')


# Script principal
if __name__ == '__main__':
    main()
