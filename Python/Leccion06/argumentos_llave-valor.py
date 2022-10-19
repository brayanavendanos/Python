#función que tenga una lista de terminos

def listar_terminos(**terminos): # el kwargs nos va a permitir un diccionario completo, es decir, un elemento de llave:valor, pero en argumentos
    for llave, valor in terminos.items(): # iterar la llave y el valor de cada uno de los terminos, con el termino.items accedemos a los terminos de nuestro diccionario
        print(f'{llave}: {valor}') # imprimimos cada elemento accediendo a la llave y a su valor
        
listar_terminos(IDE = 'Integrated Developement Enviroment', PK = 'Primary Key') # Podemos pasar n cantidad de terminos porque es un diccionario variable 
#la llave no lleva comillas y el valor puede ser cualquier tipo de dato
#podemos pasar cualquier tipo de elementos

listar_terminos(DBMS= 'Database Management System')

#Así manejamos argumentos variables. 


# si tenemos varios parametros para nuestra función, debemos añadirlos antes de los argumentos variables y luego un diccionario de terminos también variable


        
        
        
        