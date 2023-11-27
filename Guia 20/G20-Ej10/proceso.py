import clase


def generar_datos(vector, n):
	contador = 0
	while contador < n:
		reg = clase.crear_pasaje_aleatorio()
		ind = buscar_por_pasaporte(vector, reg.pasaporte)
		if ind == -1:
			vector.append(reg)
			contador += 1


def ordenar_por_monto(vector):
	for i in range(len(vector)-1):
		for j in range(i+1, len(vector)):
			if vector[i].monto < vector[j].monto:
				vector[i], vector[j] = vector[j], vector[i]


def acumular_por_clase(vector):
	acumuladores = [0] * 10

	for pasaje in vector:
		clase = pasaje.clase
		indice_acumulador = clase - 1
		acumuladores[indice_acumulador] += pasaje.monto

	return acumuladores


def calcular_promedio_clase_3(vector):
	acum = 0
	contador = 0
	promedio = 0

	for pasaje in vector:
		if pasaje.clase == 3:
			acum += pasaje.monto
			contador += 1

	if contador > 0:
		promedio = acum / contador
	return promedio


def buscar_por_pasaporte(vector, pasaporte):
	ind = -1
	for i in range(len(vector)):
		if vector[i].pasaporte == pasaporte:
			ind = i
			break
	return ind
