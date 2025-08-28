"""Gestión de inventario con arrays:
Consigna: Una tienda maneja su inventario de productos en un array donde 
cada índice representa un producto específico y su valor es la cantidad 
disponible. Escribe una función que reciba el array de inventario y 
un número de productos vendidos (otro array) y devuelva el inventario 
actualizado.

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]
"""
def actualizar_inventario(stock, venta):
    inventario_actualizado = []
    for i in range(len(stock)):
        inventario_actualizado.append(stock[i] - venta[i])
        # stock[i] -= venta[i]
    #return stock
    return inventario_actualizado

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

print(actualizar_inventario(inventario, ventas))