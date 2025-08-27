"""Registro de notas con tuplas y arrays:
Consigna: Escribe una función que reciba una lista de tuplas donde cada 
tupla contiene el nombre de un estudiante y sus calificaciones en un array.
La función debe devolver un diccionario con el nombre del estudiante como
clave y su promedio de calificaciones como valor.

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
"""
def promedio_estudiantes(notas_estudiantes):
    promedio = {}
    for nombre, notas in notas_estudiantes:
        promedio[nombre] = round(sum(notas) / len(notas), 3)
    return promedio

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
print(promedio_estudiantes(notas_estudiantes))