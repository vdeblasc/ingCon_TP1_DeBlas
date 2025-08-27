"""Análisis financiero con **kwargs:
Consigna: Escribe una función que reciba diferentes tipos de ingresos y 
gastos como **kwargs y calcule el balance final. La función debe manejar 
ingresos como positivos y gastos como negativos.

analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, 
freelance=500)
"""
def analizar_finanzas(**kwargs):
    balance = 0
    ingresos = 0
    gastos = 0
    for accion, monto in kwargs.items():
        if monto > 0:
            ingresos += monto
        else:
            gastos += monto
        balance += monto
    return f"El balance final es: {balance} \nTotal de ingresos: {ingresos} \nTotal de gastos: {gastos}"

finanzas = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(finanzas)
