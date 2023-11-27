# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe incluir al menos una función simple con parámetros y retorno de resultado, debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:
# Determinar el promedio de dígitos por palabra de las palabras formadas solo por dígitos que posee el texto. Por ejemplo, en el texto: “En el 2020 hubo 130 alumnos en el 1k02.” Resultado: 2 palabras cumplen con la condición: (“2020” y “130”) y tienen 7 dígitos  entre la dos. Por lo tanto su promedio de dígitos por palabra es 3.5.
# Determinar la cantidad de palabras que finalizan con un dígito y tienen al menos una letra. Por ejemplo, en el texto: “En el 2020 hubo 130 alumnos en el 1k05 y 1k09.” Resultado: 2 palabras cumplen con la condición (“1k05” y “1k09”).
# Determinar la longitud y el orden o posición de la palabra más corta del texto. Por ejemplo, para el texto: “Este cuatrimestre hubo 130 alumnos en el 1k02.” Como las palabras más cortas son “en” y “el” de ellas puedo mostrar el orden y la posición de cualquiera de las dos (NO HAY que mostrar la palabra propiamente dicha). Resultado: La longitud es 2 y (si se tomó la primera), la posición es 6.
# Determinar la cantidad de palabras que tienen las letras “ch” continuas pero comenzando esa secuencia a partir de la cuarta letra en adelante. Por ejemplo, en el texto: “El chancho cochino juega en la hamaca.” Resultado: 1 palabra cumple con la condición (“chancho”). La palabra "cochino“ no cumple, porque la secuencia "ch" comienza en la tercera letra.


def es_digito(car):
    if car >= '0' and car <= '9':
        return True
    else:
        return False


def calcular_promedio(suma, cant):
    if cant == 0:
        return 0
    else:
        return suma / cant


def es_letra(car):
    if (car >= 'a' and car <= 'z') or (car >= 'A' and car <= 'Z'):
        return True
    else:
        return False


def principal():
    print('PARCIAL 2')
    # Datos
    texto = input('Ingrese texto: ')
    # Variables de palabra (se reinician al terminar cada palabra)
    long_pal = 0
    solo_digitos = True
    tiene_letras = False
    tiene_ch = False
    ultimo = ''
    # Variables de texto (NO se reinician)
    suma_solo_dig = 0
    palabras_solo_dig = 0
    palabras_dig_let = 0
    cant_palabras = 0
    palabras_ch = 0
    # Proceso
    for car in texto:
        if car == ' ' or car == '.':
            if long_pal > 0:
                cant_palabras += 1
            if solo_digitos:
                suma_solo_dig += long_pal
                palabras_solo_dig += 1
            print(ultimo)
            if es_digito(ultimo) and tiene_letras:
                palabras_dig_let += 1
            if cant_palabras == 1:
                men_long, men_pos = long_pal, cant_palabras
            elif long_pal < men_long:
                men_long, men_pos = long_pal, cant_palabras
            if tiene_ch:
                palabras_ch += 1
            # Reiniciar variables de palabra
            long_pal = 0
            solo_digitos = True
            tiene_letras = False
            tiene_ch = False
        else:
            # Dentro de la palabra
            long_pal += 1
            if es_digito(car) == False:
                solo_digitos = False
            if es_letra(car):
                tiene_letras = True
            if car == 'h' and ultimo == 'c' and long_pal > 4:
                tiene_ch = True
            ultimo = car
    # Resultados
    print('-' * 80)
    promedio = calcular_promedio(suma_solo_dig, palabras_solo_dig)
    print('Promedio de dígitos por palabra de las palabras formadas solo por dígitos:', promedio)
    print('Palabras que finalizan con un dígito y tienen al menos una letra:', palabras_dig_let)
    print('La menor longitud es', men_long, 'y apareció en el orden o posición', men_pos)
    print('Palabras que tienen “ch” comenzando esa secuencia a partir de la cuarta letra:', palabras_ch)


if __name__ == '__main__':
    principal()