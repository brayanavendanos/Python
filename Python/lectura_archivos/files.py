file = open('./Python/lectura_archivos/text.txt')

#lee todo el archivo
# print(file.read())

# lee linea por linea
#print(file.readline())

# lee un archivo en forma de lista
# print(file.readlines())

#iterar un archivo
for line in file:
    print(line)
    
file.close()


#Cerrar de forma automatica el archivo
with open('./Python/lectura_archivos/text.txt'):
    for line in file:
        print(line)
