class AnalisisTermico:
    def __init__(self, region, mes, maxima, minima):
        self.region = region
        self.mes = mes
        self.temperatura_maxima = maxima
        self.temperatura_minima = minima

    def __str__(self):
        r = 'Region: ' + self.region
        r += ' - Mes: ' + str(self.mes)
        r += ' - Maxima: ' + str(self.temperatura_maxima)
        r += ' - Minima: ' + str(self.temperatura_minima)
        return r
    