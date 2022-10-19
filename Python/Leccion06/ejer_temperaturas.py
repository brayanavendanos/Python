""" 
Ejercicio: Convertidor de temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""

# Funcion que convierte de celcius a fahrenheit
def celsius_fahrenheit(grados_celsius):
    grados_farenheit = grados_celsius * 1.8 + 32
    return grados_farenheit

# Entrada del usuario / llamado de función / print del resultado
grados_celsius = float(input('Ingrese la cantidad de grados celsius: '))
grados_farenheit = celsius_fahrenheit(grados_celsius)
print(f'{grados_celsius} C a F: {grados_farenheit:.2f}')

# Función que convierte de celcius a fahrenheit
def farenheit_celsius(grados_farenheit):
    grados_celsius = (grados_farenheit - 32) * (5/9)
    return grados_celsius

# Entrada del usuario / llamado de función / print del resultado
grados_farenheit = float(input('Ingrese la cantidad de grados farenheit: '))
grados_celsius = farenheit_celsius(grados_farenheit)
print(f'{grados_farenheit} F a C: {grados_celsius:0.2f}')

