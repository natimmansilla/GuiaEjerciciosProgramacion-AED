import arreglos


def test():
    print('ARREGLOS: ÚLTIMO Y PRIMERO')
    print('*'*80)
    n = arreglos.validar_tamanio()
    v = arreglos.crear(n)
    print('*'*80)
    rep = arreglos.contar_repeticiones(v)
    print('El último número se repite',rep,'veces en el vector')
    menores = arreglos.buscar_menores(v)
    print('Los valores menores al primer elemento son:',menores)


if __name__ == "__main__":
    test()