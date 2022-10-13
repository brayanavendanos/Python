# Encapsulamiento en python

class Persona: 
    
    def __init__(self, nombre, apellido, edad): 
        # Si se añade un _ a nombre = _nombre, esto indica que no se debe acceder directamente al valor, solo se deben
        # Acceder desde la misma clase. 
        # Para ser mas restrictivos, podemos añadir _ _ antes del nombre y ya no se dejará modificar por fuera de la clase 
        # cómo cuando se utiliza el _ 

        self._nombre = nombre                      
        self.apellido = apellido                  
        self.edad = edad
        
    # Decorador: Modifica el comportamiento de nuestro metodo
    # Vamos a modificar el metodo de get nombre 
    
    @property   # Esto va a recuperar el atributo de _nombre y solo se podrá acceder através del metodo  
                # pero permite llamar al metodo sin los () ya que eso es lo que hace el decorador.  
    # Metodo de nombre para regresar el atributo de nombre "_nombre"
    def nombre(self):
        print('Llamando método get nombre')          
        return self._nombre 
    
    #definimos el nombre cómo si fuera una propiedad 
    # omitimos guión bajo y agregamos el decorador nombre.setter
    @nombre.setter # metodo de tipo set asociado a nuestro atributo de nombre (nombre del atributo / setter )
    def nombre(self, nombre): # recibimos el valor del atributo nombre para modificar nuestro atributo
        print('Llamando método set nombre')
        self._nombre = nombre # Accedemos de manera indirecta y le asignamos el valor del parametro que recibimos.
    
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        

persona_1 = Persona('Juan', 'Perez', '28') 
print(persona_1.nombre) # imprimimos el valor de nombre, con el metodo y no con el atributo.
persona_1.nombre ='Juan Carlos' # No se agrega el paréntesis al metodo nombre ya que tenemos un decorador indicando cual va a ser el atributo que vamos a modificar
print(persona_1.nombre) 

# persona_1._nombre = 'Juan Carlos' # Esto es una mala práctica, ya que debemos hacerlo desde la clase por el _ arriba en la clase

# La impresion de los metodos, se realizan sin el print, solo con la variable y el nombre del metodo
# Permite imprimirlo, pero como se dijo anteriormente, no se debe realizar. 
#persona_1.mostrar_detalle()

# El encapsulamiento subjetivo es que no podemos acceder directamente a los atributos de nuestra clase

# Para acceder a ellos, se crean los metodos get y set

# get = obtener / recuperar
# set = colocar / modificar 


