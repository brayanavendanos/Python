# es una función que se manda a llamar a si misma para completar una tarea

# Factorial de 5

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6 
# 5! = 5 * 24
# 5! = 120

def factorial(numero): #numero es el valor del número del cual queremos ejecutar su factorial
    if numero == 1: #si el número que estamos recibiendo es igual a 1 
        return 1 #regresamos el valor de 1
    else:        #de lo contrario 
        return numero * factorial(numero-1) # retornamos el numero qu eestamos recibiendo, lo multiplicamos por el factorial del numero que estamos recibiendo pero -1 
                # 5   *             4
                # de esta forma se repite hasta que llegue al numero 1 y no se vuelve a llamar a uno para aplicar la linea 13 en el return. 

numero = int(input("Escribe el número del cual quieres saber el factorial: "))
resultado = factorial(numero)                

print(f'El factorial de {numero} es {resultado}')


