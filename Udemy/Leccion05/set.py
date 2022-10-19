#Colección de tipo set, no mantiene orden ni permite modificar los elementos
#Si permite añadir o eliminar
#No tiene indices, por ende no deja modificar elementos en específico ya que se encuentran desorganizados

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas) #La impresión cambia al momento de la impresión

#Largo
print(len(planetas))

#Revisar si un elemento está presente
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

planetas.update('marte')
print(planetas)

#No acepta duplicación de elementos
planetas.add('Tierra')
print(planetas)

#remover un elemento
planetas.remove('Jupiter')
print(planetas)

#eleiminar un elemento sin arrojar error
planetas.discard('Jupiters')
print(planetas)

#limpiar un set
planetas.clear()
print(planetas)

#eliminar por completo un set
del planetas
print(planetas)
