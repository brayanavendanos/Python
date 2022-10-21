
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input('ingrese número: ').strip())

    if n % 2 == 1: 
        print('Weird')
    elif n % 2 == 0 & 2 < n <= 5:
        print('Not weird')
    elif n % 2 == 0 & 6 <= n <= 20:
        print('Weird 2')
    elif n % 2 == 0 & n < 20:
        print('Not weird 2')
    else: 
        print('Ingrese un número valido')
        
