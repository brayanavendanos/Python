# Importamos las clases de tipo persona

from Persona import * # imprimimos todo

persona_1 = Persona('Juan', 25)
print(persona_1) # si lo ponemos así, unicamente nos va a arrojar la posición en memoria que se tiene debemos añadir un metodo __str__ 

empleado_2 = Empleado('Karla', 25, 5000)
print(empleado_2)

print(empleado_1)

empleado_3 = Empleado('Juanchis', 19, 12000)
print(empleado_3)

