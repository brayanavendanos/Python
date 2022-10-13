'''
Calcular el volumen de un Cubo
Creamos una clase llamada Cubo atributos ancho, alto y profundo
Metodo calcular_volumen
ancho * profundo * alto
El usuario debe proporcionar los valores
'''

class Cubo:
    
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto
    
    def calcular_volumen(self):
        return self.ancho * self.profundo * self.alto
         
    
ancho = int(input('Proporciona el ancho: '))
profundo = int(input('Proporciona el profundo: '))
alto = int(input('Proporciona el alto: '))

# resultado = Cubo(ancho, profundo, alto).calcular_volumen()
# print(f'Volúmen del cubo: {resultado}')


cubo_1 = Cubo(ancho, profundo, alto)
print(f'Volúmen cubo: {cubo_1.calcular_volumen()}')  # siempre debe llevar el paréntesis en el momento en que llamamos el metodo al momento de imprimir.



