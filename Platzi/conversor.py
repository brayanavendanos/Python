# Conversor de monedas

pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
#reduccion decimales
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

pesos = input("¿Cuantos dolares tienes?: ")
pesos = float(pesos)
valor_peso_colombiano = 4575.7
valor_peso_colombiano = float(valor_peso_colombiano)
dolares = pesos * valor_peso_colombiano
dolares = round(dolares, 2)
print(f'Tienes $ {dolares} pesos Colombianos')

