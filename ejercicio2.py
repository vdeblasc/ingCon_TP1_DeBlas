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

cont = 1

# Imprimir fila por fila
for fila in matriz:
    print(cont,"|", "  ".join(fila))
    cont +=1