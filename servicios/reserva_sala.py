# Importa clase Servicio
from servicios.servicio import Servicio


# Clase ReservaSala hereda de Servicio
class ReservaSala(Servicio):

# Constructor
    def __init__(self, nombre, precio_base, horas):

# Llama constructor padre
        super().__init__(nombre, precio_base)

# Validación horas
        if horas <= 0:
            raise ValueError("Horas inválidas")

# Atributo horas
        self.horas = horas

# Calcula costo total
    def calcular_costo(self):

        return self.precio_base * self.horas

# Retorna descripción
    def descripcion(self):

        return f"Sala reservada por {self.horas} horas"