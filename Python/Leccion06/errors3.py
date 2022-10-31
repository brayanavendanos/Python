"""Creamos una función en donde cada elemento de
una lista es dividida por un divisor definido"""
def divide_elementos_de_lista(lista, divisor):
    
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))