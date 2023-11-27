__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Datos

print('DIRECCIÓN DE TRÁNSITO')
patente = input('Ingrese patente (sin espacios intermedios): ')
print('-' * 80)

# Validar formato
ok = True
if len(patente) == 6:
    print('Formato antiguo')
elif len(patente) == 7:
    print('Formato nuevo')
else:
    print('Formato INVÁLIDO!')
    ok = False

# Validar caracteres
if ok:
    pos = 0
    for car in patente:
        if (car >= 'A' and car <= 'Z') or (car >= 'a' and car <= 'z'):
            if len(patente) == 6 and pos >= 3:
                ok = False
            elif len(patente) == 7 and pos >= 2 and pos <= 4:
                ok = False
        elif car >= '0' and car <= '9':
            if len(patente) == 6 and pos <= 2:
                ok = False
            elif len(patente) == 7 and (pos <= 1 or pos >= 5):
                ok = False
        else:
            ok = False
        pos += 1

if ok:
    print('La patente es válida')
else:
    print('La patente NO es válida')
