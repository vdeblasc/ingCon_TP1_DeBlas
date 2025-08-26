"""
Análisis de datos meteorológicos con arrays:
Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena 
en un array. Escribe una función que reciba este array y devuelva la 
temperatura media del mes, la máxima y la mínima.
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
"""
def analisis_temperaturas(lista_temperaturas):
    suma = lista_temperaturas[0]
    temp_max = lista_temperaturas[0]
    temp_min = lista_temperaturas[0]
    for i in range(1, len(lista_temperaturas)):
        temp = lista_temperaturas[i]
        suma += temp
        temp_media = suma / len(lista_temperaturas)
        if lista_temperaturas[i] > temp_max:
            temp_max = lista_temperaturas[i]
        if lista_temperaturas[i] < temp_min:
            temp_min = lista_temperaturas[i]
    return f"La temperatura media es: {temp_media}, la máxima es: {temp_max} y la mínima es: {temp_min}"

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

print(analisis_temperaturas(temperaturas))

"""def analisis_temperaturas(lista_temperaturas):
    temp_media = sum(lista_temperaturas) / len(lista_temperaturas)
    temp_max = max(lista_temperaturas)
    temp_min = min(lista_temperaturas)
    return f"La temperatura media es: {temp_media}, la máxima es: {temp_max} y la mínima es: {temp_min}"""