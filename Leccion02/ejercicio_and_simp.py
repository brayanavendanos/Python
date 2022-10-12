edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad <= 29
#print(veintes)
#treintas = edad >= 30 and edad <= 39
#print(treintas)

if (20 <= edad < 29) or (30 <= edad < 39):
    print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes: 
#        print('Dentro de los 20\'s')
#    elif treintas:
#          print('Dentro de los 30\'s')
#    else:
#          print('Fuera de rango de edad')
else:
    print("No está dentro de los 20's ni 30's")