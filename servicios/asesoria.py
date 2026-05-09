

from servicios.servicio import Servicio

class Asesoria(Servicio):

    def __init__(self, nombre, precio_base, nivel):

        super().__init__(nombre, precio_base)

        self.nivel = nivel

    def calcular_costo(self):

        if self.nivel.lower() == "premium":
            return self.precio_base * 2

        return self.precio_base

    def descripcion(self):

        return f"Asesoría nivel {self.nivel}"