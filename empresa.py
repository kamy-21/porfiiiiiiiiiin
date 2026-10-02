class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)
