__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Ejericio tipo parcial')
print('=' * 60)
print('\n')

menu = 'Menu de Opciones\n' \
       '==================================\n' \
       '1 ------- Ingresar n numero y calcular porcentaje\n' \
       '2 ------- Analisis de texto\n' \
       '3 ------- Buscar peor alumno\n' \
       '0 ------- Salir\n' \
       'Ingrese su opcion: '

opcion = -1
while opcion != 0:
	# presentar las opciones
	opcion = int(input(menu))
	if opcion == 1:
		# Ingreso a la opcion 1
		n = 0
		cont_multiplos = 0
		while n <= 0:
			n = int(input('Ingresar la cantidad de numeros a procesar: '))
			if n <= 0:
				print('Error!!! Usted debe ingresar un numero mayor a cero')

		for i in range(n):
			numero = int(input('Ingrese el ' + str(i + 1) + '° de la secuencia: '))
			if numero % 3 == 0 or numero % 5 == 0:
				cont_multiplos += 1
		porcentaje = cont_multiplos * 100 / n
		print('La cantidad total de multiplos de 3 y 5 fueron:', cont_multiplos)
		print(' y representan un ', round(porcentaje, 2), '% sobre el total de numero')

	elif opcion == 2:
		# Ingreso a la opcion 2
		texto = input('Ingresar un texto (debe terminar con punto): ')
		if texto[-1] != '.':
			texto += '.'

		cl = cp = 0
		for caracter in texto:
			# tengo que identificar cuando recorro una palabra y cuando deje de recorrerla
			if caracter != ' ' and caracter != '.':
				# dentro de la palabra, leyendo de letras
				cl += 1
			else:
				# termine de recorrer la palabra y pregunto si he encontrado lo que estaba buscando en esa palabra
				if cl > 4:
					cp += 1
				cl = 0

		print('La cantidad total de palabras de mas de cuatro letras fue de:', cp)

	elif opcion == 3:
		# Ingreso a la opcion 3
		nombre_alumno_1 = input('Ingrese el nombre del primer alumno: ')
		nota_alumno_1 = int(input('Ingrese la nota final del primer alumno: '))
		nombre_alumno_2 = input('Ingrese el nombre del segundo alumno: ')
		nota_alumno_2 = int(input('Ingrese la nota final del primer alumno: '))
		nombre_alumno_3 = input('Ingrese el nombre del tercer alumno: ')
		nota_alumno_3 = int(input('Ingrese la nota final del primer alumno: '))

		if nota_alumno_1 < nota_alumno_2 and nota_alumno_1 < nota_alumno_3:
			peor_alumno = nombre_alumno_1
		elif nota_alumno_2 < nota_alumno_3:
			peor_alumno = nombre_alumno_2
		else:
			peor_alumno = nombre_alumno_3

		print('El alumno de posgrado con la peor nota fue:', peor_alumno)
	print('\n\n')
