"""
Registro de estudiantes con diccionarios:
Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de 
matrícula y el valor es un diccionario con nombre, edad y calificaciones en distintas 
materias. Escribe una función que reciba el registro de estudiantes y devuelva el promedio 
de calificaciones de un estudiante dado su número de matrícula.

estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}
"""
def promedio_calificaciones(lista_estudiantes, matricula):
    est = lista_estudiantes[matricula]
    calificaciones = est["calificaciones"]
    suma = 0
    cont = 0
    for materia in calificaciones:
        suma += calificaciones[materia]
        cont += 1
    promedio = suma / cont
    return f"EL promedio de {est['nombre']} es: {promedio}"

estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

print(promedio_calificaciones(estudiantes, 101))
print(promedio_calificaciones(estudiantes, 102))

"""
def promedio_estudiante(lista_estudiantes, matricula):
    # Accedo al estudiante usando la clave de matrícula
    datos = lista_estudiantes.get(matricula)
    if not datos:
        return None  # si no existe, devuelvo None
    
    calificaciones = datos["calificaciones"]
    valores = calificaciones.values()
    
    promedio = sum(valores) / len(valores)
    return promedio
"""




