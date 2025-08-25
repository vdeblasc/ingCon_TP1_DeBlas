def suma(a,b):
    return a+b
print(suma(5,6,))

def suma_args(*args):
    return sum(args)

def suma_args(*args):

    # funciona de la misma manera
    total = 0
    for arg in args:
        total += arg
    return total