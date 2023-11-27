__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('CENSO POBLACIONAL')
print('*' * 80)

# Inicializar contadores y acumuladores
cant_hombres = 0
cant_mujeres = 0
cant_escolares = 0
hay_mayores80 = False

# Primera carga de datos de corte antes del ciclo
sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Proceso repetitivo
while sexo == 'M' or sexo == 'F':
    # Carga de datos que no determinan el corte del ciclo
    edad = int(input('Ingrese edad: '))
    # Proceso
    if sexo == 'M':
        cant_hombres += 1
        if edad > 80:
            hay_mayores80 = True
    else:
        cant_mujeres += 1
        if edad >= 4 and edad <= 18:
            cant_escolares += 1
    # Nueva carga de dato de corte dentro del ciclo
    sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Resultados
print('*' * 80)
if cant_hombres > cant_mujeres:
    print('Hay más hombres que mujeres')
elif cant_mujeres > cant_hombres:
    print('Hay más mujeres que hombres')
else:
    print('La cantidad de mujeres y hombres es igual')
print('Las mujeres en edad escolar son:', cant_escolares)
if hay_mayores80 == True:
    print('Hay hombres mayores a 80 años')
else:
    print('NO hay hombres mayores a 80 años')
