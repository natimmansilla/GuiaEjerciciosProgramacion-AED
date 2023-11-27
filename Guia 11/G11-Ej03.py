__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Inicialización de variables
vocales = 'aeiouAEIOUáéíóú'
texto = ''
cv = cp = cl = ctl = may = cpTa = 0
hayT = hayTa = False

# Validacion de que el texto no tenga longitud 0
while len(texto) <= 0:
    texto = input('Ingrese el texto a analizar: ')
    if len(texto) <= 0:
        texto = input('Ingrese el texto a analizar: ')

# comienza el procesamiento del texto ingresado por el usuario
for c in texto:
    if c.isalpha():  # si es un caracter alfanumerico
        cl += 1  # cuenta las letras de la palabra

        if c in vocales:  # pregunta si la letra es una vocal
            cv += 1  # cuenta las vocales de la frase

        if cl == 1 and c.upper() == 'T':  # pregunta si es el primer caracter y ademas es igual a T.
            # c.upper() convierte el caracter c a mayusculas
            hayT = True  # activa la bandera
        else:
            if hayT and c.upper() == 'A':  # pregunta si el primer caracter era T y el actual es A
                hayTa = True  # activa la bandera indicando que encontro la silaba TA al comienzo de la palabra
            hayT = False  # desactiva la bandera porque no encontro la silaba TA al comienzo de la palabra

    else:  # si no es un caracter alfanumerico (espacio, punto, etc.)

        if cl > 0:  # si la cantidad de letras es mayor a 0
            cp += 1  # cuenta una palabra mas
            ctl += cl  # incrementa el acumulador de letras de la frase en la cantidad de letras de la palabra
            if cl > may:  # hace la busqueda de la palabra de mayor longitud
                may = cl  # si encuentra un mayor, almacena la longitud de la palabra

        if hayTa:  # si encontro la  silaba TA
            cpTa += 1  # incrementa el contador de silabas TA que encontro
            hayTa = False  # resetea la bandera para que pueda seguir buscando la silaba en las palabras subsiguientes
        cl = 0  # resetea el contador de letras de la palabra para que siga contando la cantidad de letras de las palabras subsiguientes

if ctl != 0:  # valida que el denominador del calculo del porcentaje sea distinto de 0 para evitar una indeterminacion
    porc = round(cv * 100 / ctl, 2)  # Calcula el porcentaje de vocales con respecto a la cantidad de letras de la frase
else:
    porc = 0  # si el denominador es 0, entonces el calculo del porcentaje se determina como igual a 0.

if cp != 0:  # valida que el denominador del calculo del promedio sea distinto de 0 para evitar una indeterminacion
    prom = ctl // cp  # calcula la longitud promedio de las palabras de la frase
else:
    prom = 0  # si el denominador es 0, entonces el calculo del promedio se determina como igual a 0.

# Muestra de resultados
print('El porcentaje de vocales respecto del total de letras es de ', porc, '%')
print('Hay', prom, 'letras por palabra')
print('La palabra mas larga del texto tiene', may, 'letras')
print('Hay', cpTa, 'palabras que comienzan con \"ta\"')
