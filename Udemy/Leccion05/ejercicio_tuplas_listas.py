# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)

#Definir la lista
numeros_menores = [] 

#iteramos la tupla para filtrar los menores a 5
for elemento in tupla: 
    if elemento < 5:  #menores a 5
     numeros_menores.append(elemento)  #añadimos los menores a 5 que están guardados en la variable elemento, con append a la lista numeros_menores

#imprimimos la lista
print(numeros_menores)
    

