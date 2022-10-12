from ctypes.wintypes import HLOCAL


a = 4
b = 2

#Saber si a es mayor que b (==)
resultado = a == b 
print(f'Resultado == : {resultado}')

#operador si es diferente !=
resultado = a != b
print(f'Resultado != : {resultado}')

#operadores < y >
resultado = a < b
print(f'Resultado < : {resultado}')

resultado = a <= b
print(f'Resultado <= : {resultado}')

resultado = a > b
print(f'Resultado > : {resultado}')

resultado = a >= b
print(f'Resultado >= : {resultado}')

#funcionan con string de igual forma, ambos operadores
resultado = 'hola' == 'hola'
print(f'Resultado == : {resultado}')