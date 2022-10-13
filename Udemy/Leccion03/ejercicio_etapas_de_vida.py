edad = int(input('Proporciona tu edad: '))
intervalo = None

if 0 < edad <= 10: 
    intervalo = ('La infancia es increíble')
elif 10 < edad <= 20:
    intervalo = ('Muchos cambios y mucho estudio')
elif 20 < edad <= 30:
    intervalo = ('Amor y comienza el trabajo')
else: 
    intervalo = ('Edad incorrecta') 
    
print(f'Tu edad es: {edad}, {intervalo}')
