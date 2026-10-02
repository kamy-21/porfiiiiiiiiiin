class Sucursal:
    def __init__(self, id_sucursal, ciudad, direccion):
        self.id_sucursal = id_sucursal
        self.ciudad = ciudad
        self.direccion = direccion
        self.vehiculos = []
        self.reservas = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def registrar_reserva(self, reserva):
        self.reservas.append(reserva)
