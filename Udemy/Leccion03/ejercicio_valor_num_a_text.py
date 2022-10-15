numero = int(input('Propociona un valor entre 1 y 3: '))
numero_texto = ''

if numero == 1:
    numero_texto = 'Número uno'
elif numero == 2:
    numero_texto = 'Número dos'
elif numero == 3:
    numero_texto = 'Número tres'
else:
    numero_texto = 'Valor fuera de rango' 
print(f'Número proporcinado: {numero} - {numero_texto}')