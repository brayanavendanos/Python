""" 
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *arg como parámetro de la función y 
regresar como resultado la multiplicación de todos los valores pasados como argumentos
"""

def multiplicar_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

print(multiplicar_valores(3,2,2,2,3))

