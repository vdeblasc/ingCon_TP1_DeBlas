"""Análisis de resultados de encuestas con diccionarios y arrays:
Consigna: Una empresa realiza encuestas de satisfacción y registra las 
respuestas en un diccionario donde la clave es la pregunta y el valor es 
un array con las respuestas recibidas. Escribe una función que calcule la 
frecuencia de cada respuesta para cada pregunta y devuelva un 
diccionario con estos resultados.

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
"""
def analizar_encuestas(encuestas):
    resultados = {}
    for pregunta, respuestas in encuestas.items():
        cont = {}  # acá guardamos cuántas veces aparece cada respuesta
        for r in respuestas:
            if r not in cont:
                cont[r] = 1
            else:
                cont[r] += 1
        resultados[pregunta] = cont
    return resultados


encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultado = analizar_encuestas(encuestas)
print(resultado)
