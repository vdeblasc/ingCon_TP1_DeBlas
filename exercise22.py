"""Planificación de viajes con tuplas y diccionarios:
Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, 
cada uno representado como una tupla (destino, precio, duración en días).
Escribe una función que reciba una lista de estos paquetes y devuelva un 
diccionario con los destinos como claves y el precio total 
(precio por día * duración) como valor.

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]
"""
def planificar_viajes(presupuesto_paquetes):
    viajes = {}
    for destino, precio, dias in presupuesto_paquetes:
        precio_total = precio * dias
        viajes[destino] = precio_total
    return viajes

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

print(planificar_viajes(paquetes))

"""for paquete in presupuesto_paquetes:
    destino = paquete[0]
    precio_total = paquete[1] * paquete[2]
    viajes[destino] = precio_total"""
