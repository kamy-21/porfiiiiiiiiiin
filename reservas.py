from enums import EstadoReserva
from historial import HistorialReserva

class Reserva:
    def __init__(self, id_reserva, cliente, vehiculo, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = None
        self.fecha_fin = fecha_fin
        self.estado = EstadoReserva.SOLICITADA
        self.historial = HistorialReserva()

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, valor):
        if valor > self.__fecha_inicio:
            self.__fecha_fin = valor
        else:
            raise ValueError("La fecha de fin debe ser posterior a la fecha de inicio")

    def cambiar_estado(self, nuevo_estado):
        transiciones_validas = {
            EstadoReserva.SOLICITADA: [EstadoReserva.CONFIRMADA, EstadoReserva.CANCELADA],
            EstadoReserva.CONFIRMADA: [EstadoReserva.EN_CURSO, EstadoReserva.CANCELADA],
            EstadoReserva.EN_CURSO: [EstadoReserva.FINALIZADA],
        }
        if nuevo_estado in transiciones_validas.get(self.estado, []):
            self.estado = nuevo_estado
            self.historial.registrar_cambio(nuevo_estado, f"Estado cambiado a {nuevo_estado.value}")
        else:
            raise ValueError(f"Transición inválida desde {self.estado.value} a {nuevo_estado.value}")

    def calcular_costo(self):
        dias = (self.__fecha_fin - self.__fecha_inicio).days
        return self.vehiculo.calcular_costo(dias)
