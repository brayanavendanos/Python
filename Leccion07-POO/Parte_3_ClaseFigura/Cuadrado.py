from FiguraGeometrica import *
from Color import *
# Se puede renombrar los nombres de la clase al momento de importar para abreviar

class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, lado, color):
        # Utilizar el super en herencia múltiple puede ser un poco complejo
        # super().__init__(lado)
        # Utilizamos esto para llamar el método init, pero al nivel de la clase, por eso se coloca el nombre d ela clase 
        FiguraGeometrica.__init__(self, lado, lado) 
        # Llamamos la clase de color y pasamos su metodo para llamar el atributo de color
        Color.__init__(self, color)
        
    def calcular_area(self):
        return self._alto * self._ancho
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'