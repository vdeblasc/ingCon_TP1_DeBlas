"""Ordenamiento de datos con tuplas:
Consigna: Escribe una función que reciba una lista de tuplas donde cada 
tupla contiene un nombre y una puntuación. La función debe devolver la 
lista ordenada por puntuación de mayor a menor.

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
"""
def ordenar_tupla(lista_tuplas):
    lista_tuplas.sort(key=lambda x: x[1], reverse=True)
    return lista_tuplas

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
print(ordenar_tupla(puntuaciones))