from socio import *
import os.path
import pickle
import io


def buscar(fd, m, numero):
    t = os.path.getsize(fd)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        soc = pickle.load(m)
        if soc.activo and soc.numero == numero:
            posicion = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def validar_entre(desde, hasta, mensaje):
    num = int(input(mensaje))
    while num < desde or num > hasta:
        print('Inválido! Debe ser un valor entre', desde, 'y', hasta)
        num = int(input(mensaje))
    return num


def validar_monto(mensaje):
    monto = float(input(mensaje))
    while monto < 0:
        print('Inválido! Debe ser un valor positivo.')
        monto = float(input(mensaje))
    return monto


def alta(fd):
    m = open(fd, 'a+b')
    print()
    numero = validar_entre(0, 99999, 'Ingrese número de socio: ')
    pos = buscar(fd, m, numero)
    if pos == -1:
        # no estaba repetido... lo cargamos por teclado...
        nombre = input('Ingrese nombre: ')
        # ...ajustamos a 30 caracteres, rellenando con blancos al final...
        nombre = nombre.ljust(40, ' ')
        plan = validar_entre(0, 3, 'Ingrese plan: ')
        monto = validar_monto('Ingrese cuota mensual: ')
        reg = Socio(numero, nombre, plan, monto)
        # ...lo grabamos...
        pickle.dump(reg, m)
        # ...volcamos el buffer de escritura
        # para que el sistema operativo REALMENTE
        # grabe en disco el registro...
        m.flush()
        print('Registro grabado en el archivo...')
    else:
        print('Número repetido... alta rechazada...')
    m.close()


def modificacion(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    print()
    numero = validar_entre(0, 99999, 'Ingrese número de socio a modificar: ')
    pos = buscar(fd, m, numero)
    if pos != -1:
        # encontrado... procedemos a cargarlo...
        m.seek(pos, io.SEEK_SET)
        reg = pickle.load(m)

        # ...mostramos el registro tal como estaba...
        print()
        print('El registro actualmente grabado es:')
        print(reg)

        reg.plan = validar_entre(0, 3, 'Ingrese plan:' )
        reg.monto = validar_monto('Ingrese cuota mensual: ')

        # ...registro modificado en memoria...
        # ...ahora nos volvemos a su posición en el archivo...
        m.seek(pos, io.SEEK_SET)

        # ...y volvemos a grabar el registro modificado...
        pickle.dump(reg, m)

        print()
        print('Los datos del registro se actualizaron en el archivo...')

    else:
        print('Ese registro no existe en el archivo...')

    m.close()


def baja(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    print()
    numero = validar_entre(0, 99999, 'Ingrese número de socio: ')
    pos = buscar(fd, m, numero)
    if pos != -1:
        # encontrado... procedemos a cargarlo...
        m.seek(pos, io.SEEK_SET)
        reg = pickle.load(m)

        # ...mostramos el registro tal como estaba...
        print()
        print('El registro actualmente grabado es:')
        print(reg)

        # ...chequemos si el usario está seguro de lo que hace...
        r = input('Está seguro de querer borrarlo (s/n)?: ')
        if r in ['s', 'S']:
            # lo marcamos como borrado, y ya...
            reg.activo = False

            # ...reubicamos el file pointer...
            m.seek(pos, io.SEEK_SET)

            # ...y lo volvemos a grabar...
            pickle.dump(reg, m)

            print()
            print('Registro eliminado del archivo...')

    else:
        print('Ese registro no existe en el archivo...')

    m.close()


def listado_completo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    print('Listado General de Socios')
    while m.tell() < tbm:
        reg = pickle.load(m)
        if reg.activo:
            print(reg)

    m.close()


def sumar_por_plan(fd):
    va = [0] * 4
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    while m.tell() < tbm:
        reg = pickle.load(m)
        if reg.activo:
            va[reg.plan] += reg.monto

    m.close()

    for i in range(len(va)):
        print('Plan', i, 'Monto $', va[i])


def depuracion(fd):
    """Optimiza el espacio físico del archivo.

    La función aplica un proceso de baja física generalizada: todos los registros que estaban
    marcados en forma lógica como eliminados, son físicamente eliminados del archivo.
    """
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    original = open(fd, 'rb')
    temporal = open('temporal.dat', 'wb')

    print('Procediendo a optimizar el archivo', fd, '(eliminación física de registros borrados)')
    while original.tell() < tbm:
        # cargar un registro del archivo original...
        reg = pickle.load(original)

        # ...y si no estaba marcado como eliminado, grabarlo en el archivo temporal...
        if reg.activo:
            pickle.dump(reg, temporal)

    # cerrar ambos archivos...
    original.close()
    temporal.close()

    # eliminar el archivo original...
    os.remove(fd)

    # y renombrar el temporal...
    os.rename('temporal.dat', fd)


def main():
    opcion = -1
    fd = 'socios.dat'
    while opcion != 0:
        print('\nMenu de Opciones')
        print('=' * 80)
        print('1\t Alta de Socio')
        print('2\t Modificacion de Socio')
        print('3\t Baja de Socio')
        print('4\t Listado de Socios')
        print('5\t Monto Total por Plan')
        print('6\t Compactar Archivo')
        print('0\t Salir')
        opcion = int(input('Ingrese la opcion a ejecutar: '))
        if opcion == 1:
            alta(fd)
        elif opcion == 2:
            modificacion(fd)
        elif opcion == 3:
            baja(fd)
        elif opcion == 4:
            listado_completo(fd)
        elif opcion == 5:
            sumar_por_plan(fd)
        elif opcion == 5:
            depuracion(fd)
        print('=' * 80)


if __name__ == '__main__':
    main()
