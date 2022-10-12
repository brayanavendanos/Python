
print('Proporcione los siguientes datos del libro: ')

nombre = input('Proporciona el nombre: ')
id_libro = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envio = input('Indica si el envío es gratuito (True/False): ') # No se coloca el "bool" para definir el valor del envio, ya que lo convertirá a true automaticamente desde que se ingrese un dato. 

#Conversión a bool del envío para confirmar el string ingresado
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else: 
    envio = 'Valor incorrecto, debe escribir "True/False"'
    
    
#imprimir varios datos al tiempo
print(f'''
    Nombre: {nombre}
    Id: {id_libro}
    Precio: {precio}
    Envio gratuito: {envio}
''')

