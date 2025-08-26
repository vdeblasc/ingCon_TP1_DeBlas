#Crea un código que imprima en pantalla la siguiente expresión. 
#1 | A B C
#2 | D E F
#3 | G H I

# Definir matriz como lista de listas
matriz = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]



# Imprimir fila por fila
for i, fila in enumerate(matriz, start=1):
    print(i, "|", "  ".join(fila))
    