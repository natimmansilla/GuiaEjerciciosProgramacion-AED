def validar_cuit(cuit):
    # Proceso
    valido = False
    cant_nums = 0
    if len(cuit) == 13:
        if cuit[2] == '-' and cuit[-2] == '-':
            for car in cuit:
                if car >= '0' and car <= '9':
                    cant_nums += 1
            if cant_nums == 11:
                valido = True
            else:
                print('Los caracteres del CUIT no son todos numéricos')
        else:
            print('Los guiones del CUIT no son correctos')
    else:
        print('La longitud del CUIT es incorrecta')
    # Resultado
    return valido


def es_mayuscula(letra):
    if letra >= 'A' and letra <= 'Z':
        return True
    else:
        return False


def validar_descripcion(descripcion):
    valida = False
    cant_pal = 0
    mayusc_seg = False
    anterior = ''
    if len(descripcion) <= 60:
        for letra in descripcion:
            if letra == ' ' or letra == '.':
                cant_pal += 1
            if es_mayuscula(letra) and es_mayuscula(anterior):
                mayusc_seg = True
            anterior = letra
        if cant_pal >= 3:
            if mayusc_seg == False:
                valida = True
            else:
                print('Descripción inválida -  Tiene dos mayúsculas seguidas')
        else:
            print('Descripción inválida -  Tiene menos de 3 palabras')
    else:
        print('Descripción inválida - Tiene más de 60 caracteres')
    return valida


def validar_salario(salario):
    valido = False
    if salario > 0:
        valido = True
    else:
        print('El salario no puede ser menor que cero')
    return valido


def principal():
    rta = 'S'
    while rta == 'S':
        print('-' * 80)
        print('PORTAL DE EMPLEO')
        # Datos y proceso
        cuit = input('Ingrese el CUIT: ')
        ok = validar_cuit(cuit)
        if ok:
            descripcion = input('Ingrese la descripcion: ')
            ok = validar_descripcion(descripcion)
            if ok:
                salario = float(input('Ingrese el salario: '))
                ok = validar_salario(salario)
                if ok:
                    print('La empresa ', cuit, 'busca', descripcion,
                          '- Salario ofrecido $', salario)
                    print('-' * 80)
        rta = input('Desea cargar otro? S/N: ')


if __name__ == '__main__':
    principal()
