#pasar información a nuestra función, que es conocido cómo parámetros.
#Los parametros van a ser las variables que declaremos en nuestra función
#los argumentos es el valor que enviamos a nuestra función

def mi_funcion(nombre, apellido): #se definen los parametros de nombre y apellido (Variables : nombre y apellido) 
    print('Saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}') # imprimimos los valores con un fstring para poder llamar los parametros de nuestra función
    
mi_funcion('Juan', 'Perez') #se deben delcara si o si los argumentos o no se va a ejecutar
# nombre(parametro) = 'Juan'(Argumento)
mi_funcion('Karla', 'Lara')
#añadimos otros datos a nuestra función y así nos arroja los dos números. 


