# Conversor de monedas

menu = """
----------------------------------------------------------------
[[Bienvenido al conversor de monedas 🪙]]

<<Seleccione que conversión desea realizar>>

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

----------------------------------------------------------------
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4575
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    
    
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 151
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    
elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    
else:
    
    print("Ingresa una opción valida")


