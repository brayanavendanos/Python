# for i in range(10):
#     if i % 2 == 0:
#         print(f'Valor: {i}')


for i in range(6):
    if i % 2 != 0:  # preguntamos si el valor de i no es divisible entre 2
        continue # nos vamos a la siguiente iteración ( nos permite ejecutar la siguiente iteración dentro de nuestro ciclo)
    print(f'Valor: {i}') # si el if es falso, ya que es diferente de 0 se imprime unicamente i ( los valores que son divisibles en 2)


