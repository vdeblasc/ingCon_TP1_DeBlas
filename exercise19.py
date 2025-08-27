"""Análisis de resultados deportivos con diccionarios:
Consigna: Un club deportivo registra los resultados de sus partidos en un 
diccionario donde la clave es el nombre del equipo rival y el valor es 
una tupla con los goles anotados y recibidos. Escribe una función que 
calcule el total de goles anotados y recibidos en la temporada.

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}
"""
def calcular_goles(marcadores):
    goles_anotados = 0
    goles_recibidos = 0
    for rival, marcadores in marcadores.items():
        goles_anotados += marcadores[0]
        goles_recibidos += marcadores[1]
    return f"Total de goles anotados: {goles_anotados}\nTotal de goles recibidos: {goles_recibidos}"

resultados = {
    "Talleres": (3, 2),
    "Don Orione": (2, 4),
    "Regatas": (2, 2),
    "Cementista": (1, 1),
    "San Martin": (3, 1),
    "Jockey": (1, 3)
}
print(calcular_goles(resultados))

"""def calcular_goles(resultados):
    goles_favor = 0
    goles_contra = 0

    for rival, marcador in resultados.items():
        goles_favor += marcador[0]   # primer valor de la tupla
        goles_contra += marcador[1]  # segundo valor de la tupla

    return {"goles_favor": goles_favor, "goles_contra": goles_contra}
# Ejemplo de uso
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}
totales = calcular_goles(resultados)
print(totales)
# Salida esperada: {'goles_favor': 8, 'goles_contra': 3}"""