class Usuario:
    def __init__(self, codigo, nombre, pwd, dpto):
        self.codigo = codigo
        self.nombre = nombre
        self.password = pwd
        self. departamento = dpto

    def __str__(self):
        linea = '{:<10}\t{:<40}\t{:<12}\n'
        return linea.format(self.codigo, self.nombre, self.departamento)
