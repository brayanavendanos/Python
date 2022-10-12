# Herencia múltiple

# Para convertir una base en clase abstracta debemos importar ABC
# Abstract Base Class - Es la base para convertir una clase abstracta
# Importamos la clase ABC y también un decorador "abstracmethod"
# Se importa el metodo para definir un método abstracto
from abc import ABC, abstractmethod 

# Extebdemos figura a ABC

class FiguraGeometrica(ABC):
    
    def __init__(self, ancho, alto):
        # Validar datos de ancho y alto

        if self._validar_valor(ancho):
            self._ancho = ancho
        else: 
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else: 
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')
    
    # Metodo abstracto
    # Usamos el decorador @abstractmethod
    
    @abstractmethod
    
    # Al no tener implementación ya que no sabemos que figura vamos a tener
    # Lo dejamos sin formula y solo usamos pass.
    def calcular_area(self):
        pass
    
    def __str__(self):
        return f'Figura geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
    # Definimos un método para hacerlo privado de uso interno
    # con el valor que queremos validar y retornamos la validación
    # y lo llevamos arriba.
    def _validar_valor(self,valor):
        # Regresamos verdadero si el valor está entre 0 y 10 
        # si no, regresamos falso
        return True if 0 < valor < 10 else False