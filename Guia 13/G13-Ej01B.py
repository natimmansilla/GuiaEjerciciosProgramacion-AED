def es_letra(car):
    if car != ' ' and car == '.':
        return True
    else:
        return False


def es_vocal(car):
    if car in "aeiou":
        return True
    else:
        return False


def es_impar(nro):
    if nro % 2 == 1:
        return True
    else:
        return False


def porcentaje(cantidad, total):
    return cantidad / total * 100


def promedio(suma, cantidad):
    if cantidad > 0:
        return suma / cantidad
    else:
        return 0


c_vocales = 0
c_letras = 0
c_palabras = 0
c_palabras_si = 0  # Cantidad de palabras con SI
c_palabras_cc = 0  # Cantidad de palabras con CC
c_palabras_vi = 0  # Cantidad de palabras con vocales impares
c_palabras_1v = 0  # Cantidad de palabras con una sola vocal
c_palabras_pu = 0  # Cantidad de palabras con primera y última letras iguales
minima = 0  # Longitud de palabra mínima
primera = None  # Primera letra de cada palabra
ultima = None  # Ultima letra de cada palabra
paso_s = False
paso_si = False
paso_c = False
paso_cc = False
paso_vocal = False
acum_letras = 0

texto = input('Ingrese un texto:').lower()

for car in texto:  # Por cada car del texto
    if es_letra(car):  # Si car es una letra o sea que no es un separador
        # Dentro de la palabra:
        c_letras += 1

        # Secuencia de dos letras diferentes
        if car == 's' and c_letras == 1:
            paso_s = True
        else:
            if car == 'i' and paso_s:
                paso_si = True
            paso_s = False

        # Secuencia de dos letras iguales
        if car == 'c':
            if paso_c:
                paso_cc = True
            paso_c = True
        else:
            paso_c = False

        # Contador de vocales y bandera de vocal en la letra anterior
        if es_vocal(car):
            c_vocales += 1
            paso_vocal = True
        else:
            paso_vocal = False

        # Para guardar la primera letra
        if c_letras == 1:
            primera = car

        # Guardar la anterior
        ultima = car
    else:
        # fuera de la palabra:
        if c_letras > 0:

            c_palabras += 1
            if paso_si:
                c_palabras_si += 1

            if paso_cc:
                c_palabras_cc += 1

            if paso_vocal and es_impar(c_letras):
                c_palabras_vi += 1

            if c_vocales == 1:
                c_palabras_1v += 1

            if primera == ultima:  # La anterior al separador es la última
                c_palabras_pu += 1

            if c_palabras == 1 or c_letras < minima:
                minima = c_letras

            acum_letras += c_letras

            # Limpieza para la próxima palabra
            c_letras = c_vocales = 0
            paso_s = paso_si = pasoc = paso_cc = paso_vocal = False
            primera = ultima = None

# Al final del texto
porcentaje_punto_b = porcentaje(c_palabras_vi, c_palabras)
promedio_letras = promedio(acum_letras, c_palabras)

# Presentación de resultados
print("Cantidad de palabras que comienzan con la expresión ´SI´:", c_palabras_si)
print("Cantidad de palabras que terminan con vocal y tienen una cantidad impar de letras:", c_palabras_vi)
print("Cantidad de palabras que tienen sólo una vocal:", c_palabras_1v)
print("Cantidad de palabras que comienzan y terminan con la misma letra:", c_palabras_pu)
print("Cantidad de palabras que contienen la expresión ´CC´:", c_palabras_cc)
print("Porcentaje que representan las palabras del punto b sobre el total de palabras:", porcentaje_punto_b)
print("Longitud de la palabra más corta:", minima)
print("Promedio de letras por palabra:", promedio_letras)
