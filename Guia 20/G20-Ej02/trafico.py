class Trafico:
    def __init__(self, ip_origen, ip_destino, tamanio):
        self.direccion_origen = ip_origen
        self.direccion_destino = ip_destino
        self.tamanio = tamanio

    def __str__(self):
        r = 'La dirección ' + self.direccion_origen
        r += ' envió ' + str(self.tamanio)
        r += ' bytes de información a la siguiente dirección: ' + self.direccion_destino
        return r
