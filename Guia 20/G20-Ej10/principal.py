import proceso
import clase

opciones = ('1. Cargar', '2. Mostrar ordenado', '3. Conteo por clase', '4. Filtrar clase 3', '5. Buscar', '0. Salir')


def mostrar_men_ing_opcion(opciones, titulo):
	print(titulo)
	for opc in opciones:
		print(opc)
	return int(input('Ingrese su opción: '))


def mostrar_vector_pasajes(vector):
	print('Lista de pasajes:')
	print(f'{"Pasaporte":9} {" Nombre y Apellido":<30} {"Destino":^7} {"Clase":^5} {"Monto":^10}')
	print('=' * 65)
	for reg in vector:
		print(reg)


def mostrar_vector_conteos(acumuladores):
	mayor = None

	for i in range(len(acumuladores)):
		if acumuladores[i] > 0:
			print(f'Clase: {i + 1} ==> importe acumulado: {acumuladores[i]}')
			if mayor is None or acumuladores[i] > mayor:
				mayor = acumuladores[i]
				clase_mayor = i + 1

	print(f'La clase con mayor monto acumulado fue la clase: {clase_mayor}')


def mostrar_pasajes_clase_3(vector, promedio):
	print('Lista de pasajes:')
	print(f'{"Pasaporte":9} {" Nombre y Apellido":<30} {"Destino":^7} {"Clase":^5} {"Monto":^10}')
	print('=' * 65)
	for pasaje in vector:
		if pasaje.clase == 3 and pasaje.monto > promedio:
			print(pasaje)


def validar_en_rango(msg, li, ls):
	valor = int(input(msg))
	while valor < li or valor > ls:
		print('Error')
		valor = int(input(msg))
	return valor


def inicio():
	vector = []
	opc = None

	while opc != 0:
		opc = mostrar_men_ing_opcion(opciones, 'Menú de Opciones')

		if opc != 0:
			print(f'\nOpción: {opciones[opc - 1]}\n')

			if opc == 1:
				n = int(input('Ingrese la cantidad: '))
				proceso.generar_datos(vector, n)

			elif len(vector) > 0 and opc < 6:
				if opc == 2:
					proceso.ordenar_por_monto(vector)
					mostrar_vector_pasajes(vector)

				elif opc == 3:
					acumuladores = proceso.acumular_por_clase(vector)
					mostrar_vector_conteos(acumuladores)

				elif opc == 4:
					promedio = proceso.calcular_promedio_clase_3(vector)
					print(f'Promedio (para prueba): {promedio}')
					mostrar_pasajes_clase_3(vector, promedio)

				else:
					pasaporte = input('Ingrese el pasaporte a buscar: ')
					indice = proceso.buscar_por_pasaporte(vector, pasaporte)
					if indice >= 0:
						clase = validar_en_rango('Ingrese la nueva clase: ', 1, 10)
						vector[indice].clase = clase
						print(vector[indice])
					else:
						print('No se encuentra un pasajero con el Pasaporte indicado.')
			else:
				if len(vector) == 0:
					print('Error: debe generar el vector primero con la opción 1')
				else:
					print('Error: elija bien')
			print()


if __name__ == '__main__':
	inicio()
