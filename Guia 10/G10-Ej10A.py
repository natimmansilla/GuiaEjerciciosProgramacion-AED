__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def validar_cuit(cuit):
    # CUIT: un texto compuesto por 13 números
    # separados por guiones de la siguiente manera: 00-00000000-0
    valido = False
    cant_numeros = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[11] == '-':
            for car in cuit:
                if car in '0123456789':
                    cant_numeros += 1
            # Controlo si todos los que no son guiones, son digitos
            if cant_numeros == 11:
                valido = True
    return valido


def es_mayuscula(letra):
    if letra >= 'A' and letra <= 'Z':
        return True
    else:
        return False


def validar_descripcion(descripcion):
    # Descripción de la búsqueda: un texto donde
    # cada palabra se separa con un espacio y termina con punto.
    # Debe tener un máximo de 60 caracteres y un mínimo de 3 palabras.
    # Ninguna palabra debe contener 2 mayúsculas seguidas.
    valida = False
    cant_palabras = 0
    anterior = ''
    tiene_mayusc_seguidas = False
    if len(descripcion) <= 60:
        for letra in descripcion:
            # Contamos las palabras
            if letra == ' ' or letra == '.':
                cant_palabras += 1
            else:
                # Controlamos mayusculas seguidas
                if es_mayuscula(letra) and es_mayuscula(anterior):
                    tiene_mayusc_seguidas = True
            anterior = letra
        # Controlamos cantidad de palabras
        if cant_palabras >= 3:
            # Controlamos que no haya mayusculas seguidas
            if tiene_mayusc_seguidas == False:
                valida = True
    return valida


def validar_salario(salario):
    # Salario ofrecido: un valor mayor a 0
    if salario > 0:
        valido = True
    else:
        valido = False
    return valido


def principal():
    rta = 'S'
    while rta == 'S':
        print('PORTAL DE EMPLEOS')
        # Datos
        cuit_empleador = input('Ingrese cuit: ')
        # Proceso
        if validar_cuit(cuit_empleador):
            descripcion = input('Ingrese descripcion de la busqueda: ')
            if validar_descripcion(descripcion):
                salario = int(input('Ingrese salario ofrecido (mayor a 0): '))
                if validar_salario(salario):
                    # Mostramos el aviso
                    print('=' * 50)
                    print('AVISO')
                    print('El empleador', cuit_empleador, 'te esta buscando!')
                    print('Busqueda:', descripcion)
                    print('El salario ofrecido es de $', salario)
                    print('=' * 50)
                else:
                    print('El salario no es valido')
            else:
                print('La descripcion no es valida')
                print('Debe tener un máximo de 60 caracteres y un mínimo de 3 palabras.')
                print('Ninguna palabra debe contener 2 mayúsculas seguidas.')
        else:
            print('El cuit no es valido')
            print('Debe ser un texto compuesto por 13 números separados por guiones')
            print('de la siguiente manera: 00-00000000-0')
        rta = input('Quiere cargar otro aviso? (S/N) ')

    print('Programa terminado')


principal()
