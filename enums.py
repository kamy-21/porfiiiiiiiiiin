from enum import Enum

class TipoVehiculo(Enum):
    AUTO = "auto"
    CAMIONETA = "camioneta"
    MOTO = "moto"

class EstadoVehiculo(Enum):
    DISPONIBLE = "disponible"
    RESERVADO = "reservado"
    EN_ALQUILER = "en alquiler"
    FUERA_DE_SERVICIO = "fuera de servicio"

class EstadoReserva(Enum):
    SOLICITADA = "solicitada"
    CONFIRMADA = "confirmada"
    EN_CURSO = "en curso"
    FINALIZADA = "finalizada"
    CANCELADA = "cancelada"
