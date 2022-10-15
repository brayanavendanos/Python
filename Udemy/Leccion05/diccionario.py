#Diccionarios
# En lugar de tener una lista de datos, vamos a tener una colección de datos organizados en donde tenemos, una llave(Key) y el valor asociado(value) / los diccionarios no tienen indices
#key:value así cómo se maneja en los diccionarios, palabra y significado.

diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System',
}

print(diccionario)

#largo de un diccionario
print(len(diccionario))

#cómo acceder a un elemento (key)
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#modificar elementos dentro del diccionario 
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#cómo recorrer los elementos de un diccionario
for termino, valor in diccionario.items(): # esta función nos devuelve los elementos separados, de termino y valor. key y valor
    print(termino, valor)

#cómo recuperar solamente los terminos
for termino in diccionario.keys():
    print(termino)

#cómo imprimir solamente los valores
for valor in diccionario.values():
    print(valor)

#comprobar la existencia de un elemento dentro del diccionario
print('IDE' in diccionario) # se debe respetar mayúsculas y minúsculas en la busqueda de elementos en nuestro diccionario

#agregar un elemento a los diccionarios 
diccionario['PK'] = 'Primary Key'
print(diccionario)

#remover un elemento del diccionario 
diccionario.pop('DBMS')
print(diccionario)

#limpiar el diccionario
diccionario.clear()
print(diccionario)

#eliminar el diccionario
del diccionario
print(diccionario)



