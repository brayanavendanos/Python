# Herencia múltiple

class FiguraGeometrica:
    
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
        
    def __str__(self):
        return f'Figura geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
    # Definimos un método para hacerlo privado de uso interno
    # con el valor que queremos validar y retornamos la validación
    # y lo llevamos arriba.
    def _validar_valor(self,valor):
        # Regresamos verdadero si el valor está entre 0 y 10 
        # si no, regresamos falso
        return True if 0 < valor < 10 else False