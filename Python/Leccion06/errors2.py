try:
    print(0 / 0)
# Cualquier error que pase en este bloque el lo va a capturar 
# registra este tipo de errores para ver un reporte de fallos 
# sin romper el sistema
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

print('Hola')
