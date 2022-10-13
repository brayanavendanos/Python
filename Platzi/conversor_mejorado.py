# Conversor de monedas

def conversor(tipo_pesos, valor_dolar):
    pesos = input(f'Cuántos pesos {tipo_pesos} tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    #reduccion decimales
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f'Tienes ${dolares} dólares')
    pass


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
    conversor("colombianos", 4575) 
elif opcion == 2:
    conversor("argentinos",151)
elif opcion == 3:
    conversor("mexicanos",20)
else:
    
    print("Ingresa una opción valida")


