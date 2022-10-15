class Aritmetica:
    '''
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    '''
    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a    
        self.operando_b = operando_b
    
    def sumar(self):
        return self.operando_a + self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b
    
    def multiplicar(self):
        return self.operando_a * self.operando_b
    
    def dividir(self):
        return self.operando_a / self.operando_b 
    
aritmetica_1 = Aritmetica(3, 2) 
print(f'Operaciones entre {aritmetica_1.operando_a} y {aritmetica_1.operando_b}')
print(f'Suma: {aritmetica_1.sumar()}')
print(f'Resta: {aritmetica_1.restar()}')
print(f'Multiplicación: {aritmetica_1.multiplicar()}')
print(f'División: {aritmetica_1.dividir():.2f}')




        