#Definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba') #Se crea con paréntesis

#Se mantiene un indice, un orden conforme se van agregando los elementos
#No se pueden agregar más elementos dentro de una tupla

#Saber el largo de una tupla
print(len(frutas))

#Acceder a un elemento de la tupla
print(frutas[0])

#Acceder inversamente cómo en las listas
print(frutas[-1]) #Usamos corchetes, porque se creó con paréntesis.

#Acceder a un rango
print(frutas[0:1])

#Para que sea una tupla debe tener una "," al final, si solo tiene un elemento, así como cuando imprimimos el rango anterior
#en la consola arrojó esto =
#('Naranja',)-
#y así mismo se debe definir la tupla cuando lleva un solo elemento.

#recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ') #Se añade el end= para cambiar el caracter de salto de linea por defecto que es el \n

#cambiar valor de una tupla es imposible.
#frutas[0] = 'Pera' 

#Convertir una tupla a una lista utilizando la funcion list
frutas_lista = list(frutas) #se convierte con la funcion a lista
frutas_lista[0] = 'Pera' # se cambia el indice del valor Naranja a Pera
frutas = tuple(frutas_lista) # utilizamos la función tuple para convertir la lista en tupla
print('\n',frutas) #utilizamos el \n para imprimir un salto de linea y posteriormente imprimir nuestra nueva tupla modificada

#No es buena practica realizar estas conversiones, si vamos a escoger una tupla es porque jamás vamos a modificar esos elementos. 
#No se utiliza append ni remove, pero si se puede eliminar = 

#Elminar la tupla por completo
del frutas

print(frutas) #Error variable de frutas no definida
