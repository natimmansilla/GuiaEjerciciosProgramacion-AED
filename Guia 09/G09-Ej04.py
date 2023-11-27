__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Validacion de Datos de Personas')
print('=' * 60)
print('\n')
menu = 'Menu de Opciones \n' \
       '----------------------------- \n' \
       '1 ----------- Validar Cuit\n' \
       '2 ----------- Validar DNI\n' \
       '0 ----------- Salir\n' \
       'Ingrese su opcion: '

opcion = -1
while opcion != 0:
	opcion = int(input(menu))
	if opcion == 1:
		ok = True
		cuit = input('Ingrese el cuit de la persona que desea validadar: ')

		if len(cuit) != 13:
			ok = False
		elif cuit[2] != '-' or cuit[-2] != '-':
			ok = False
		else:
			multiplicador = 5
			acumulador = 0
			for pos in range(len(cuit) - 1):
				digito = cuit[pos]
				if digito != '-':
					if '0' <= digito <= '9':
						numero = int(digito)
						acumulador += numero * multiplicador
						multiplicador -= 1
						if multiplicador == 1:
							multiplicador = 7
					else:
						ok = False
						break

			if ok:
				resto = acumulador % 11
				verificador = 11 - resto

				if verificador == 11:
					verificador = 0
				elif verificador == 10:
					verificador = 9

				verificadorIngresado = int(cuit[-1])
				if verificador != verificadorIngresado:
					ok = False

		if not ok:
			print('El CUIT ingresado es invalido')
		else:
			print('CUIT Validado correctamente')

	elif opcion == 2:

		ok = True
		dni = input('Ingrese el DNI de la persona que desea validadar: ')

		if len(dni) != 10:
			ok = False
		elif dni[2] != '.' or dni[-4] != '.':
			ok = False
		else:
			for digito in dni:
				if '0' > digito > '9':
					ok = False
					break
		if not ok:
			print('El DNI ingresado es invalido')
		else:
			print('DNI Validado correctamente')
