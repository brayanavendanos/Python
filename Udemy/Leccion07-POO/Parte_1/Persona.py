class Persona: 
    
    def __init__(self, nombre, apellido, edad): 
        self._nombre = nombre                      
        self._apellido = apellido                  
        self._edad = edad
    
    # Decorador
    @property
    # Metodo de nombre para regresar el atributo de nombre "_nombre"
    def nombre(self):
        return self._nombre 
    
    # Decorador setter
    @nombre.setter
    # metodo de tipo set asociado a nuestro atributo de nombre (nombre del atributo / setter )
    def nombre(self, nombre):
         self._nombre = nombre
    
    # Regresar apellido
    @property
    def apellido(self):
        return self._apellido
    
    # Modificar apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
       
    # Regresar edad 
    @property
    def edad(self):
        return self._edad
    
    # Modificar edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
         
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    
    #Crear metodo destructor    
    def __del__(self): # under del es el metodo destructor
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
        
# Validamos si la propiedad de __name__ es igual a el módulo __main__ para que ejecute nuestro codigo
if __name__ == '__main__':
    
    persona_1 = Persona('Juan', 'Perez', '28')
    persona_1.mostrar_detalle()

    persona_2 = Persona('Maria', 'Gonzalez', '23')
    persona_2.mostrar_detalle()

    persona_1.nombre = 'Brayan Andres'
    persona_1.apellido = 'Avendaño'
    persona_1. edad= '26'
    persona_1.mostrar_detalle()

    persona_2.nombre = 'Maria Fernanda' 
    persona_2.apellido = 'Lozano'
    persona_2.edad = '27'
    persona_2.mostrar_detalle()

# imprime el módulo en el que estamos trabajando 
print(__name__) # imprime el modulo principal __main__ ya que este es el módulo principal 
