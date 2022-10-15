class Persona: 
    def __init__(self, nombre, apellido, edad ): # Se asignan los parámetros 
        self.nombre = nombre
        self.apellido = apellido        # Se llaman los parámetros definidos en nuestra clase. 
        self.edad = edad
    
    #Todo lo que está definido a este nivel de tabulación está dentro de nuestra clase
    
    def mostrar_detalle(self):  # Metodo mostrar_detalle, es un metodo de instancia ya que se relaciona con todos los objetos que vamos a crear
                                # Es obligatorio usar el "self" si es un metodo de instancia
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}') # Imprimimos el objeto persona, accedemos a cada uno de los objetos de nuestra clase con el parámetro self
                                         # Para acceder a cada uno de nuestros atributos, por eso usamos el self.nombre
                                         
      
persona_1 = Persona('Juan', 'Perez', '28')
persona_1.mostrar_detalle() # Se llama el metodo sin parametros dentro ya que el metodo al ser de instancia trae el self y los datos de la función

# Se pueden agregar atributos a nuestro objeto, pero no se comparten con los demás
# Es decir no se comparte con persona_2 porque no se encuentra dentro de la clase. 
persona_1.telefono =  '3124748198' 
# No es comun añadir esos datos a los objetos de esta forma. 
print(persona_1.telefono)

Persona.mostrar_detalle(persona_1) # Se llama el metodo utilizando el nombre de nuestra clase, pero debemos pasar referencias
                                   # Al pasar persona_1 obtenemos el mismo detalle de la linea anterior, pero esto no es lo común. 
                                   

persona_2 = Persona('Karla', 'Gomez', '30')
persona_2.mostrar_detalle()
print(persona_2.telefono)
