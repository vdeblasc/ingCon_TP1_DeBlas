"""Sistema de reservas con tuplas y diccionarios:
Consigna: Un hotel maneja sus reservas utilizando un diccionario donde 
la clave es la fecha y el valor es una lista de tuplas, cada tupla 
contiene el nombre del huésped, la habitación asignada y el precio. 
Escribe una función que permita hacer una nueva reserva verificando 
primero si la habitación está disponible en la fecha seleccionada.

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
"""
from pprint import pprint

# Diccionario con reservas iniciales
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

# Función: verifica si la habitación está libre y agrega la reserva
def nueva_reserva(reservas, fecha, nombre, habitacion, precio):
    if fecha not in reservas:
        reservas[fecha] = []
    
    for _, hab, _ in reservas[fecha]:
        if hab == habitacion:
            return False  # habitación ocupada
    
    reservas[fecha].append((nombre, habitacion, precio))
    return True

# Lista de intentos de reserva
intentos = [
    ("2024-08-15", "María", 101, 150),
    ("2024-08-15", "María", 103, 170),
    ("2024-08-17", "Pedro", 101, 150),
    ("2024-08-16", "Ana", 101, 150)
]

# Ejecutar intentos y mostrar resultado
for fecha, nombre, habitacion, precio in intentos:
    if nueva_reserva(reservas, fecha, nombre, habitacion, precio):
        print(f"{fecha} - Habitación {habitacion}: RESERVA REALIZADA con éxito para {nombre}")
    else:
        print(f"{fecha} - Habitación {habitacion}: YA ESTÁ OCUPADA, no se pudo reservar")

print("\nEstado final de las reservas:")
pprint(reservas)

