from itertools import product


items = [
    {
        'producto': 'camisa',
        'price' : 100
    },
    {
        'producto': 'pantalones',
        'price' : 300
    },
    {
        'producto': 'zapatos',
        'price': 200
    }
]
        #recibe una función item es cada uno de los diccionarios
        #de ese diccionario solo devuelveme el precio
        #iterado de la lista items
prices = list(map(lambda item: item['price'], items))
products= list(map(lambda item: item['producto'], items))

print(prices)
print(products)

# agregar un atributo a nuestros diccionarios dentro de nuestra lista

# creo una función porque necesito tener el item, agregar un elemento y retornarlo
# implica más de 2 lineas

def add_taxes(item):
    new_item = item.copy() # Crear copia del array, para no reemplazar el original
    new_item['taxes'] = new_item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
