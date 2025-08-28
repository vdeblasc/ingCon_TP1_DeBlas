# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
# “Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)”

nombre_asociado = str
numero_asociado = int

nombre_asociado = input("Ingrese su nombre: ")
numero_asociado = int(input("Ingrese su número de asociado: "))

print(f"Estimado/a {nombre_asociado}, su numero de asociado es: {numero_asociado}")
