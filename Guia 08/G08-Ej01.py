__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

menu = 'Menu de Opciones \n' \
       '=========================================================' + '\n' \
       '1 -- Suma de cuadrados \n' \
       '2 -- Cantidad de palabras que terminan en vocales\n' \
       '3 -- Determinar cantidad de pares e impares\n' \
       '4 -- Salir \n'
opcion = 0
vocales = 'aeiouAEIOU'

while opcion != 4:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        n = 0
        suma = 0
        while n <= 0:
            n = int(input('Ingrese un numero: '))
            if n <= 0:
                print('Error!!! El numero debe ser mayor a cero')
        for valor in range(1, n + 1):
            suma += valor ** 2
        print('La suma de los cuadrados del 1 al', n, ' es', suma)

    elif opcion == 2:
        texto = input('Ingrese el texto a analizar, Finaliza con punto: ')
        cp = 0
        caranterior = ' '
        for caracter in texto:
            if caracter == ' ' or caracter == '.':
                if caranterior in vocales:
                    cp += 1
            caranterior = caracter
        print('La cantidad de palabras que terminan con vocales son', cp)

    elif opcion == 3:
        cpares = cimprares = 0
        n = int(input('Ingrese un numero (la carga finaliza con cero): '))
        while n != 0:
            if n % 2 == 0:
                cpares += 1
            else:
                cimprares += 1
            n = int(input('Ingrese otro numero: '))

        if cpares > cimprares:
            print('Hay una mayor cantidad de numeros pares que impares')
        else:
            print('Hay una mayor cantidad de numeros impares que pares')
