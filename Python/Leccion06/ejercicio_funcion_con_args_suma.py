""" 
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""

#definimos nuestra función 
def sumar_valores(*args): #si se usan argumentos variables se recomienda usar *args, no otro nombre #el asterisco se le conoce cómo la firma de la función
    resultado = 0
    #iteramos cada elemento de los argumentos variables *args
    for valor in args: # se usa sin el * ya que es solo la firma en la declaración de nuestra función
        resultado += valor # resultado = resultado + valor, guarda cada valor de la tupla en la variable "valor" y luego la suma a nuestra variable resultado con el valor que ya se tenía igualado la adiciona a resultado.
    return resultado
#llamada a la función
print(sumar_valores(3, 5, 9, 10, 20))


