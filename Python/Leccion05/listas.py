#Las listas son conjunto de elementos en donde se almacenan
# cualquier tipo de datos que exista en python. A cada valor dentro de la lista se le asigna un valor, iniciando de 0. 

#El indice nos permite acceder, modificar o eliminar elementos en cada lista.

#Definir una lista de tipo str
nombres = ['Juan', 'Andres', 'Karla', 'Ricardo', 'Maria']

#imprimir la lista de nombres
print(nombres)

#Acceder a elementos de una lista
print(nombres[0])
print(nombres[3])

#Acceder a los elementos de la lista inversamente, se añaden los números en negativo, desde el último al primero.
print(nombres[-5])
print(nombres[-2])

#imprimir un rango dentro de la lista
print(nombres[0:2]) #sin incluir el indice 2, imprime el 0 y el 1

#ir del inicio de la lista al indice (sin excluirlo)
print(nombres[:3])

# imprimir de atras hacia adelante
print(nombres[::-1])

#desde el indice indicado hasta el final de la lista
print(nombres[1:]) #no imprime el indice 0 imprime hasta el 4

#cambiar un valor de la lista
nombres[3] = 'Ivone' #cambiamos el valor del indice 3(ricardo) por Ivone)
print(nombres)

#iterar una lista - imprime valores individuales de la lista
#las listas deberían ir siempre con un nombre en plural
for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")

#preguntar el largo de una lista
print(len(nombres))

#Agregar un elemento a nuestra lista
nombres.append('Brayan')
print(nombres)

#insertar un elemento en un índice en específico 
nombres.insert(1, 'Octavio')
print(nombres)

#eliminar un elemento de la lista
nombres.remove('Octavio')
print(nombres)

#eliminar el último valor agregado a la lista
nombres.pop()
print(nombres)

#eliminar un indicé en específico de la lista
del nombres[0]
print(nombres)

#limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres) 


