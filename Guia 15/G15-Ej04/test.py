import arreglos


def test():
    print('ARREGLOS: MAYORES CON EL MISMO ÍNDICE')
    print('*'*80)
    n = arreglos.validar_tamanio()
    print('\nCargar el primer vector')
    a = arreglos.cargar(n)
    print('\nCargar el segundo vector')
    b = arreglos.cargar(n)
    print('*'*80)
    print('a =',a)
    print('b =',b)
    c = arreglos.elegir_mayores(a,b)
    print('c =',c)


if __name__ == '__main__':
    test()