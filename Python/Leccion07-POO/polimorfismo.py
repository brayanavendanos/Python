class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando caminando')
        

class Ciclista(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre) #Referencia a Persona(superclase)
        
    def avanza(self):
        print('Ando moviendome en mi bicicleta')
    
def main():
    persona = Persona('Andres')
    persona.avanza()
    
    ciclista = Ciclista('Bryan')
    ciclista.avanza()
        
if __name__ == '__main__':
    main()
        
        
        