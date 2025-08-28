"""Administración de suscripciones con diccionarios, arrays, y **kwargs:
Consigna: Escribe una función que gestione las suscripciones a un servicio
en línea. La función debe recibir el nombre del usuario, el tipo de 
suscripción (mensual, anual), y cualquier o	tra opción adicional usando
**kwargs. La función debe actualizar un diccionario que almacene el 
historial de suscripciones de los usuarios y devolver el estado 
actualizado.

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
actualizar_suscripcion(usuario="Luis", suscripcion="mensual", 
auto_renovacion=True)
"""
from pprint import pprint

# Diccionario inicial
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    # si el usuario no existe, se crea
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    
    # si la suscripción no está, se agrega
    if suscripcion not in suscripciones[usuario]:
        suscripciones[usuario].append(suscripcion)
    
    # procesar opciones extra (ej: auto_renovacion, descuentos, etc.)
    if kwargs:
        suscripciones[usuario].append(kwargs)
    
    return suscripciones


resultado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)

print("Estado actualizado de las suscripciones:")
pprint(resultado)


