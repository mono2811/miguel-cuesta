#Clase abstracta
# Importa herramientas para crear clases abstractas
from abc import ABC, abstractmethod



# Clase abstracta Persona
# Sirve como base para otras clases
class Persona(ABC):

    def __init__(self, nombre, documento):
        self._nombre = nombre
        self._documento = documento

    @abstractmethod
    def mostrar_info(self):
        pass