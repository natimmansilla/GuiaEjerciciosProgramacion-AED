__author__ = 'Algoritmos y Estructuras de Datos'


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóú'


def es_letra(car):
    if (car >= 'a' and car <= 'z') or (car >= 'A' and car <= 'Z'):
        return True
    else:
        return False


def es_consonante(car):
    if es_letra(car) and not es_vocal(car):
        return True
    else:
        return False


def calcular_porcentaje(cant, total):
    if total != 0:
        return cant * 100 / total
    else:
        return 0


def principal():
    texto = input('Ingrese texto: ')
    # Variables dentro de la palabra (debemos reiniciarlos al terminar la misma)
    letras_pal = vocales = 0
    tiene_cons2da = False
    empieza_vp = False
    tiene_ga = False
    # Variables para el texto (no se reinician)
    anterior = ''
    pals_3voc4let = 0
    men_cons2da = None
    pals_vp_na = 0
    pals_ga = 0
    palabras = 0
    for car in texto:
        if car != ' ' and car != '.':
            # Dentro de la palabra
            letras_pal += 1
            if es_vocal(car):
                vocales += 1
            if letras_pal == 2 and es_consonante(car):
                tiene_cons2da = True
            if letras_pal == 1 and (car == 'v' or car == 'p'):
                empieza_vp = True
            if anterior == 'g' and car == 'a':
                tiene_ga = True
        else:
            # Final de la palabra
            palabras += 1
            if vocales >= 3 and letras_pal > 4:
                pals_3voc4let += 1
            if tiene_cons2da:
                # Buscar palabra más corta
                if men_cons2da is None:
                    men_cons2da = letras_pal
                elif letras_pal < men_cons2da:
                    men_cons2da = letras_pal
            if empieza_vp and (anterior == 'n' or anterior == 'a'):
                pals_vp_na += 1
            if tiene_ga:
                pals_ga += 1
            # Reiniciamos variables de palabra
            letras_pal = vocales = 0
            tiene_cons2da = False
            empieza_vp = False
            tiene_ga = False
        anterior = car
    # La universidad es una etapa más de la vida.
    print('Palabras que tenían por lo menos tres vocales y más de cuatro letras:', pals_3voc4let)
    # Vamos Argentina el sabado contra Francia.
    if men_cons2da is None:
        print('No había palabras con una consonante en la segunda posición')
    else:
        print('Longitud de la palabra más corta de entre las que contenían una consonante en la segunda posición:',
              men_cons2da)
    # Ahora que vengan y nos ganen si pueden.
    print('Palabras empiezan con "v" o con "p" y terminan con "n" o con "a":', pals_vp_na)
    porcentaje = calcular_porcentaje(pals_ga, palabras)
    print('Porcentaje de palabras que contenían la expresión "ga" con respecto al total del palabras del texto:',
          round(porcentaje, 2), '%')


if __name__ == '__main__':
    principal()