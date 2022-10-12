# Crear clase con argumentos y no valores duros por default

class Persona: 
    
    def __init__(self, nombre, apellido, edad ): # Se asignan los parámetros 
    # La variable que no utiliza self es un parámetro
    # Las que utilizan self, son los atributos de nuestra clase
     self.nombre = nombre
     self.apellido = apellido        # Se llaman los parámetros definidos en nuestra clase. 
     self.edad = edad

# persona_1 = Persona()
# Esto ya no se puede hacer ya que mandamos a llamar el constructor de nuestra clase y eso llama nuestro metodo init
# se debe añadir de la siguiente forma

persona_1 = Persona('Juan', 'Perez', '28')
# De esta forma se guardan los datos en nuestra clase y finalmente
# Se imprimen accediendo como en el anterior.
print('Objeto Persona 1:')
print(persona_1.nombre)
print(persona_1.apellido)
print(persona_1.edad)

# Para crear un segundo objeto creamos una segunda variable y usamos nuestra plantilla que es el nombre 
# De nuestra clase

persona_2 = Persona('Karla', 'Gomez', '30')

# se vuelven a imprimir los datos de nuestro objeto y podemos hacerlo en una sola linea. 
print(f'Objeto Persona 2: {persona_2.nombre} {persona_2.apellido} {persona_2.edad}')


# Para modificar los atributos de un objeto ya creado hacemos lo siguiente:

# Utilizamos la variable que ya tenemos definida persona_1 y accedemos al atributo que queremos modificar
persona_1.nombre = 'Brayan Andres' 
persona_1.apellido = 'Avendaño'
persona_1.edad = '25'

# Imprimimos para validar el cambio
print(f'Objeto Persona 1: {persona_1.nombre} {persona_1.apellido} {persona_1.edad}')

# Cambiamos los datos del segundo objeto
persona_2.nombre = 'Paula'
persona_2.apellido = 'Jolly'
persona_2.edad = '24'

# Imprimimos para ver los cambios
print(f'Objeto Persona 2: {persona_2.nombre} {persona_2.apellido} {persona_2.edad}')

# No es la forma recomendada acceder a los atributos de nuestra clase directamente y cambiarlos
# Se utilizará con encapsulamientos a través de metodos para la modificación de valores de nuestros atributos

