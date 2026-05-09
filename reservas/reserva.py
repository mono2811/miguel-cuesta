

from excepciones.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError("Costo inválido")

            self.estado = "Confirmada"

            return f"Reserva confirmada. Total: {costo}"

        except Exception as e:

            self.estado = "Error"

            raise ReservaError(
                "Error al confirmar reserva"
            ) from e

    def cancelar(self):

        self.estado = "Cancelada"