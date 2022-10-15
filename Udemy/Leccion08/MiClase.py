class MiClase:
    
    # Variable de clase - Compartida con todos los objetos que se creen a partir de esta clase
    variable_clase = 'Valor variable clase 1'
    
    
    # Variables instancia
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia
        
    # Métodos estaticos
    
    # Este decorador afecta el siguiente metodo, asociandose a la clase misma y no a los objetos
    # Contexto estático: El método estatico no puede acceder a las variables de instancia ni a los metodos de instancia ya que al definir la clase todavía no se pueden crear objetos
    # Contexto dinámico: Objetos creados con atributos y metodos de instancia de nuestra clase, al momento en que ya se carga por completo nuestra clase por memoria.
    
    # No recibe la palabra self, por el contexto estático.
    # a las variables de manera indirecta, si se puede acceder usando la clase y la variable de la misma. 
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # Método de clase
    
    # Si recibe contexto de clase, este recibe un parametro similar al self, ya que usa el "cls" que significa clase
    # Podría utilizar otra palabra pero segun la documentación de python es el recomendable. 
    # Es el parámetro de la clase en si misma, que recibe el metodo.
    # En metodo de clase accedemos a las variables de clase con el apuntador "cls" directamente
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        


        
print('Variable de clase'.center(30,'-'))
print(MiClase.variable_clase)
     
print('Variable 1 de objeto'.center(30,'-'))
mi_clase = MiClase('Valor variable instancia 1')
print(mi_clase.variable_instancia)
print(mi_clase.variable_clase) # Acceso desde el objeto a la variable definida en la clase

# Crear variable al vuelo - se asoció dinámicamente a nuestra clase
MiClase.variable_clase2 = 'Valor variable clase 2'

print('Variable 2 de objeto'.center(30,'-'))
mi_clase2 = MiClase('Valor variable instancia 2') 
print(mi_clase2.variable_instancia)
print(mi_clase2.variable_clase)

# Acceder a nuestra variable al vuelo 
print('Variable vuelo'.center(30,'-'))
print(MiClase.variable_clase2)
print(mi_clase.variable_clase2)
print(mi_clase2.variable_clase2)

# Imprimir método estático
print('Método estático'.center(30,'-'))
MiClase.metodo_estatico()

# Imprimir metodo clase
print('Método de clase'.center(30,'-'))
MiClase.metodo_estatico()

# Acceder

mi_objeto1 = MiClase('variable_instancia')
print(mi_objeto1.variable_instancia)

