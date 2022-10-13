'''
Crearemos una clase que se llama rectangulo, con dos atributos, altura y base.
Se debe crear un metodo para calcular el area, con la siguiente formula
A = b * h
la base y la h debe proporcionarla el usuario. 
'''

class Rectangulo:
    
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    
    def calcular_area(self):
        area =  self.altura * self.base
        return area
    
base = float(input('Proporcione la base del rectángulo: '))
altura = float(input('Proporcione la altura del rectángulo: '))

area = Rectangulo(base, altura).calcular_area()

print(f'Área rectángulo: {area}')


# Solución del docente

# rectangulo_1 = Rectangulo(base, altura)
# print(f'Área rectángulo: {rectangulo_1.calcular_area}')

# Se puede crear otro objeto para pedir 2 objetos

# rectangulo_2 = Rectangulo(base, altura)
# print(f'Área rectángulo: {rectangulo_2.calcular_area}')

