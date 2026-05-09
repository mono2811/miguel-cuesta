
# Importa la clase Persona
from entidades.persona import Persona

# Clase Cliente hereda de Persona
class Cliente(Persona):

# Constructor de la clase Cliente
    def __init__(self, nombre, documento, correo):
        
# Llama al constructor de Persona
        super().__init__(nombre, documento)

# Valida que el correo contenga @
        if "@" not in correo:
            raise ValueError("Correo inválido")
        
# Encapsulación del correo
        self.__correo = correo
        
# Método para mostrar información del cliente
    def mostrar_info(self):

        return f"Cliente: {self._nombre}"
    
# Getter para obtener el correo privado
    def get_correo(self):

        return self.__correo