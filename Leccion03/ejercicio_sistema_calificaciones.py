valor_calificacion = int(input('Proporcione un valor entre 0 y 10: '))
calificacion = None

#  if valor_calificacion == 9 or valor_calificacion == 10: 
#      calificacion = 'A'
#  elif valor_calificacion >= 8 and valor_calificacion < 9: 
#      calificacion = 'B'
#  elif valor_calificacion >= 7 and valor_calificacion < 8:
#      calificacion = 'C'
#  elif valor_calificacion >= 6 and valor_calificacion < 7:
#      calificacion = 'D'
#  elif valor_calificacion >= 0 and valor_calificacion < 6:
#      calificacion = 'F'

if 9 <= valor_calificacion <= 10:
    calificacion = 'A'
elif 8 <= valor_calificacion < 9:
    calificacion = 'B'
elif 7 <= valor_calificacion < 8:
    calificacion = 'C'
elif 6 <= valor_calificacion < 7:
    calificacion = 'D'
elif 0 <= valor_calificacion < 6:
    calificacion = 'F'
else: 
    calificacion = 'Número incorrecto, por favor ingrese un valor entre 0 y 10'

print(f'El número ingresado es: {valor_calificacion} lo que corresponde a : {calificacion}')
