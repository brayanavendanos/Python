# Calculadora de potencias

def run():
    menu =""" 
    [Bienvenido a la calculadora de potencias]📖
    """
    print(menu)
    
    numero = int(input('Ingrese el número que desea elevar a la potencia: '))
    potencia = int(input(f'Ingrese la potencia a la cual desea elevar el número {numero}: '))
    contador = 0
        
    while contador <= potencia & potencia < 1000:
        resultado_potencia = numero ** contador
        contador += 1
        print(f'El número {numero} elevado a la potencia {contador-1} es igual a: {resultado_potencia}')
    

if __name__ == "__main__":
    run()