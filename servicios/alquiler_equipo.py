
from servicios.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):

        super().__init__(nombre, precio_base)

        if dias <= 0:
            raise ValueError("Días inválidos")

        self.dias = dias

    def calcular_costo(self):

        return self.precio_base * self.dias

    def descripcion(self):

        return f"Equipo alquilado por {self.dias} días"