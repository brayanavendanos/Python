#No modifiques esta celda
import operator

catalogo = { 
            "Oso de peluche" : 50000,
            "Perfume" : 9800,
            "Gretes" : 5000,
            "Dulces" : 5000,
            "Blusa" : 15000,
            "Bono de peluqueria" : 10000,
            "Libros" : 60000
            }



regalo = min(catalogo.keys(), key=lambda k: catalogo[k])

print('\n')

print(regalo)
print(catalogo[regalo])