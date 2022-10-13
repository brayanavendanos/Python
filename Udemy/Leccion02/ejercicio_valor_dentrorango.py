valor = int(input('Escribe el valor: '))
valor_min = 0
valor_max = 5

dentro_rango = valor >= valor_min and valor <= valor_max

if dentro_rango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')