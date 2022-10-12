class Persona: 
    
    def __init__(self, nombre, apellido, edad, *valores, **terminos):  # Si queremos pasar una tupla de valores de tipo variable usamos *args
        self.nombre = nombre                      # de la misma forma podemos añadir un diccionario de datos **kwargs 
        self.apellido = apellido       
        self.edad = edad
        self.valores = valores  #le asignamos a nuestro objeto la tupla de valores
        self.terminos = terminos  # también asignamos a nuestro atributo de terminos el diccionario de terminos que podemos recibir
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
        


# de esa forma se pueden seguir añadiendo datos de cualquier tipo de dato, ya que es una tupla con argumentos variables.
# También podemos añadir un diccionario para nuestro objeto y pasamos diccionarios.
# Primero se ponen las tuplas y luego los tipo diccionario
persona_1 = Persona('Juan', 'Perez', '28', '444123', 2, 3, 5, m ='Manzana', p='Pera') 
persona_1.mostrar_detalle()

persona_2 = Persona('Karla', 'Gomez', '30')
persona_2.mostrar_detalle()