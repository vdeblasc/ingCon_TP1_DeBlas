"""Configuración de una aplicación con **kwargs:
Consigna: Escribe una función que reciba configuraciones opcionales para 
una aplicación como modo oscuro, idioma, notificaciones, etc., 
usando **kwargs. La función debe devolver un diccionario con las 
configuraciones aplicadas.

configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
"""
def configurar_app(**kwargs):
    return(kwargs)

app = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print(app)