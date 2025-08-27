"""Organización de una biblioteca con diccionarios:
Consigna: Una biblioteca registra sus libros en un diccionario donde la 
clave es el título del libro y el valor es otro diccionario con la 
información del autor, año de publicación, y género. Escribe una función 
que reciba este diccionario y devuelva una lista de todos los libros
publicados después del año 2000.

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}
"""
def biblioteca_post_dosmil(biblioteca):
    libros_post_dosmil = []
    for titulo, info in biblioteca.items():
        if info["año"] > 2000:
            libros_post_dosmil.append(titulo)
    return libros_post_dosmil

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}
print(biblioteca_post_dosmil(biblioteca))