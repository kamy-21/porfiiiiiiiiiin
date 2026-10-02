from datetime import date
from empresa import Empresa
from sucursal import Sucursal
from cliente import Cliente
from vehiculo import Vehiculo
from enums import TipoVehiculo, EstadoReserva
from reservas import Reserva

empresa = Empresa("Alquiler Express")
sucursal = Sucursal(1, "Mar del Plata", "Av. Colón 1234")
empresa.agregar_sucursal(sucursal)

auto = Vehiculo("ABC123", "Toyota", "Corolla", TipoVehiculo.AUTO, 10000)
moto = Vehiculo("XYZ789", "Honda", "Wave", TipoVehiculo.MOTO, 5000)
sucursal.agregar_vehiculo(auto)
sucursal.agregar_vehiculo(moto)

cliente = Cliente("name", "surname", "40123456", "2234567890", "name@mail.com")
reserva = Reserva(1, cliente, auto, date(2026, 10, 1), date(2026, 10, 5))
cliente.registrar_reserva(reserva)
sucursal.registrar_reserva(reserva)

print("Costo total del alquiler:", reserva.calcular_costo())
reserva.cambiar_estado(EstadoReserva.CONFIRMADA)
reserva.cambiar_estado(EstadoReserva.EN_CURSO)
reserva.cambiar_estado(EstadoReserva.FINALIZADA)

print("Historial de cambios:")
for registro in reserva.historial.registros:
    print(f"{registro.fecha} - {registro.estado.value} - {registro.descripcion}")
