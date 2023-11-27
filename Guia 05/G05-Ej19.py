__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print("Análisis de lluvias en un trimestre\n")

mes1 = float(input("Ingrese los mm de lluvia caídos en el primer mes del trimestre: "))
mes2 = float(input("Ingrese los mm de lluvia caídos en el segundo mes del trimestre: "))
mes3 = float(input("Ingrese los mm de lluvia caídos en el tercer mes del trimestre: "))

promedio = (mes1 + mes2 + mes3) / 3

print("Promedio de lluvias caídas:", promedio)

mayores_promedio = 0
if mes1 >= promedio:
    mayores_promedio += 1
if mes2 >= promedio:
    mayores_promedio += 1
if mes3 >= promedio:
    mayores_promedio += 1

print("Cantidad de meses con lluvias mayores al promedio:", mayores_promedio)

if mes1<mes2 and mes1<mes3:
    mes = 1
    men = mes1
else:
    if mes2 < mes3:
        mes = 2
        men = mes2
    else:
        mes = 3
        men = mes3

print("Mes con menos lluvias:", mes)

sin_lluvia = False
if men == 0:
    sin_lluvia = True

if sin_lluvia:
    print("Dicho mes no tuvo lluvias")