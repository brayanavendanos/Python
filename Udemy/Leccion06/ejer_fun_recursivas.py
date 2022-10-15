"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

Si se pasan valores negativos no imprime nada
"""

def imprimir_numero_recursivo(numero): # definimos función
    if numero >= 1:                     # si numero es igual o mayor que 1, debe seguir
        print(numero)                   # imprimiendo el numero que se pone en el input que es el parametro de la función
        imprimir_numero_recursivo(numero - 1)  # y debe continuar llamando la funcion para restar el 1 y volver a empezar.
    elif numero == 0: # si es igual a cero
        return        # se debe regresar a la función nuevamente
    elif numero <= 0: # en caso de que sea menor que cero (negativo) debe imprimir este error
        print("El numero que ingreses debe ser positivo")
        

numero = int(input("Escribe el número: "))
imprimir_numero_recursivo(numero)        