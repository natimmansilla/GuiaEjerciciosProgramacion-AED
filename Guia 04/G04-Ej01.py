__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Generador de dirección de Mail
# Entrada:
# Nombre
# Apellido
# Dominio
# Salida:
# Dirección de mail propuesta

print('#' * 30)
print('# ' + 'Generador de Mails' + \
      (' ' * (30 - (len('Generador de Mails') + 5))) + '#')
print('#' * 30)

print('\nIngreso de datos:')
nombre = input('\tNombre : ')
apellido = input('\tApellido: ')
dominio = input('\tDominio : ')

# transformar las cadenas ingresadas en minúscula
# independientemente de cómo se ingresaron.
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()
primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_apellido != primera_letra_nombre:
    mail_propuesto = primera_letra_nombre + apellido + '@' + \
                     dominio
else:
    mail_propuesto = nombre + '.' + apellido + '@' + dominio

print()
print('Mail propuesto:\n\t', mail_propuesto)
print('#' * 30)

input('\nPresione enter para finalizar...')
