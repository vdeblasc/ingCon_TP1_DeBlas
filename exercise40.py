"""Análisis de rendimiento académico con diccionarios y arrays:
Consigna: Una universidad lleva un registro de las calificaciones de los
estudiantes en diferentes materias. Cada estudiante tiene un ID único y
su información se almacena en un diccionario donde la clave es el ID y
el valor es otro diccionario con las materias y sus respectivas 
calificaciones (arrays). Escribe una función que reciba este diccionario 
y devuelva un ranking de estudiantes basado en su promedio general.

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
"""
def calcular_ranking(registro_estudiantes):
    ranking = []
    for id_estudiante, materias in registro_estudiantes.items():
        suma_notas = 0
        cantidad_notas = 0
        for lista_notas in materias.values():
            suma_notas += sum(lista_notas)
            cantidad_notas += len(lista_notas)
        promedio_general = suma_notas / cantidad_notas if cantidad_notas > 0 else 0
        ranking.append((id_estudiante, round(promedio_general, 2)))
    # ordenar de mayor a menor promedio
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking


estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = calcular_ranking(estudiantes)
print("Ranking (ID, promedio):")
for posicion, (id_estudiante, promedio) in enumerate(ranking, start=1):
    print(f"{posicion}. {id_estudiante} → {promedio}")
