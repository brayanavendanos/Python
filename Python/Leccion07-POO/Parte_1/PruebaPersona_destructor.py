# Crear metodo destructor dentro del metodo externo "PruebaPersona"
from Persona import Persona 

print('Creación de objetos'.center(30,'-')) # Dar formato de impresión al modulo de creación de objetos
persona_3 = Persona('Karla', 'Gomez', 30)
persona_3.mostrar_detalle() 

print('Eliminación de objetos'.center(30,'-')) # Dar formato de impresión al módulo de destructor

del persona_3

