__author__ = 'Algoritmos y Estructuras de Datos'


def validate_values(mensaje, valores_permitidos, mensaje_error):
    val = int(input(mensaje))
    while val not in valores_permitidos:
        print(mensaje_error)
        val = int(input(mensaje))
    return val


def validate_range(mensaje, inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje + " (entre " + str(inf) + " y " + str(sup) + "): "))
        if n < inf or n > sup:
            print("Valor incorrecto!")
    return n


def cargar_datos(nombre1, nombre2):
    # se solicita la cantidad de sets a la que se juega el partido, 3 o 5
    cantidad_sets = validate_values('Cantidad de sets:', [3, 5], 'Valor Incorrecto, reintente')
    # Hay una cantidad mínima de sets que debe ser jugado para que uno pueda ganar
    cantidad_minima_sets = cantidad_sets // 2 + 1
    # Se solicita la cantidad de sets que se desean cargar como resultado
    cantidad_sets_jugados = validate_range('Cantidad de sets jugados', cantidad_minima_sets, cantidad_sets)
    # Se incializan los vectores que almacenarán los puntajes de cada jugador
    puntos1 = [0] * cantidad_sets_jugados
    puntos2 = [0] * cantidad_sets_jugados
    # Para cada set que se va a cargar, se solicitan los games de cada jugador
    for i in range(cantidad_sets_jugados):
        puntos1[i] = validate_range(nombre1 + ', Set ' + str(i + 1), 0, 7)
        puntos2[i] = validate_range(nombre2 + ', Set ' + str(i + 1), 0, 7)
    return cantidad_sets, puntos1, puntos2


def mostrar(nombre1, nombre2, puntos1, puntos2):
    print('Resultados cargados:')
    print(nombre1, ':', puntos1)
    print(nombre2, ':', puntos2)


def determinar_ganador(cantidad_sets, puntos1, puntos2):
    # Se acumulan los sets ganados por cada jugador
    sets_ganados1 = 0
    sets_ganados2 = 0
    # El ganador debe haber ganado más de la mitad de los sets
    cantidad_minima_sets = cantidad_sets // 2 + 1
    # Para cada set cargado como resultado
    for i in range(len(puntos1)):
        if puntos1[i] > puntos2[i]:
            sets_ganados1 += 1
        else:
            sets_ganados2 += 1

        # Si uno de los jugadores alcanzó la cantidad mínima de games
        # para ganar, ganó
        if sets_ganados1 == cantidad_minima_sets:
            return True, 1, (i + 1)

        if sets_ganados2 == cantidad_minima_sets:
            return True, 2, (i + 1)

    return False, 0, 0


def validar_cantidad_games(set, punto1, punto2):
    # Para ganar un set, se deben ganar, al menos, 6 games
    if punto1 < 6 and punto2 < 6:
        print('Se deben ganar al menos 6 games en un set', '(Set=' + str(set) + ')')
        return False

    return True


def validar_diferencias(set, punto1, punto2):
    # Debe haber diferencia de 2 games, salvo tiebreak (7-6)
    if abs(punto1 - punto2) < 2:
        # Si terminó 7-6 es válido, en otro caso, no
        if punto1 + punto2 != 13:
            # No se alcanzó diferencia de al menos 2 sets y no se trata de
            # un tie-break
            print('No hay diferencia de 2 games', '(Set=' + str(set) + ')')
            return False
    return True


def validar_game_extra(set, punto1, punto2):
    # Si se llegó a 7 games es un tiebreak o el resultado es 7-5
    if punto1 == 7 or punto2 == 7:
        suma_puntos = punto1 + punto2
        # Si el resultado no es 7-5 o 7-6, no es válido
        if suma_puntos != 12 and suma_puntos != 13:
            print('Si uno de los jugadores llegó a 7 games, o es 7-6 (tie-break) o 7-5', '(Set=' + str(set) + ')')
            return False

    return True


def validar_cantidad_sets(cantidad_sets, puntos1, puntos2):
    # En los resultados, debió ganar un jugador, y luego de ganar, no se debieron jugar más sets
    hubo_ganador, jugador, set = determinar_ganador(cantidad_sets, puntos1, puntos2)

    # Si los datos son incorrectos y no hubo ganador...
    if not hubo_ganador:
        print('Ningún jugador alcanzó la cantidad mínima de sets para ganar');
        return False

    if set < len(puntos1):
        # Significa que se registraron más sets que los necesarios
        print('Se jugaron más sets que los necesarios para un ganador')
        return False


