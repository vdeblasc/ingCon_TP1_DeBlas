"""
Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs:
Consigna: Escribe una función que gestione el inventario de una cadena de
tiendas. La función debe recibir el nombre de la tienda, el producto y 
la cantidad a actualizar usando **kwargs. Debe manejar un diccionario
donde la clave es el nombre de la tienda y el valor es otro diccionario 
con los productos y sus cantidades. La función debe actualizar el 
inventario y devolver el estado actual.

inventario = {

    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
"""
from pprint import pprint

inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(tienda, **kwargs):
    if tienda not in inventario:
        inventario[tienda] = {}  # si la tienda no existe, la creamos
    
    for producto, cantidad in kwargs.items():
        if producto in inventario[tienda]:
            inventario[tienda][producto] += cantidad
        else:
            inventario[tienda][producto] = cantidad
    return inventario


actualizar_inventario(tienda = "Tienda A", producto_1 = 10, producto_2 = -5)
actualizar_inventario(tienda = "Tienda B", producto_1 = -5, producto_2 = 25)

print("Estado actualizado del inventario:")
pprint(inventario)