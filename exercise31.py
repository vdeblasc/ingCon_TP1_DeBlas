"""Gestión de una red social con **kwargs y arrays:
Consigna: Escribe una función que administre publicaciones de una red 
social. La función debe recibir el nombre del usuario, el texto de la 
publicación y un número variable de etiquetas usando **kwargs y arrays.
Además, debe manejar opciones adicionales como visibilidad pública o 
privada. La función debe devolver un diccionario con todos los detalles 
de la publicación.

publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], 
visibilidad="publica", likes=100)
"""
from pprint import pprint

def publicar (usuario, texto, etiquetas, **kwargs):
    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": etiquetas
    }

    publicacion.update(kwargs)
    return publicacion

post = publicar("Juan",
                "Mi primer post!",
                etiquetas=["#hola", "#primerPost"],
                visibilidad="publica",
                likes=100
                )

pprint(post)
