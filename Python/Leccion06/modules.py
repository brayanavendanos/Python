import itertools
import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del país es 57, mi número de la suerte es el 3'

# ['311', '123', '121', '57', '3']
result = re.findall('[0-9]+', text)
print(result)

# 1666369731.7095237
import time 
timestamp = time.time()
print('\n',timestamp)

#Impresion tiempo formato = Fri Oct 21 11:28:51 2022
local = time.localtime()
result = time.asctime(local)
print('\n',result)

#Imprime un diccionario con la frecuencia de cada uno de los elementos dentro de la lista
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)