def validar(cantidad_sets, puntos1, puntos2):
    # Se recorren los resultados cargados y se valida que los puntos estén bien
    for i in range(len(puntos1)):

        if not validar_cantidad_games(i + 1, puntos1[i], puntos2[i]):
            return False

        if not validar_diferencias(i + 1, puntos1[i], puntos2[i]):
            return False

        if not validar_game_extra(i + 1, puntos1[i], puntos2[i]):
            return False

    if not validar_cantidad_sets(cantidad_sets, puntos1, puntos2):
        return False

    return True


def contar_tiebreak(puntos1, puntos2):
    # se acumula la cantidad de tie-breaks (resultados 7-6)
    cant_tiebreaks = 0
    # se recorren los resultados
    for i in range(len(puntos1)):
        # Si alguno de los dos terminó con 7 games
        if puntos1[i] == 7 or puntos2[i] == 7:
            # Si suman 13, es porque salieron 7-6
            if (puntos1[i] + puntos2[i]) == 13:
                cant_tiebreaks += 1

    # se devuelve la cantidad de tie-breaks
    return cant_tiebreaks


def calcular_diferencias(puntos1, puntos2):
    # se inicializa el vector con las diferencias
    diferencias = [0] * len(puntos1)
    # se recorren los resultados
    for i in range(len(puntos1)):
        # simplemente se asigna la diferencia en el elemento correcto del array
        # se toma el valor absoluto para no asumir que un jugador ganó más games que otro
        diferencias[i] = abs(puntos1[i] - puntos2[i])

    # se devuelven los valores
    return diferencias


def ordenar(diferencias):
    # cantidad de elementos del vector de diferencias
    n = len(diferencias)
    # vector con los números de sets
    sets = list(range(1, n + 1))
    # Ordenamiento
    for i in range(n - 1):
        for j in range(i + 1, n):
            if diferencias[i] < diferencias[j]:
                diferencias[i], diferencias[j] = diferencias[j], diferencias[i]
                sets[i], sets[j] = sets[j], sets[i]
    return sets, diferencias


def menu():
    print('')
    print('1) Cargar datos')
    print('2) Validar datos')
    print('3) Determinar ganador')
    print('4) Sets ganados por tie-break')
    print('5) Mostrar diferencias')
    print('6) Mostrar Sets con mayor diferencia')
    print('')
    print('7) - Salir')
    print('')
    return validate_range('Ingrese opción: ', 1, 7)
    print('')


def main():
    nombre1 = ''
    nombre2 = ''
    puntos1 = []
    puntos2 = []
    sets = 0
    validos = False
    op = menu()
    while op != 7:
        if op == 1:
            # Se solicitan los nombres de los jugadores
            nombre1 = input('Ingrese el nombre del jugador 1: ')
            nombre2 = input('Ingrese el nombre del jugador 2: ')
            # Se cargan los resultados del partido
            sets, puntos1, puntos2 = cargar_datos(nombre1, nombre2)
            # Se muestran los resultados
            mostrar(nombre1, nombre2, puntos1, puntos2)
            # Se marcan como inválidos los datos, hasta que se validen
            validos = False
        elif op == 2:
            validos = validar(sets, puntos1, puntos2)
            if not validos:
                print('Validación fallida!!!')
            else:
                print('Datos válidos')
        elif op == 3:
            if not validos:
                print('Debe cargar datos válidos')
            else:
                mostrar(nombre1, nombre2, puntos1, puntos2)
                hubo_ganador, jugador, set = determinar_ganador(sets, puntos1, puntos2)
                if jugador == 1:
                    print('Ganó el jugador ' + nombre1 + ', en el Set ', str(set))
                else:
                    print('Ganó el jugador ' + nombre2 + ', en el Set ', str(set))
        elif op == 4:
            if not validos:
                print('Debe cargar datos válidos')
            else:
                mostrar(nombre1, nombre2, puntos1, puntos2)
                print('La cantidad de sets ganados por tie-break es: ' + str(contar_tiebreak(puntos1, puntos2)))
        elif op == 5:
            if not validos:
                print('Debe cargar datos válidos')
            else:
                mostrar(nombre1, nombre2, puntos1, puntos2)
                print('Las diferencias fueron: ', calcular_diferencias(puntos1, puntos2))
        elif op == 6:
            if not validos:
                print('Debe cargar datos válidos')
            else:
                mostrar(nombre1, nombre2, puntos1, puntos2)
                sets_ordenados, diferencias = ordenar(calcular_diferencias(puntos1, puntos2))
                print('Sets (ordenados por diferencia): ', sets_ordenados)
                print('Diferencias                    : ', diferencias)
        op = menu()


if __name__ == "__main__":
    main()
