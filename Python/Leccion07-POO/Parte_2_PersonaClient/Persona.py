"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""



class Persona:  # Si se añade un paréntesis con (object) hereda las características y si no se pone también ya que es por default
    
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Definimos un metodo dentro de la clase padre que lo que hace es sobreescribiendo la clase padre en una clase hija
    # Tenemos una subclase que es empleado, en donde también sobreescribimos el de la clase padre en la clase hija
    
    def __str__(self): 
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]' # Retornamos un string con los valores de los atributos de nuestra clase padre
                        # Esto va a permitir que en el objeto dentro de "CLientePersona.py" se ejecute de manera automatica
                        # este metodo __str__ para que imprima los datos añadidos. 
        

class Empleado(Persona): # Añadimos la clase "Persona" dentro del paréntesis para decir que es la clase padre
    
    # Se llama el constructor de la clase padre con la palabra "Super" que nos va a permitir acceder a los metodos de la case padre
    # super().__init__(self,nombre, edad) / Se vuelve a poner el primer constructor
    def __init__(self, nombre, edad, sueldo): # Y se adicionan los atributos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def __str__(self): # añadimos metodo str, y accedemos al metodo sueldo, pero llamamos el str anterior ya que este 
                       # ya estaba llamando nombre y edad en la clase superior, con el super que accedemos a los metodos definidos de x clase
        return f'Empleado: [Sueldo: {self.sueldo}] {super().__str__()}'

# Y al llamar los atributos de la clase padre, también debemos añadirlos cuando creamos un nuevo objeto
empleado_1 = Empleado('Andres', 20, 5000)  
print(empleado_1.nombre)
print(empleado_1.edad)
print(empleado_1.sueldo)

# es importante inicializar los atributos de la clase siempre o si no, no van a ser llamados.


