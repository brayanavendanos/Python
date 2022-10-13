from Cuadrado import *
from Rectangulo import *

print('Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado_1 = Cuadrado(lado = 5, color = "Rojo")
print(cuadrado_1)
# cuadrado_1.alto = -10 no es forma adecuada de añadir datos.
print(f'Área del cuadrado: {cuadrado_1.calcular_area()}')

print('Creacion Objeto Rectangulo'.center(50,'-'))
rectangulo_1 = Rectangulo(ancho = 8, alto = 9, color = "Azul")
print(rectangulo_1)
print(f'Área del rectangulo: {rectangulo_1.calcular_area()}')

# print(f'El lado del cuadrado equivale a: {cuadrado_1.ancho}')
# print(f'El color del cuadrado es: {cuadrado_1.color}')
# print(f'El área del cuadrado: {cuadrado_1.calcular_area()}')


# # # MRO - Method Resolution Order

# print(Cuadrado.mro())
# print(Color.mro())


# rectangulo_1 = Rectangulo(5,4,"Lo pone tu corazón")
# print(f'Altura: {rectangulo_1.altura} Base: {rectangulo_1.base}')
# print(f'Color: {rectangulo_1.color}')
# print(f'El área del rectangulo es: {rectangulo_1.calcular_area}')