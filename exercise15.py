"""Manejo de parámetros variables con *args:
Consigna: Escribe una función que reciba un número variable de notas de estudiantes y 
devuelva la nota promedio. Utiliza *args para recibir las notas.
calcular_promedio(85, 90, 78, 92)
"""

def calcular_promedio_arg(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma / len(args)

notas = (85, 90, 78, 92)

print(calcular_promedio_arg(*notas))
