"""Optimización de rutas con arrays y tuplas:
Consigna: Una empresa de logística necesita optimizar sus rutas de 
entrega. Cada ruta se representa como una tupla 
(origen, destino, distancia). Escribe una función que reciba una lista de
rutas y un array con las distancias máximas permitidas para cada ruta. 
La función debe devolver las rutas que cumplen con las restricciones.

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]
"""
def filtrar_rutas(rutas, distancias_max):
    rutas_validas = []
    for i in range(len(rutas)):
        origen, destino, distancia = rutas[i]
        if distancia <= distancias_max[i]:
            rutas_validas.append(rutas[i])
    return rutas_validas


rutas = [("Madrid", "Barcelona", 620),
         ("Madrid", "Valencia", 350),
         ("Barcelona", "Valencia", 350)]

distancias_max = [600, 400, 500]

resultado = filtrar_rutas(rutas, distancias_max)
print(resultado)

