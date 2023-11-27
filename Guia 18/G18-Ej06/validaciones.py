def validar_entre(lim_inferior, lim_superior, mensaje='Ingrese un valor: '):
    """
    Permite la carga y validación de un valor entero que debe estar en el
    intervalo cerrado [lim_inferior, lim_superior]. El método no retorna
    hasta que no se ingrese un valor correcto
    :param lim_inferior: El límite inferior a validar
    :param lim_superior: El límite superior a validar
    :param mensaje: Mensaje que se le presenta al usuario
    :return: Un valor en el rango validado
    """
    # Se carga un valor
    n = int(input(mensaje))
    # Mientras no sea correcto...
    while n < lim_inferior or n > lim_superior:
        # Se muestra un mensaje de error
        print('El valor debe estar entre', lim_inferior, 'y', lim_superior)
        # Se solicita otro valor
        n = int(input(mensaje))

    # Retorno del valor
    return n


def validar_mayor_igual(limite, mensaje='Ingrese un valor: '):
    """
    Permite la carga y validación de un valor entero que debe ser
    Mayor o igual a limite. El método no retorna hasta que no se
    ingrese un valor correcto
    :param limite: El límite a validar
    :param mensaje: Mensaje que se le presenta al usuario
    :return: Un valor en el rango validado
    """
    # Se carga un valor
    n = int(input(mensaje))
    # Mientras no sea correcto...
    while n < limite:
        # Se muestra un mensaje de error
        print('El valor debe ser mayor o igual a', limite)
        # Se solicita otro valor
        n = int(input(mensaje))
    # Retorno del valor
    return n


def validar_tarjeta(mensaje='Ingrese un número de tarjeta: '):
    """
    Permite la carga y validación de un string que representa el
    número de una tarjeta de crédito. Debe tener 16 dígitos y no
    empezar por 0
    :param mensaje: Mensaje a presentar al usuario
    :return: Un número de tarjeta validado
    """
    nro_tarjeta = input(mensaje)
    # Mientras esté mal
    while len(nro_tarjeta) != 16 or nro_tarjeta[0] < '1' or nro_tarjeta[0] > '9':
        # Se muestra un mensaje de error
        print('Número de tarjeta inválido')
        # Se solicita un nuevo número de tarjeta
        nro_tarjeta = input(mensaje)
    # Tarjeta ya validada
    return nro_tarjeta
