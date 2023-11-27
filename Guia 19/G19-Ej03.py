class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def determinar_cuadrante(self):
        if self.x > 0:
            if self.y > 0:
                cuadrante = 1
            else:
                cuadrante = 4
        else:
            if self.y > 0:
                cuadrante = 2
            else:
                cuadrante = 3
        return cuadrante


def test():
    print('PUNTOS EN EL PLANO')
    print('-'*40)
    print('Primer punto')
    x = int(input('Coordenada x: '))
    y = int(input('Coordenada y: '))
    punto1 = Punto(x, y)
    print('Segundo punto')
    x = int(input('Coordenada x: '))
    y = int(input('Coordenada y: '))
    punto2 = Punto(x, y)

    cuad1 = punto1.determinar_cuadrante()
    cuad2 = punto2.determinar_cuadrante()

    print('-'*40)
    print(punto1, end="")
    print(' se encuentra en el cuadrante: ', cuad1)
    print(punto2, end="")
    print(' se encuentra en el cuadrante: ', cuad2)
    if cuad1 == cuad2:
        print('Están en el mismo cuadrante')
    else:
        print('No están en el mismo cuadrante')


if __name__ == '__main__':
    test()
