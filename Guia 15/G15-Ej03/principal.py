import arreglo
from funciones import validar_mayor_cero


def principal():
    print('Manejo de Arreglos')
    print('=================================')

    tam = validar_mayor_cero('Ingrese el tamaño del vector: ')
    vector = arreglo.crear(tam)

    print()
    print('Vector original:')
    print(arreglo.mostrar(vector))

    primos = arreglo.generar_vector_primos(vector)
    print()
    print('Vector con los números primos contenidos en el original:')
    print(arreglo.mostrar(primos))

    prom = arreglo.promedio(primos)
    print()
    print('El promedio de los números primos en el segundo vector es:', prom)


if __name__ == '__main__':
    principal()
