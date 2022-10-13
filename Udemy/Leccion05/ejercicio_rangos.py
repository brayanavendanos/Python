#Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

#Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

print('Números divisibles entre 3')
for i in range(11):
    if i % 3 == 0:  #si aplicamos el operador de modulo de 3 y esta operación regresa a cero quiere decir que es divisible entre 3. 
        print(i)

#Ejercicio 2. Crear un rango de números de 2 a 6, e imprimir

print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2,7)
for i in rango: #iteramos el rango de 2 a 7 de uno en 1
    print(i)

#Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

print('Números con incremento de 2 en 2')
for i in range(3,11,2): #Se utiliza la sintaxis de range, número inicial<3>, fin<11> e incremento <2>
    print (i)

#también se puede hacer definiendo el rango desde antes. 
print('números de 2 en 2 con rango definido')
rango = range(3,11,2)
for i in rango:
    print(i)