"""Simulación de ventas con tuplas, arrays, y *args:
Consigna: Una empresa quiere simular las ventas de diferentes productos.
Escribe una función que reciba un número variable de ventas (tuplas) 
donde cada tupla contiene el producto, la cantidad vendida, y el precio 
por unidad. La función debe devolver el total de ingresos generados por 
las ventas.
simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), 
("Producto C", 3, 50.0))
"""

def simular_ventas(*args):
    total_ingresos = 0
    for venta in args:
        producto, cantidad, precio_unitario = venta
        total_ingresos += cantidad * precio_unitario
    return total_ingresos

ventas = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
    )
print(f"Total de ingresos generados por las ventas: ${ventas}")