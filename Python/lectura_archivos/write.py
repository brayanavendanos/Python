with open('./Python/lectura_archivos/text.txt', 'w+') as file:
    for line in file:
        print(line)
    # Escribir al final del archivo
    file.write('Nuevas cosas en este archivo \n')
    
    file.write('\nNueva linea espaciado')
    
    
    # el permiso de r+ nos permite leer y escribir, agrega nuevas lineas, respeta lo que hay
    # w+ cambiamos los permisos, lectura y escritura pero va a sobreescribir todo el archivo.
    
    
    