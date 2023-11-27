class Proyecto:
    def __init__(self, numero, nombre, honorarios, tipo):
        self.codigo = numero
        self.cliente = nombre
        self.honorarios = honorarios
        self.tipo = tipo

    def __str__(self):
        linea = 'Código: {:<8}  Cliente: {:<30}  Honorarios: ${:>10.2f}  Tipo: {:>5}\n'
        return linea.format(self.codigo, self.cliente, self.honorarios, self.tipo)


def validar_mayor(minimo, mensage='Ingrese un valor: '):
    numero = minimo
    while numero <= minimo:
        numero = int(input(mensage))
        if numero < minimo:
            print('Valor incorrecto!!! Debe se mayor a ', minimo)
    return numero


def validar_rango(minimo, maximo, mensage='Ingrese un valor: '):
    numero = minimo - 1
    while numero <= minimo or numero > maximo:
        numero = int(input(mensage))
        if numero <= minimo or numero > maximo:
            print('Valor incorrecta!!! El valor debe estar comprendido entre', minimo, 'y', maximo)
    return numero


def cargar_proyectos(cantidad):
    v = []
    for i in range(cantidad):
        codigo = validar_mayor(0, 'Ingrese el codigo del proyecto: ')
        nombre = input('Ingrese el nombre del cliente: ')
        honorario = float(input('Ingrese los honorarios del arquitecto: '))
        tipo = validar_rango(0, 14, 'Ingrese el tipo de proyecto: ')
        v.append(Proyecto(codigo,nombre, honorario, tipo))
        print()
    return v


def listar_proyectos(vector):
    listado = '{:<8}\t{:<30}\t{:<10}\t{:<5}\n'.format('Codigo', 'Nombre', 'Honorarios', 'Tipo')
    listado += '-' * 70 + '\n'
    for proyecto in vector:
        listado += str(proyecto)
    return listado


def totalizar_horarios_por_tipo(proyectos):
    va = [0] * 15
    for proyecto in proyectos:
        va[proyecto.tipo] += proyecto.honorarios
    return va


def ordenar(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if vector[i].honorarios > vector[j].honorarios:
                vector[i], vector[j] = vector[j], vector[i]


def listar_excepto_tipo_4(vector):
    lista = [p for p in vector if p.tipo != 4]
    ordenar(lista)
    print(listar_proyectos(lista))


def buscar(vector, cliente):
    proyecto = None
    for proy in vector:
        if proy.cliente == cliente:
            proyecto = proy
            break
    return proyecto


def main():
    menu = 'Menu de Opciones\n' \
           '=======================================\n' \
           '1\t Cargar vector de proyectos\n' \
           '2\t Listar todos los proyectos\n' \
           '3\t Listar total de honorarios por tipo\n' \
           '4\t Listar proyectos tipo diferente 4\n' \
           '5\t Buscar proyecto por cliente\n'\
           '6\t Salir\n' \
           'Ingresar la opcion: '

    proyectos = None
    opcion = 0
    while opcion != 6:
        opcion = int(input(menu))
        if opcion == 1:
            cantidad = validar_mayor(0, 'Ingrese la cantidad de proyectos a generar: ')
            proyectos = cargar_proyectos(cantidad)
        else:
            if proyectos is not None:
                if opcion == 2:
                    print(listar_proyectos(proyectos))

                elif opcion == 3:
                    va = totalizar_horarios_por_tipo(proyectos)
                    linea = '{:<6}\t{:>13}\n{}\n'.format('Tipo', 'T. Honorarios', '-' * 23)
                    detalle = '{:<5}\t${:>13.2f}\n'
                    for pos in range(len(va)):
                        linea += detalle.format(pos, va[pos])
                    print(linea)

                elif opcion == 4:
                    listar_excepto_tipo_4(proyectos)

                elif opcion == 5:
                    cliente = input('Ingrese el nombre del cliente: ')
                    proyecto = buscar(proyectos, cliente)
                    if proyecto is not None:
                        print(proyecto)
                    else:
                        print('No existe un proyecto para el cliente', cliente)

            else:
                print('No se generaron proyectos!!!!')


if __name__ == '__main__':
    main()