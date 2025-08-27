"""Estadísticas de ventas con arrays:
Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un 
diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]"""

def estadisticas_ventas(ventas):
    total_ventas = 0
    promedio = 0
    mayor_venta = ventas[0]
    for venta in ventas:
        total_ventas += venta
        promedio = round(total_ventas / len(ventas),3)
        if venta > mayor_venta:
            mayor_venta = venta
    return {"total_ventas": total_ventas, "promedio_mensual": promedio, "mayor_venta": mayor_venta}

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

print(estadisticas_ventas(ventas_mensuales))

   
