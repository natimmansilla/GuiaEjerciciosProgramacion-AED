def cargar_datos():
    n = int(input("Ingrese la cantidad de muestras a registrar: "))
    temperaturas = [0.0] * n
    regiones = [0] * n
    dias = [0] * n
    for i in range(n):
        dia = int(input("Ingrese día: "))
        region = int(input("Ingrese región: "))
        temperatura = float(input("Ingrese temperatura: "))
        dias[i] = dia
        regiones[i] = region
        temperaturas[i] = temperatura
    return dias, regiones, temperaturas


def menu():
    print("1 _ Cargar datos")
    print("2 _ Promedio de temperaturas")
    print("3 _ Mostrar temperatura de una región")
    print("4 _ Buscar temperaturas mayores a x")
    print("5 - Mostrar cantidad de muestras por región")
    print("0 _ Salir")
    return int(input("Ingrese opción: "))


def promedio_temperaturas(temperaturas):
    suma = 0
    for temp in temperaturas:
        suma += temp
    return suma / len(temperaturas)


def buscar_temperatura(regiones, temperaturas, region, x):
    existe = False
    for i in range(len(regiones)):
        if regiones[i] == region and temperaturas[i] > x:
            existe = True
            break

    return existe


def ordenar(dias, regiones, temperaturas):
    n = len(dias)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if dias[i] > dias[j]:
                dias[i], dias[j] = dias[j], dias[i]
                regiones[i], regiones[j] = regiones[j], regiones[i]
                temperaturas[i], temperaturas[j] = temperaturas[j], temperaturas[i]


def mostrar_temperaturas(dias, regiones, temperaturas, reg):
    print("Dia \t\t Temperatura")
    for i in range(len(regiones)):
        if regiones[i] == reg:
            print(dias[i], "\t\t\t", temperaturas[i])


def contar_muestras_por_region(regiones):
    n = len(regiones)
    # Se crea un vector con 20 contadores (uno por región), todos en cero
    muestras_por_region = [0] * 20

    # Se recorren los datos, para contar en el contador correspondiente
    for i in range(n):
        # Se consigue el índice del contador para la región. Se resta 1 porque las regiones están numeradas en el rango
        # 1 a 20, pero los índices del vector están en el rango 0 a 19
        indice = regiones[i] - 1

        # Se cuenta una muestra para esa región
        muestras_por_region[indice] += 1

    # Se devuelve el vector con el resultado
    return muestras_por_region


def mostrar_muestras_por_region(muestras_por_region):
    n = len(muestras_por_region)

    # Se recorre el vector de contadores
    for i in range(n):
        # El índice indica la región y el valor del vector en ese índice indica la cantidad de muestras. NO es realmente
        # necesario crear una variable para almacenar el valor de muestras_por_region[i], lo hago de esta manera por
        # claridad en el ejemplo
        cantidad_muestras = muestras_por_region[i]

        # El enunciado no lo pide explícitamente, pero puede pensarse en mostrar únicamente aquellas regiones donde
        # haya habido, al menos, una muestra.
        if cantidad_muestras > 0:
            # Nuevamente, hay que tener en cuenta que los índices están en el rango [0, 19], pero las regiones [1, 20]
            region = i + 1
            # Se muestra el valor para esa cantidad
            print('Para la región', region, 'hay', cantidad_muestras, 'muestras')


def main():
    dias = None
    regiones = None
    temperaturas = None

    op = 0
    while op != 6:
        op = menu()
        if op == 1:
            dias, regiones, temperaturas = cargar_datos()

        elif op == 2:
            if temperaturas is not None:
                promedio = promedio_temperaturas(temperaturas)
                print("El promedio de temperaturas fue de: ", promedio)
            else:
                print("Primero debe cargar los datos!")

        elif op == 3:
            if temperaturas is not None:
                ordenar(dias, regiones, temperaturas)
                reg = int(input("Ingrese región a analizar: "))
                mostrar_temperaturas(dias, regiones, temperaturas, reg)
            else:
                print("Primero debe cargar los datos!")

        elif op == 4:
            if temperaturas is not None:
                reg = int(input("Ingrese región a analizar: "))
                x = int(input("Ingrese temperatura a controlar: "))
                existe = buscar_temperatura(regiones, temperaturas, reg, x)
                if existe:
                    resultado = "Hay al menos una temperatura menor a"
                else:
                    resultado = "No hay temperaturas menores a"
                print(resultado, x, "en la región analizada")
            else:
                print("Primero debe cargar los datos!")

        elif op == 5:
            if temperaturas is not None:
                # Se obtiene el vector de conteo por región
                muestras_por_region = contar_muestras_por_region(regiones)
                # Se muestran los resultados
                mostrar_muestras_por_region(muestras_por_region)
            else:
                print("Primero debe cargar los datos!")

        elif op == 6:
            print("Hasta luego.")

        else:
            print("Error, opción errónea")


if __name__ == "__main__":
    main()