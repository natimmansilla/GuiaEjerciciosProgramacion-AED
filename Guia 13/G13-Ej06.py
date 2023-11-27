__author__ = 'Algoritmos y Estructuras de Datos'


def calcular_promedio(suma, cantidad):
    prom = 0
    if cantidad != 0:
        prom = round(suma / cantidad, 2)
    return prom


def principal():
    letras_pal = cp4ln = palabras_t = letras_palt = palabras_as = palabras_re = 0
    tiene_n = empieza_t = tiene_a = tiene_s = tiene_e = tiene_r = tiene_re = False
    ultima_letra = ''
    texto = input('Ingrese el texto, debe finalizar con punto: ')
    for letra in texto:
        if letra == ' ' or letra == '.':

            if letras_pal > 4 and tiene_n:
                cp4ln += 1

            if empieza_t:
                letras_palt += letras_pal
                palabras_t += 1

            if not tiene_e and tiene_a and tiene_s:
                palabras_as += 1

            if tiene_re and (ultima_letra == 'o' or ultima_letra == 'O'):
                palabras_re += 1

            letras_pal = 0
            tiene_n = empieza_t = tiene_a = tiene_s = tiene_e = tiene_r = False
        else:

            letras_pal += 1
            if letra == 'n' or letra == 'N':
                tiene_n = True

            if letras_pal == 1 and (letra == 't' or letra == 'T'):
                empieza_t = True

            if letra == 'a' or letra == 'A':
                tiene_a = True

            if letra == 's' or letra == 's':
                tiene_s = True

            if letra == 'e' or letra == 'E':
                tiene_e = True

            if letra == 'r' or letra == 'R':
                tiene_r = True
            else:
                if tiene_r and (letra == 'e' or letra == 'E'):
                    tiene_re = True
                tiene_r = False
            ultima_letra = letra

    print('La cantidad de palabras con mas de cuatro letras y '
          'contienen \"n\" son:', cp4ln)
    promedio = calcular_promedio(letras_palt, palabras_t)
    print('El promedio de letras por palabra entre las que '
          'comenzaban con \"t\" es', promedio)
    print('La cantidad palabras contenían una \"a\" y también una \"s\", pero no '
          'contenían una \"e\" son:', palabras_as)
    print('La cantidad palabras contenían  al menos una vez la expresión "re" pero'
          ' terminaban con la letra "o" son:', palabras_re)


if __name__ == '__main__':
    principal()
