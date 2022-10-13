# Operadores

from __future__ import division
from tokenize import Exponent


operando_a = 3
operando_b = 2
suma = operando_a + operando_b
# print('Resultado suma: ', suma)
print(f'Resultado suma: {suma}')

resta = operando_a - operando_b
print(f'Resultado resta: {resta}')

multiplicacion = operando_a * operando_b
print(f'Resultado multiplicacion: {multiplicacion}')

division = operando_a / operando_b
print(f'Resultado division: {division}')

division = operando_a // operando_b
print(f'Resultado division (int): {division}')

modulo  = operando_a % operando_b
print(f'Resultado residuo división (modulo): {modulo}')

exponente = operando_a ** operando_b
print(f'Resultado exponen exp: {exponente}')
