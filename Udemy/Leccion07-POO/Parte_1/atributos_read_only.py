'''
Si no queremos modificar la variable nombre, quitamos el metodo set y se conocerá cómo variable de solo lectura

'''

class Persona: 
    
    def __init__(self, nombre, apellido, edad): 
        self._nombre = nombre                      
        self.apellido = apellido                  
        self.edad = edad
    
    # Decorador
    @property
      # Metodo de nombre para regresar el atributo de nombre "_nombre"
    def nombre(self):
        print('Llamando método get nombre')          
        return self._nombre 
    
    # # Decorador setter
    # @nombre.setter
    # # metodo de tipo set asociado a nuestro atributo de nombre (nombre del atributo / setter )
    # def nombre(self, nombre):
    #      print('Llamando método set nombre')
    #      self._nombre = nombre
         
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        

persona_1 = Persona('Juan', 'Perez', '28')
print(persona_1.nombre)

