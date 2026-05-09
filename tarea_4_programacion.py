
# IMPORTACIÓN DE CLASES Y MÓDULOS

from entidades.cliente import Cliente
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from reservas.reserva import Reserva

import logging


# CONFIGURACIÓN DEL ARCHIVO DE REGISTRO LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# MENSAJE INICIAL DEL SISTEMA


print("\n===== SOFTWARE FJ =====\n")

# OPERACIÓN 1 CREACIÓN DE CLIENTE VÁLIDO
try:

    cliente1 = Cliente(
        "Miguel",
        "12345",
        "miguel@gmail.com"
    )

    print(cliente1.mostrar_info())

except Exception as e:

    logging.error(e)
    print("Error:", e)

# OPERACIÓN 2 CREACIÓN DE OTRO CLIENTE
try:

    cliente2 = Cliente(
        "juan",
        "2222",
        "juan@gmail.com"
    )

    print(cliente2.mostrar_info())

except Exception as e:

    logging.error(e)
    print("Error:", e)


# OPERACIÓN 3 CLIENTE CON CORREO INVÁLIDO
try:

    cliente3 = Cliente(
        "Pedro",
        "3333",
        "correo_invalido"
    )

except Exception as e:

    logging.error(e)
    print("Error cliente:", e)


# OPERACIÓN 4 CREACIÓN DE SERVICIO DE SALA
try:

    sala = ReservaSala(
        "Sala VIP",
        50000,
        3
    )

    print(sala.descripcion())
    print("Costo:", sala.calcular_costo())

except Exception as e:

    logging.error(e)
    print("Error:", e)
    
    

# OPERACIÓN 5 ALQUILER DE EQUIPO
try:

    equipo = AlquilerEquipo(
        "Portátil",
        30000,
        5
    )

    print(equipo.descripcion())
    print("Costo:", equipo.calcular_costo())

except Exception as e:

    logging.error(e)
    print("Error:", e)


# OPERACIÓN 6 SERVICIO DE ASESORÍA
try:

    asesoria = Asesoria(
        "Asesoría IA",
        80000,
        "premium"
    )

    print(asesoria.descripcion())
    print("Costo:", asesoria.calcular_costo())

except Exception as e:

    logging.error(e)
    print("Error:", e)



# OPERACIÓN 7 RESERVA EXITOSA
try:

    reserva1 = Reserva(cliente1, sala)

    print(reserva1.confirmar())

except Exception as e:

    logging.error(e)
    print("Error reserva:", e)




# OPERACIÓN 8 SEGUNDA RESERVA EXITOSA
try:

    reserva2 = Reserva(cliente2, equipo)

    print(reserva2.confirmar())

except Exception as e:

    logging.error(e)
    print("Error reserva:", e)




# OPERACIÓN 9 SERVICIO CON PRECIO INVÁLIDO
try:

    servicio_error = ReservaSala(
        "Sala Error",
        -500,
        2
    )

except Exception as e:

    logging.error(e)
    print("Error servicio:", e)




# OPERACIÓN 10 HORAS INVÁLIDAS
try:

    sala_error = ReservaSala(
        "Sala Mala",
        1000,
        0
    )

except Exception as e:

    logging.error(e)
    print("Error horas:", e)




# OPERACIÓN 11 CANCELACIÓN DE RESERVA
try:

    reserva2.cancelar()

    print("Reserva cancelada correctamente")

except Exception as e:

    logging.error(e)
    print("Error cancelando:", e)




# OPERACIÓN 12 TRY / EXCEPT / ELSE / FINALLY
try:

    numero = 10
    resultado = numero / 2

except Exception as e:

    logging.error(e)
    print("Error matemático:", e)

else:

    print("Resultado división:", resultado)

finally:

    print("Fin de operaciones del sistema")