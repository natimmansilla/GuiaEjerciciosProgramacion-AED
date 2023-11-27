class AprendizMago:
    def __init__(self, legajo=0, nombre='', apellido='', casa_asignada=-1):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.casa_asignada = casa_asignada

    def __str__(self):
        linea = '{:<8}\t{:<20}\t{:<20}\n'
        return linea.format(self.legajo, self.nombre, self.apellido)


def to_string_casa(casa):
    if casa == 0:
        return 'Griffinfor'
    elif casa == 1:
        return 'Slytherin'
    elif casa == 2:
        return 'Hufflepuff'
    elif casa == 3:
        return 'Ravenclaw'