"""Procesamiento de ventas con arrays:
Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un 
array. Escribe una función que reciba el array de ventas diarias y 
devuelva el total de ventas y el promedio de ventas por día.

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
"""

def ventas (ventas_dia):
    suma = ventas_dia[0]
    for i in range(1, len(ventas_dia)):
        suma += ventas_dia[i]
        total_ventas = suma
        promedio_ventas = total_ventas / len(ventas_dia)
    return f"El total de ventas es: {total_ventas} \nEl promedio de ventas por dia es: {promedio_ventas}"

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
print(ventas(ventas_diarias)) 
