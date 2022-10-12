from traceback import print_tb


numero_uno = int(input('Digite el primer número: '))
numero_dos = int(input('Digite el segundo número: '))

print(f'Proporciona el número uno: {numero_uno}')
print(f'Proporciona el segundo número: {numero_dos}')


if(numero_uno > numero_dos):
    print(f'El número uno ({numero_uno}) es mayor que el número dos ({numero_dos})')
else:
    print(f'El número dos ({numero_dos}) es mayor que el número uno ({numero_uno})')