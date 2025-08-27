"""Organización de eventos con *args:
Consigna: Escribe una función que reciba un número variable de nombres 
de eventos y los imprima en un formato de lista numerada. Utiliza *args 
para recibir los nombres de los eventos.

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")"""

def organizar_eventos(*args):
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")