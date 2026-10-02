from enums import TipoVehiculo, EstadoVehiculo

class Vehiculo:
    def __init__(self, patente, marca, modelo, tipo, tarifa_base):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.estado = EstadoVehiculo.DISPONIBLE
        self.__tarifa_base = None
        self.tarifa_base = tarifa_base

    @property
    def tarifa_base(self):
        return self.__tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if valor > 0:
            self.__tarifa_base = valor
        else:
            raise ValueError("La tarifa base debe ser mayor a 0")

    def calcular_costo(self, dias):
        if self.tipo == TipoVehiculo.AUTO:
            return self.__tarifa_base * dias
        elif self.tipo == TipoVehiculo.CAMIONETA:
            return self.__tarifa_base * dias * 1.2
        elif self.tipo == TipoVehiculo.MOTO:
            return self.__tarifa_base * dias * 0.85

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
