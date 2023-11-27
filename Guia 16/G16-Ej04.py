def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        num = int(input('Error!' + mensaje))
    return num


def buscar_secuencial(v, x):
    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1


def principal():
    print('CREACIÓN DE USUARIOS')
    n = validar_mayor_que(0, 'Ingrese cantidad de usuarios: ')
    v = list()
    for i in range(n):
        nombre = input('Ingrese nombre de usuario: ')
        while buscar_secuencial(v, nombre) != -1:
            nombre = input('Ya existe! Ingrese otro: ')
        v.append(nombre)
    print('\nUsuarios:', v)


if __name__ == '__main__':
    principal()