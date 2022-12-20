import math
lado= int(input("Ingrese la medida de un lado del hexágono: "))
perimetro = lado * 6
apotema = math.sqrt(lado**2-(lado/2)**2)
area = (perimetro * apotema)/2
print(area)
print(perimetro)