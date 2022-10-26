# escribe en un rango de 2 a 6

for x in range(2, 6):
  print(x)


#Imprime la lista completa

fruits = ["apple", "banana", "cherry", "Parchita", "Mango"]
for y in fruits:
  print(y)  


#break cuando llega a banana
 
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana": 
    break

# break cuando llega a banana e imprime el sig en la lista

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# crea una secuencia (ini,Fin, Secuencia)

for x in range(0, 31, 5):
  print(x)


# Loop dentro de una Loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  

# for loops cannot be empty, but if you for some reason have a for 
# loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass