#cómo pasar argumentos variables a una función en python
#En esta función desconocemos el número de argumentos

def listar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
#el * antes del parametro, lo que hace es definir que no sabemos cuantos elementos vamos a recibir. 
#dentro del código de manera interna python lo convierte en una tupla y se puede iterar de esa forma

#llamamos la función
listar_nombres('Juan', 'Karla', 'Maria', 'Ernesto')
listar_nombres('Laura', 'Carlos')
