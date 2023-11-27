def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        print('Error! Debe ser un valor mayor que', inf)
        num = int(input(mensaje))
    return num


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        print('Error! Debe ser un valor entre', inf, 'y', sup)
        num = int(input(mensaje))
    return num
