__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def test():
    # titulo general...
    print('Deteccion de secuencia 1-2-3')
    print('Carga de la secuencia, terminando en 0(cero)...')

    # inicializacion de flags y contadores...
    # contador de números ingresados...
    cn = 0

    # contador de números divisibles por 4...
    cd4 = 0

    # contador de veces que entro 1-2-3...
    c123 = 0

    # el mayor de los impares...
    myi = None

    # el primero de todos los numeros...
    prim = None

    # cuantas veces entro el primero de todos?...
    cvp = 0

    # flag: paso el primero de los impares?...
    spi = False

    # flag: el ultimo fue un 1?...
    s1 = False

    # flag: el ultimo fue un 2 e inmediatamente paso un 1?...
    s12 = False

    # carga del primer numero...
    num = int(input('Numero (ingrese un 0(cero) para terminar): '))

    # ciclo de carga para procesar le secuencia...
    while num != 0:
        # contar el número actual...
        cn += 1

        # 1.) contar divisibles por 4...
        if num % 4 == 0:
            cd4 += 1

        # 2.) determinar el mayor de los impares...
        if num % 2 == 1:
            if not spi:
                myi = num
                spi = True
            elif num > myi:
                myi = num

        # 3.) determinar cuantas veces entro el primero de todos...
        if cn == 1:
            prim = num
        if num == prim:
            cvp += 1

        # 4.) determinar cuantas veces entro la secuencia 1-2-3...
        if num == 1:
            s1 = True
            s12 = False
        else:
            if num == 2 and s1:
                s12 = True
            else:
                if num == 3 and s12:
                    c123 += 1

                s12 = False
            s1 = False

        # carga del siguiente numero...
        num = int(input('Otro (ingrese un 0(cero) para terminar): '))

    # analisis de los resultados finales...
    print('1. Cantidad de numeros divisibles por 4:', cd4)
    print('2. Mayor de los impares:', myi)
    print('3. El primero fue el', prim, 'y se ingreso:', cvp, 'veces')
    print('4. Cantidad de veces que se formo la secuencia 1-2-3:', c123)


# script principal...
# ... solo invocar a test()...
test()
