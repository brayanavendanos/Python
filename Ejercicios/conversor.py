# Conversor de monedas

menu = """
----------------------------------------------------------------
[[Bienvenido al conversor de monedas 馃獧]]
<<Seleccione que conversi贸n desea realizar>>
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
----------------------------------------------------------------
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("驴Cu谩ntos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 4575
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    
    
elif opcion == 2:
    pesos = input("驴Cu谩ntos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 151
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    
elif opcion == 3:
    pesos = input("驴Cu谩ntos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")
    
else:

    print("Ingresa una opci贸n valida")

