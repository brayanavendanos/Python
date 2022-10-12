#Valores por default en los parametros de la función
def sumar(a = 0, b = 0) -> int: #Se añaden valores por default en 0, si no se modifican más adelante, arrojarán siempre sus valores por defecto.
    #se añaden al final de la función el -> int, es una pista para decir que retornará un tipo de dato entero
    #también se puede definir cómo a:int = 0, b:int = 0, pero son indicios nada más para la función, no son obligatorios
    return a + b

resultado = sumar()

print(f'Resultado sumar: {resultado}') #el resultado sigue en 0, por default
#le asignamos otros valores
print(f'Resultado sumar: {sumar(2,8)}') #cambia los valores de a y b