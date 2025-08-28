"""Simulación de mercado bursátil con arrays y tuplas:
Consigna: Escribe una función que simule el comportamiento de acciones 
en un mercado bursátil. La función debe recibir un array con los precios 
diarios de una acción y una lista de tuplas donde cada tupla contiene un 
día y un precio de compra o venta. La función debe devolver el beneficio 
o pérdida total si las acciones se hubieran comprado y vendido en los 
días especificados.

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
"""
def simular_mercado(precios, operaciones):
    beneficio = 0
    precio_compra = None
    
    for operacion, dia in operaciones:
        if operacion == "compra":
            precio_compra = precios[dia]   # guardamos el precio de compra
        elif operacion == "venta" and precio_compra is not None:
            beneficio += precios[dia] - precio_compra
            precio_compra = None           # después de vender ya no tenemos acciones
    return beneficio


precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = simular_mercado(precios_diarios, operaciones)
print("Beneficio total:", resultado)
