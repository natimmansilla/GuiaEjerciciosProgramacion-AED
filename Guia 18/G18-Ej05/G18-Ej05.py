__author__ = 'Algoritmos y Estructuras de Datos'

import random


# funcion que carga en forma aleatoria los valores de los 4 vectores a analizar
def carga_datos_aleatorios(cant):
    tupla_col = "Blanco", "Negro", "Azul"
    tupla_tipo = "Cuero", "Tela"
    n = list()
    c = list()
    e = list()
    t = list()
    for i in range(0, cant):
        n.append(random.randint(35, 40))
        c.append(random.choice(tupla_col))
        e.append(random.randint(10, 25))
        t.append(random.choice(tupla_tipo))
    return n, c, e, t


# Funcion que muestra las opciones  del menu
def menu():
    print("\n ESTADISTICAS ")
    print("1) Número de zapatillas promedio")
    print("2) Color de Preferencia entre 10 y 18 años")
    print("3) Material de  preferencia de los jóvenes entre 19 y 25 años")
    print("4) Demanda de cada número de calzado")
    print("5) El número de mayor y menor demanda")
    print("0) Salir del menu")


# Funcion que permite calcular el promedio de nro. de zapatillas
def calcular_Promedio(v_nro):
    p = s = 0
    cant = len(v_nro)
    for i in range(cant):
        s += v_nro[i]
    if cant != 0:
        p = s / cant
    return p


# Funcion que determina cual color prefieren mas
def mayor(a, n, b):
    if a > n and a > b:
        c_may = a
        color_m = "Azul"
    elif n > a and n > b:
        c_may = n
        color_m = "Negro"
    else:
        c_may = b
        color_m = "Blanco"
    return c_may, color_m


# Funcion que cuenta cuantos prefieren cada color de zapatillas
def determinar_pref(v_edad, v_color):
    cant = len(v_color)
    cont_b, cont_n, cont_a = 0, 0, 0
    for i in range(cant):
        if v_edad[i] >= 10 and v_edad[i] < 19:
            if v_color[i] == "Blanco":
                cont_b += 1
            elif v_color[i] == "Negro":
                cont_n += 1
            else:
                cont_a += 1
    may = mayor(cont_a, cont_n, cont_b)
    return may


# funcion que determina qué tipo de material prefieren los jovenes
def determinar_pref_tipo(v_edad, v_tipo):
    cant = len(v_tipo)
    c_tela = c_cuero = 0
    for i in range(cant):
        if v_edad[i] > 19:
            if v_tipo[i] == "Tela":
                c_tela += 1
            else:
                c_cuero += 1
    if c_cuero > c_tela:
        pref = "Cuero"
    else:
        pref = "Tela"
    return pref


# Funcion que genera un vector que contiene
# la demanda de cada número de zapatillas
def determinar_demanda(v_nro):
    v = [0] * 6
    for i in range(len(v_nro)):
        v[v_nro[i] - 35] += 1
    return v


# Funcion que determina el nro. de mayor y menor demanda de zapatillas
def buscar_May_men(v_demanda):
    may = 0
    men = 1000
    for i in range(len(v_demanda)):
        if v_demanda[i] > may:
            may = v_demanda[i]

        if v_demanda[i] < men:
            men = v_demanda[i]

    return may, men


# Función principal
def main():
    v_nro = []
    v_color = []
    v_edad = []
    v_tipo = []
    v_demanda = None
    print("ESTADISTICAS\n")
    cant = int(input("\nIngrese cantidad de encuestas a cargar :"))
    v_nro, v_color, v_edad, v_tipo = carga_datos_aleatorios(cant)
    print("Datos cargados :\n Nro. de Calzados: ", v_nro)
    print("\n Colores elegidos", v_color, "\n Edades: ",
          v_edad, "\n tipo de material:", v_tipo)
    opcion = 1
    while opcion != 0:
        menu()
        opcion = int(input("Ingrese opcion :"))
        if opcion == 1:
            print("EL VALOR PROMEDIO DE NRO DE CALZADOS ES: ",
                  calcular_Promedio(v_nro))

        elif opcion == 2:
            color_pref = determinar_pref(v_edad, v_color)
            print("el color de mayor demanda es :", color_pref[1],
                  ", con un total de :", color_pref[0])

        elif opcion == 3:
            material_pref = determinar_pref_tipo(v_edad, v_tipo)
            print("El material que prefieren los jóvenes mayores "
                  "de 19 años es el : ", material_pref)

        elif opcion == 4:
            v_demanda = determinar_demanda(v_nro)
            n = 35
            print("\nLa demanda de cada numero de zapatillas es :")
            for i in range(len(v_demanda)):
                print("nro. ", (n + i), ": ", v_demanda[i])

        elif opcion == 5:
            # controlo que el vector v_demanda este cargado, sino lo cargo
            if v_demanda == None:
                v_demanda = determinar_demanda(v_nro)
            mayor, menor = buscar_May_men(v_demanda)
            # para controlar si hay mas de un nro. con mayor o menor demanda,
            # recorro el vector  de demandas y muestro los de igual demanda
            for i in range(len(v_demanda)):
                if v_demanda[i] == mayor:
                    print("El nro. de calzado de mayor demanda es : ", i + 35,
                          " con ", v_demanda[i], "")
            for i in range(len(v_demanda)):
                if v_demanda[i] == menor:
                    print("\n y el de menor demanda es: ", i + 35,
                          " con ", v_demanda[i])

        elif opcion == 0:
            print("FIN DEL PROGRAMA")

        else:
            print("ERROR, DEBE INGRESAR UN VALOR ENTRE 0 Y 5 ")


if __name__ == '__main__':
    main()
