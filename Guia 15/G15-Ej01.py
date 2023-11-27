import random


def validar_rango(mensage='Ingrese un numero: '):
    numero = 0
    while numero < 1 or numero > 4:
        numero = int(input(mensage))
        if numero < 1 or numero > 4:
            print('Valor incorrecto!!! El valor debe estar comprendio entre 1 y 4 incluidos.')
    return numero


def determinar_rango_trimestre(trimestre):
    if trimestre == 1:
        return range(3)
    elif trimestre == 2:
        return range(3, 6)
    elif trimestre == 3:
        return range(6, 9)
    else:
        return range(9, 12)


def determinar_promedio_trimestre(lluvias):
    trimestre = validar_rango('Ingrese el trimestre a calcular: ')
    suma = 0
    rango = determinar_rango_trimestre(trimestre)
    for i in rango:
        suma += lluvias[i]

    return trimestre, suma / len(rango)


def promedio_anual(lluvias):
    suma = 0
    tam = len(lluvias)

    for i in range(tam):
        suma += lluvias[i]

    return suma / tam


def buscar_mes_menor_lluvia(lluvias):
    menor = ()
    tam = len(lluvias)

    for m in range(tam):
        if m == 0:
            menor = m, lluvias[m]
        else:
            if menor[1] > lluvias[m]:
                menor = m, lluvias[m]
    return menor[0]


def principal():
    menu = 'Menu de Opciones \n' \
           '=================================== \n' \
           '1 \t Determinar el promedio anual de lluvias \n' \
           '2 \t Determinar el promedio de lluvias para un determinado trimestre \n' \
           '3 \t Determinar el mes más seco del mes \n' \
           '0 \t Salir \n '\
           'Ingrese su opcion: '
    opcion = -1

    lluvias = list()
    for i in range(12):
        lluvias.append(random.uniform(45.8, 160.1))

    while opcion != 0:
        opcion = int(input(menu))
        if opcion == 1:
            prom = promedio_anual(lluvias)
            print('El promedio anual de lluvias en el pais fue', prom, 'mm')
        elif opcion == 2:
            trimestre = determinar_promedio_trimestre(lluvias)
            print('El promedio de lluvias del trimestre', trimestre[0], 'fue de', trimestre[1], 'mm')
        elif opcion == 3:
            menor = buscar_mes_menor_lluvia(lluvias)
            print('El mes con menor lluvia registrada fue', menor + 1)


if __name__ == '__main__':
    principal()