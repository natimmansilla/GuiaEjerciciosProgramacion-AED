# NO HAY campo de marcado lógico en este ejercicio, porque no está prevista
# la operación de baja o eliminación. Los autos se venden y se registran como
# vendidos, pero los registros no se eliminan.

from auto import *
import io
import os
import pickle
import os.path


def buscar(fd, m, p):
    """Busca un registro cuya patente coincida con p en el archivo de automoviles.

    Si lo encuentra, retorna su posición (como número de byte). Si no lo encuentra, retorna
    el valor -1.

    :param fd: El file descriptor del archivo donde se debe buscar.
    :param m: El manejador del archivo donde se debe buscar.
    :param p: La patente a buscar.
    :return la posición de byte donde fue encontrado el registro.
    """
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        aut = pickle.load(m)
        if aut.patente == p:
            posicion = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def alta(fd):
    """Agrega el registro de un automovil al archivo.

    Los datos del automovil se toman por teclado. El registro será grabado sólo si el
    archivo no contenía ya un automovil con la misma patente.

    :param fd: El file descriptor del archivo donde se debe buscar.
    """
    m = open(fd, 'a+b')

    patente = input('Patente del auto a registrar (cargue 0 para salir): ')
    while patente != '0':
        # buscamos el registro con esa patente...
        pos = buscar(fd, m, patente)

        if pos == -1:
            # no estaba repetido... lo cargamos por teclado...
            modelo = int(input('Modelo: '))
            aut = Auto(patente, modelo)

            # ...lo grabamos...
            pickle.dump(aut, m)

            # ...y volcamos el buffer de escritura
            # para que el sistema operativo REALMENTE
            # grabe en disco el registro...
            m.flush()

            print('Registro grabado en el archivo...')

        else:
            print('Patente repetida... alta rechazada...')

        patente = input('Otra patente (cargue 0 para salir): ')

    print()
    print('Los nuevos registros han sido grabados...')
    input('Presione  para seguir...')
    m.close()


def modificacion(fd):
    """Modifica el contenido de un registro de un automovil del archivo.

    Solo se permitira modificar el estado de un automovil a no dispobible.
    :param fd: El file descriptor del archivo donde se debe buscar.
    """
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    patente = input('Patente del automovil a modificar su estado (cargue 0 para salir): ')
    while patente != '0':
        # buscamos el registro con esa patente...
        pos = buscar(fd, m, patente)

        if pos != -1:
            # encontrado... procedemos a cargarlo...
            m.seek(pos, io.SEEK_SET)
            aut = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            print(aut)

            if aut.estado == 0:
                print('El automovil ya fue VENDIDO')
            else:
                aut.estado = 0

                # ...registro modificado en memoria...
                # ...ahora nos volvemos a su posición en el archivo...
                m.seek(pos, io.SEEK_SET)

                # ...y volvemos a grabar el registro modificado...
                pickle.dump(aut, m)

                print()
                print('El automovil cambio su estado a VENDIDO...')

        else:
            print('Ese registro no existe en el archivo...')

        input('Presione  para seguir...')
        patente = input('Otra patente a modificar su estado (cargue 0 para salir): ')

    m.close()


def listado_completo(fd):
    """Muestra el contenido completo del archivo.

    :param fd: El file descriptor del archivo donde se debe buscar.
    """
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    print('Listado general de automoviles registrados:')
    while m.tell() < tbm:
        aut = pickle.load(m)
        print(aut)

    m.close()

    print()
    input('Presione  para seguir...')


def listado_filtrado(fd):
    """Muestra los registros de los auto con modelo mayor a m.

    :param fd: El file descriptor del archivo donde se debe buscar.
    """
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)
    m = open(fd, 'rb')
    modelo = int(input('Modelo de automovil para filtrar: '))
    print('Listado de automoviles disponibles con modelo mayor a ' + str(modelo))
    while m.tell() < tbm:
        aut = pickle.load(m)
        if aut.estado == 1 and aut.modelo > modelo:
            print(aut)
    m.close()

    print()
    input('Presione  para seguir...')


def main():
    fd = 'automoviles.aut'

    op = 0
    while op != 5:
        print('Opciones del archivo de automoviles')
        print('   1. Alta de automoviles')
        print('   2. Modificación de estado de un automovil')
        print('   3. Listado completo de automoviles')
        print('   4. Listado de automoviles disponibles con modelo mayor a m')
        print('   5. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if op == 1:
            alta(fd)

        elif op == 2:
            modificacion(fd)

        elif op == 3:
            listado_completo(fd)

        elif op == 4:
            listado_filtrado(fd)

        elif op == 5:
            pass


# script principal...
if __name__ == '__main__':
    main()
