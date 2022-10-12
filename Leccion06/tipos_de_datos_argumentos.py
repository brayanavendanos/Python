# definir una función que reciba una lista de elementos y que acceda a cada uno de ellos

def desplegar_nombres(nombres):
    for nombre in nombres: #declaramos nombre para almacenar cada uno de los valores de la lista de nombres, iteramos de la lista nombres
        print(nombre)


nombres = ['Jorge', 'Juan', 'Karla']
desplegar_nombres(nombres) #debemos poner cómo argumento nuestra lista de nombres

desplegar_nombres(nombres)
desplegar_nombres('Carlos') #El resultado es que itera nuestra cadena, itera cada uno de los caracteres por separado
desplegar_nombres((10, 11)) # Si se añade un int, no se puede iterar, y si se añaden dos valores, deben ir dentro de dos paréntesis (()) ya que debe convertirse una tupla para que se puedan iterar dos valores distintos. 
desplegar_nombres([10,11]) #o también se pueden añadir cómo una lista



