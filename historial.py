from datetime import datetime

class RegistroHistorial:
    def __init__(self, estado, descripcion):
        self.fecha = datetime.now()
        self.estado = estado
        self.descripcion = descripcion

class HistorialReserva:
    def __init__(self):
        self.registros = []

    def registrar_cambio(self, estado, descripcion):
        registro = RegistroHistorial(estado, descripcion)
        self.registros.append(registro)
