__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Menu de Opciones')
print('-' * 80)
print('1 - Calcular superficie del triangulo')
print('2 - Calcular perimetro del triangulo')
print('3 - Buscar menor lado del triangulo')
opcion = int(input('Ingrese su opcion: '))

if 1 <= opcion <= 3:

    lado1 = int(input('Ingrese el primer lado del triangulo'))
    lado2 = int(input('Ingrese el segundo lado del triangulo'))
    lado3 = int(input('Ingrese el tercer lado del triangulo'))

    if opcion == 1:
        s = (lado1 + lado2 + lado3) / 2
        superficie = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
        print('La superficie del triangulo es:', superficie)
    elif opcion == 2:
        perimetro = lado1 + lado2 + lado3
        print('El perimetro de un triangulo es', perimetro)
    elif opcion == 3:
        menor = min(lado1, lado2, lado3)
        print('El menor de los lados es', menor)
else:
    print('Selecciono una opcion erronea!!')
