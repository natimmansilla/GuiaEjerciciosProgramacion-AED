"""
    Procesar el arhivo de texto con datos de los alumnos que puede descargar haciendo click aquí, cada fila de datos
    contiene los datos de los alumnos en un esquema de cantidad fija de caracteres.

    De cada alumno figura, el legajo, nombre, nota del parcial 1, nota del parcial 2, nota del parcial 3 y nota de
    trabajos prácticos

    Se necesita procesar el archivo para conocer la cantidad de alumnos por cada estado académico:
    * Cantidad de alumnos Libres
    * Cantidad de alumnos Regulares
    * Cantidad de alumnos aprobados

    Nota: para aprobar el alumo debe tener en los parciales promedio de 8 con nota no menor a 7 y en la nota de tps 8 o
    más, para regularizar debe tener 2 de los 3 parciales aprobados con nota 4 o más y los trabajos prácticos con nota
    4 o más y en caso contrario está libre.

    También es necesario mostrar un listado con los alumnos aprobados agregando a cada alumno su no ta final que surge
    del promedio directo de las 4 notas del alumno.

    Finalmente, el programa debe mostrar el porcentaje de cada condición de alumno respecto del total del curso.

"""
import funciones as f

NOMBRE_ARCHIVO = 'datos.txt'
# NOMBRE_ARCHIVO = 'pruebas.txt'

def programa():
    archivo = open(NOMBRE_ARCHIVO, 'rt')
    contador_libres = contador_regulares = contador_aprobados = 0
    # linea = archivo.readline()
    # while True:
    #     print(linea)
    #     linea = archivo.readline()
    #     if linea == "":
    #         break

    print('Listado de alumnos aprobados')
    for linea in archivo:
        # print(linea)
        # línea entre los paréntesis es el argumento o parametro actual
        leg, nom, p1, p2, p3, tps = f.procesar_linea(linea)
        condicion = f.determinar_condicion_alumno(p1, p2, p3, tps)
        # print('Debug:  ', leg, nom, p1, p2, p3, tps, '==>', condicion)
        if condicion == 2:
            nota_final = f.calcular_nota_final(p1, p2, p3, tps)
            print(f'{leg:>6} {nom:30} ==> {nota_final:>2}')
            contador_aprobados += 1
        elif condicion == 1:
            contador_regulares += 1
        else:
            contador_libres += 1

    total = contador_aprobados + contador_regulares + contador_libres
    print('Resultados: ')
    print('Cantidad Aprobados', contador_aprobados)
    print('Cantidad Regulares', contador_regulares)
    print('Cantidad Libres', contador_libres)
    print('El porcentaje de alumno aprobados', f.porcentaje(contador_aprobados, total))
    print('El porcentaje de alumno regulares', f.porcentaje(contador_regulares, total))
    print('El porcentaje de alumno libres', f.porcentaje(contador_libres, total))


# Script principal
if __name__ == '__main__':
    print('Inicio')
    programa()
    print('fin')

