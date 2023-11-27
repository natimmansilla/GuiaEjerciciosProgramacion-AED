from clase import *


def validar_mayor(minimo, mensaje='Ingrese un numero: '):
    numero = int(input(mensaje))
    while numero <= minimo:
        numero = int(input('Error debe ser mayor a ' + str(minimo) + '.' + mensaje))
    return numero


def validar_password():
    pwd = input('Ingrese la password del usuario: ')
    tam = len(pwd)
    while tam < 4 or tam > 10:
        pwd = input('La password no cumple la longitud, reingrese la password: ')
    return pwd


def validar_rango(minimo, maximo, mensaje='Ingrese un numero: '):
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input('Error debe ingresar un valor entre ' + str(minimo) + ' y ' + str(maximo) + '.' + mensaje))
    return numero


def cargar_usuarios(vec):
    tam = len(vec)
    for pos in range(tam):
        codigo = validar_mayor(0, 'Ingrese el codigo del del usuario: ')
        nombre = input('Ingrese el nombre del usuario: ')
        pwd = validar_password()
        depto = validar_rango(0, 19, 'Ingrese el departamento del usuario: ')
        vec[pos] = Usuario(codigo, nombre, pwd, depto)


def listar_usuarios(vector):
    linea = '{:<10}\t{:<40}\t{:<12}\n{}\n'.format('Codigo', 'Nombre', 'Departamento', ('-' * 70))
    for usuario in vector:
        linea += str(usuario)
    return linea


def usuarios_por_departamente(dominio):
    v = [0] * 20
    for usuario in dominio:
        v[usuario.departamento] += 1
    return v


def buscar(codigo, dominio):
    tam = len(dominio)
    for pos in range(tam):
        if dominio[pos].codigo == codigo:
            return pos
    return -1


def main():
    menu = 'Menu de Opciones\n' \
           '===========================================\n' \
           '1 \t Cargar usuarios\n' \
           '2 \t Listar todos los usuarios\n' \
           '3 \t Cantidad de usuarios por departamento\n' \
           '4 \t Cambiar la password de un usuario\n' \
           '5 \t Salir\n' \
           'Ingrese su opcion: '

    dominio = []
    opcion = 0
    while opcion != 5:
        opcion = int(input(menu))
        if opcion == 1:
            n = validar_mayor(0, 'Ingrese la cantidad de usuarios a cargar: ')
            dominio = [None] * n
            cargar_usuarios(dominio)
        else:
            if len(dominio) > 0:
                if opcion == 2:
                    print(listar_usuarios(dominio))
                elif opcion == 3:
                    vc = usuarios_por_departamente(dominio)
                    listado = '{:<12}\t{:<8}\n{}\n'.format('Departamento', 'Cantidad', ('-' * 25))
                    for i in range(len(vc)):
                        listado += '{:<12}\t{:<8}\n'.format('Dpto ' + str(i), vc[i])
                    print(listado)
                elif opcion == 4:
                    codigo = validar_mayor(0, 'Ingrese el codigo del usuario a buscar: ')
                    pos = buscar(codigo, dominio)
                    if pos != -1:
                        usuario = dominio[pos]
                        usuario.password = validar_password()
                    else:
                        print('No existe un usuario con el codigo', codigo)

            else:
                print('No hay usuarios cargados!!!')


if __name__ == '__main__':
    main()
