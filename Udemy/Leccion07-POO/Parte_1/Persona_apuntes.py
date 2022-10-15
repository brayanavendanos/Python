# Creacion de clases en python
# Para agregar características o atributos utilizamos un metodo llamado init, es un metodo inicializador
# Este metodo es llamado por el lenguaje de python, pero para llamar los objetos necesitamos de este metodo
# Nos permitirá añadir atributos a nuestra clase y utilizarlos

# Al tener dos guiones bajos al inicio y al final es un metodo especial
# se conoce cómo double underscore o dunder / dunder init o metodo init
# Se van a ver muy común cuando estemos trabajando con clases los metodos de tipo dunder

class Persona:  # se define el nombre de la clase en mayúscula como se creo el archivo
#definimos igual que en una función + __init__ + parametro de self, cuando se crea un objeto se crea una referencia de ese objeto
    
    def __init__(self): 
     self.nombre = 'Juan'           #Se asignan los atributos de esta forma con la reservada self."nombre_atributo"
     self.apellido = 'Perez'
     self.edad = 28
     
# No es normal añadir valores por default a los atributos, pero se añadirán mas adelante con parámetros del método __init__

# Crear un objeto de nuestra clase

# Se utiliza el nombre de nuestra clase con una variable 
# Con el () indicamos que se manda a llamar el constructor de nuestra clase
# De manera indirecta llama el metodo __init__
# Se crea un objeto y lo almacena
# Pasa la referencia al objeto que se va a crear en la linea 27 

persona_1 = Persona()

# Accedemos atraves de persona_1 y el operador . nos permite entrar a los atributos de nuestra clase.
print(persona_1.nombre) # Imprime Juan
print(persona_1.apellido) # Imprime Perez
print(persona_1.edad) # Imprime 28


print(type(Persona)) # Imprime <class 'type>
