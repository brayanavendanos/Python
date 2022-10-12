from Persona import Persona # del archivo Persona, importamos la clase Persona

#preguntamos si __name__ es igual a __main__ para ejecutar esta parte
if __name__ == '__main__':
    # Añadimos un nuevo objeto a la clase de Persona
    persona_3 = Persona('Karla', 'Gomez', 30)
    # Llamamos al metodo la clase de Persona para mostrar el nuevo objeto que tenemos
    persona_3.mostrar_detalle() 

# imprime el módulo en el que estamos trabajando 

# imprime el módulo en el que estamos trabajando 
print(__name__) # imprime primero "Persona" ya qué es el módulo base, pero vuelve a imprimir __main__ ya que importa el del anterior módulo



