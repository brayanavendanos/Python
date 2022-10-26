import time

tiempo_inicial = time.time()

objetivo = int(input('Escoge un número: '))

epsilon = 0.01
paso = epsilon ** 2
respuesta = 0.0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta** 2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else: 
    print(f'La raiz cuadrada de {objetivo} es la {respuesta}')
    

print(f'El programa demoró {time.time() - tiempo_inicial} segundos ')