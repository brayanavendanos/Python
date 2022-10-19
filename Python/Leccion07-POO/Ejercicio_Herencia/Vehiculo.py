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


class Vehiculo:
    
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculo: [Color: {self._color}, Ruedas: {self._ruedas}"]'
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def ruedas(self):
        return self._ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
    
class Coche(Vehiculo):
    
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    
    def __str__(self):
       return f'{super().__str__()} Velocidad: [{self._velocidad} Km/h]'
   
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
   
class Bicicleta(Vehiculo):
    
    def __init__(self, tipo, ruedas, color):
        super().__init__(color, ruedas)
        self._tipo = tipo
        
    def __str__(self):
        return f'{super().__str__()} Tipo: [{self._tipo}]'
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
        

vehiculo_1 = Vehiculo("Rojo", 17)
print(vehiculo_1)

coche_1 = Coche(40, "azul", 40)
print(coche_1)

bicicleta_1 = Bicicleta("Todoterreno", 16, "Blanco y Negro")
print(bicicleta_1)
    
     