"""Administración de empleados con tuplas y diccionarios:
Consigna: Una empresa quiere administrar la información de sus empleados, 
donde cada empleado se representa como una tupla (nombre, edad, salario). 
Escribe una función que reciba un diccionario donde la clave es el ID del 
empleado y el valor es la tupla con su información. La función debe 
devolver un diccionario con los empleados que ganan más de un salario dado.

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
"""
def filtros_empleados(empleados, salario_limite):
    filtro = {}
    for id_empleados, datos in empleados.items():
        nombre, edad, salario = datos
        if salario > salario_limite:
            filtro[id_empleados] = datos
    return filtro


empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000),
    4: ("Daniela", 20, 5000),
    5: ("Donatella", 30, 6500),
    6: ("Gerardo", 28, 5500),
}

print(filtros_empleados(empleados, 4000))
