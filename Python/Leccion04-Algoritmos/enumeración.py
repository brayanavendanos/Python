import time

tiempo_inicial = time.time()

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta ** 2 < objetivo:
    print(respuesta)
    respuesta += 1

if respuesta ** 2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tiene una raíz cuadrada exacta.')


print(f'El programa demoró {time.time() - tiempo_inicial} segundos ')